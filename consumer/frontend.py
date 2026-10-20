"""Resolve names, ordered arguments, overloads, types and defaults exactly once."""
import copy,hashlib,json
from tools.spec_bundle import effective
from .errors import Diagnostic,invalid
from .parser import parse


def primitive(name):return {'kind':'primitive','name':name}


class Frontend:
    def __init__(self,bundle):
        self.bundle=bundle;self.registry=bundle['semantic']['registry'];self.manifest=bundle['manifest']
        self.assertions={a['assertion_id']:a for a in self.registry['assertions']}
        self.decisions={d['decision_id']:d for d in self.registry['decisions']}
        self.rules={r['rule_id']:r for r in self.registry['rules']}
        self.symbols={(s['kind'],s['name']):s for s in self.registry['symbols']}
        self.known_symbols={a['symbol_id'] for a in bundle['identities']['aliases'] if ':v6:' in a['entry_id']}
        self.evidence={a['assertion_id']:a['evidence_refs'] for a in bundle['evidence']['assertion_evidence']}
        self.facts=[];self.scopes=[{}];self.binding_serial=0;self.operations=set();self.obligations=[];self.used_rules=set();self.deferred_depth=0
        self.type_rules=self.rule('rule.types');self.qualifiers=self.type_rules['qualifier_order']

    def fail(self,category,message,rule_id,span=None,reason=None,assertion=None):
        a=assertion or self.assertions.get(rule_id) or self.assertions.get((self.rules.get(rule_id) or {}).get('semantic_assertion'),{})
        raise Diagnostic(category,message,rule_id,span,reason,self.evidence.get(a.get('assertion_id'),[]),a.get('decision_ref'),a.get('issue_refs'))

    def effective(self,aid,span=None):
        a=self.assertions[aid];value=effective(a,self.registry,version=6,profile_id=self.manifest['semantic_profile_id'])
        if value.get('kind')=='unknown' and value.get('reason')=='SPEC_UNRESOLVED':
            self.fail('SPEC_UNRESOLVED','Required assertion is not resolved: '+aid,aid,span,assertion=a)
        return value

    def rule(self,rid,span=None):
        self.used_rules.add(rid)
        if rid not in self.rules:self.fail('SPEC_UNRESOLVED','Missing rule '+rid,rid,span)
        return self.effective(self.rules[rid]['semantic_assertion'],span)

    def describe(self,typ,qualifier='const',known=False,value=None):return {'type':typ,'qualifier':qualifier,'known':known,'value':value}

    def strongest(self,infos):return max((x['qualifier'] for x in infos),key=self.qualifiers.index,default='const')

    def variable(self,name):
        return next((s[name] for s in reversed(self.scopes) if name in s),None)

    def bind_new(self,name,info,span,mode='normal'):
        self.rule('rule.scope',span)
        if name in self.scopes[-1]:invalid('Already declared in this scope: '+name,'rule.scope',span)
        self.binding_serial+=1;bid='binding.'+str(self.binding_serial)
        self.scopes[-1][name]={'binding_id':bid,'info':info,'mode':mode}
        return bid

    def match(self,expected,actual,substitutions):
        kind=expected['kind'];typ=actual['type']
        if kind=='type_variable':
            name=expected['name']
            previous=substitutions.get(name)
            if previous is None:substitutions[name]=typ;return True
            if previous==typ:return True
            if previous.get('name') in ('int','float') and typ.get('name') in ('int','float') and ['int','float'] in self.type_rules['implicit_conversions']:
                substitutions[name]=primitive('float');return True
            return False
        if kind=='alternative':
            for option in expected['options']:
                candidate=copy.deepcopy(substitutions)
                if self.match(option,actual,candidate):substitutions.update(candidate);return True
            return False
        if kind=='generic':
            return typ.get('kind')=='generic' and typ.get('name')==expected['name'] and len(typ['arguments'])==len(expected['arguments']) and all(self.match(a,self.describe(t,actual['qualifier']),substitutions) for a,t in zip(expected['arguments'],typ['arguments']))
        if typ==primitive('na'):return expected.get('name') in ('int','float','string','color')
        if expected==typ:return True
        return [typ.get('name'),expected.get('name')] in self.type_rules['implicit_conversions']

    def result(self,result,bound,subs,infos):
        if result['kind']=='void':return self.describe(primitive('void'))
        if result['kind']=='dependent':typ=next(b['info']['type'] for b in bound if b['name']==result['parameter'])
        elif result['kind']=='tuple':typ={'kind':'tuple','members':[self.result(m,bound,subs,infos)['type'] for m in result['members']]}
        else:typ=copy.deepcopy(result['type'])
        def substitute(t):
            if t['kind']=='type_variable':return copy.deepcopy(subs.get(t['name'],{'kind':'unknown'}))
            if t['kind']=='generic':return {**t,'arguments':[substitute(a) for a in t['arguments']]}
            return t
        typ=substitute(typ)
        qualifier=result.get('qualifier',{})
        if qualifier.get('relation')=='exact':q=qualifier['value']
        elif qualifier.get('from')=='arguments':q=self.strongest(infos)
        else:q=next(b['info']['qualifier'] for b in bound if b['name']==qualifier['from'])
        if typ.get('kind')=='generic':q=self.rule('rule.types')['reference_qualifier']
        return self.describe(typ,q)

    def default_node(self,p,span):
        default=p['default'];kind=default['kind']
        if p['requiredness']['state'] in ('conditional','unknown','conflict'):
            self.fail('SPEC_UNRESOLVED','Omission depends on unresolved requiredness: '+p['name'],'rule.binding',span)
        if kind=='none':invalid('Missing argument '+p['name'],'rule.binding',span)
        if kind=='unknown':self.fail('SPEC_UNRESOLVED','Needed default is unresolved: '+p['name'],default.get('assertion_ref','rule.default'),span,reason=default.get('reason'))
        base={'node_id':'default.'+p['parameter_id'],'span':span}
        if kind=='literal':
            value=default['value'];typ='json_null' if value is None else 'bool' if isinstance(value,bool) else 'int' if isinstance(value,int) else 'float' if isinstance(value,float) else 'string'
            return {**base,'kind':'literal','value':value,'type':typ}
        if kind=='na':return {**base,'kind':'literal','value':None,'type':'na'}
        if kind=='symbol':return {**base,'kind':'name','name':default['symbol_ref']}
        if kind=='expression':
            self.rule(default['rule_ref'],span)
            return {**base,'kind':'context_default','rule_ref':default['rule_ref'],'type':p['type']}
        self.fail('SPEC_UNRESOLVED','Unsupported default expression','rule.default',span)

    def resolve_call(self,node):
        self.rule('rule.binding',node['span']);self.rule('rule.overload',node['span'])
        if node['name'] in self.rule('rule.scope',node['span'])['global_only_calls'] and len(self.scopes)>1:
            invalid('Call requires global scope: '+node['name'],'rule.scope',node['span'])
        if self.deferred_depth and node['name']=='request.security':
            self.fail('ARTIFACT_INCOMPATIBLE','Nested requests are outside this profile','rule.uncovered.nested_requests',node['span'],'PROFILE_UNCOVERED')
        symbol=self.symbols.get(('function',node['name']))
        if not symbol:
            reason='PROFILE_UNCOVERED' if 'symbol.function.'+node['name'] in self.known_symbols or any(node['name'].startswith(ns) for ns in ('ta.','math.','array.','request.','input.','strategy.')) else None
            self.fail('ARTIFACT_INCOMPATIBLE' if reason else 'LANGUAGE_INVALID','Function is unavailable in this profile: '+node['name'],'rule.uncovered.builtin' if reason else 'rule.binding',node['span'],reason)
        arguments=[];seen_named=False;seen=set()
        for index,a in enumerate(node['arguments']):
            if a['name']:
                seen_named=True
                if a['name'] in seen:invalid('Duplicate named argument '+a['name'],'rule.binding',node['span'])
                seen.add(a['name'])
            elif seen_named:invalid('Positional argument after a named argument','rule.binding',node['span'])
            # Defer evaluation, not type checking, of request expression.
            is_request_expression=node['name']=='request.security' and (a['name']=='expression' or a['name'] is None and index==2)
            if is_request_expression:self.deferred_depth+=1
            info=self.expression(a['expression'])
            if is_request_expression:self.deferred_depth-=1
            arguments.append({**a,'info':info,'source_order':index})
        if node['name']=='array.from':
            policy=self.rule('rule.array.element',node['span'])
            if any(a['info']['type'].get('kind')!='primitive' or a['info']['type'].get('name') not in policy['profile_element_types'] for a in arguments):
                self.fail('ARTIFACT_INCOMPATIBLE','Collection element type is outside the declared profile','rule.uncovered.nested_collections',node['span'],'PROFILE_UNCOVERED')
        candidates=[];errors=[]
        for ov in symbol['overloads']:
            signature=self.effective(ov['signature_assertion'],node['span']);params=signature['parameters'];bound=[];subs={};used=set()
            try:
                names={p['name']:p for p in params};position=0
                grouped={p['name']:[] for p in params}
                for a in arguments:
                    if a['name'] and not signature['binding']['named'] or a['name'] is None and not signature['binding']['positional']:
                        invalid('Argument form is not accepted by this contract','rule.binding',node['span'])
                    if a['name']:
                        if a['name'] not in names:invalid('Unknown named argument '+a['name'],'rule.binding',node['span'])
                        p=names[a['name']]
                    else:
                        if position>=len(params):invalid('Too many arguments','rule.binding',node['span'])
                        p=params[position]
                        if not p['variadic']:position+=1
                    if grouped[p['name']] and not p['variadic']:invalid('Parameter passed twice: '+p['name'],'rule.binding',node['span'])
                    grouped[p['name']].append(a)
                for p in params:
                    supplied=grouped[p['name']]
                    if not supplied:
                        value=self.default_node(p,node['span']);supplied=[{'expression':value,'info':self.expression(value),'source_order':len(arguments)+len(bound),'inserted_default':True}]
                    for arg in supplied:
                        q=p['qualifier_constraint']
                        if q['relation']=='unknown':self.fail('SPEC_UNRESOLVED','Qualifier constraint unknown','rule.types',node['span'])
                        if q['relation']=='derived':self.fail('IMPLEMENTATION_MISSING','Derived parameter constraint is outside this consumer','rule.types',node['span'])
                        if q['relation']=='exact' and arg['info']['qualifier']!=q['value'] or q['relation']=='at_most' and self.qualifiers.index(arg['info']['qualifier'])>self.qualifiers.index(q['value']):invalid('Argument qualifier violates '+q['relation']+' '+q['value']+': '+p['name'],'rule.types',node['span'])
                        if not self.match(p['type'],arg['info'],subs):invalid('Argument type mismatch: '+p['name'],'rule.types',node['span'])
                    info=self.describe(subs.get('T',supplied[0]['info']['type']) if p['variadic'] else supplied[0]['info']['type'],self.strongest([a['info'] for a in supplied]))
                    bound.append({'parameter_id':p['parameter_id'],'name':p['name'],'expressions':[a['expression']['node_id'] for a in supplied],'source_order':[a['source_order'] for a in supplied],'inserted_default':any(a.get('inserted_default') for a in supplied),'evaluation_policy':p['evaluation_policy'],'variadic':p['variadic'],'info':info,'nodes':[a['expression'] for a in supplied]})
                result=self.result(signature['result'],bound,subs,[a['info'] for a in arguments])
                candidates.append((ov,signature,bound,result))
            except Diagnostic as exc:errors.append(exc)
        if len(candidates)!=1:
            if len(candidates)>1:invalid('Ambiguous overload','rule.overload',node['span'])
            unresolved=next((e for e in errors if e.data['category']=='SPEC_UNRESOLVED'),None)
            if unresolved:raise unresolved
            if errors:raise errors[-1]
            invalid('No matching overload','rule.overload',node['span'])
        ov,signature,bound,result=candidates[0]
        for b in bound:
            if b['name']=='length' and node['name']=='ta.ema':
                self.rule('rule.ema.length',node['span']);arg=b['nodes'][0]
                if arg.get('resolved',{}).get('known') and (arg['resolved']['value'] is None or arg['resolved']['value']<=0):invalid('EMA length must be positive','rule.ema.length',node['span'])
                self.obligations.append({'rule_id':'rule.ema.length','call_node':node['node_id'],'parameter_id':b['parameter_id'],'phase':'runtime'})
        refs=['rule.arguments.left_to_right','rule.context.current','rule.state.call_site_context','rule.execution.skipped_call']
        if node['name']=='ta.ema':refs+=['rule.ema']
        if node['name']=='math.round':refs+=['rule.numeric.round']
        if node['name']=='ta.tr':refs+=['rule.tr.true','rule.tr.false']
        if node['name']=='array.get':refs+=['rule.array.index']
        if node['name']=='array.from':refs+=['rule.array.element']
        if node['name']=='request.security':
            refs+=['rule.request.alignment','rule.platform.request.unique']
            if any(b['name']=='lookahead' and b['inserted_default'] for b in bound):refs+=['rule.request.lookahead.default']
        for rid in refs:self.rule(rid,node['span'])
        self.operations.add(signature['operation'])
        fact={'call_node':node['node_id'],'symbol_id':symbol['symbol_id'],'overload_id':ov['overload_id'],'parameter_bindings':[{k:v for k,v in b.items() if k!='nodes'} for b in bound],
              'resolved_type':result['type'],'resolved_qualifier':result['qualifier'],'inserted_defaults':[b['parameter_id'] for b in bound if b['inserted_default']],
              'evaluation_rules':refs,'operation':signature['operation'],'effects':signature['effects'],'semantic_hash':self.manifest['semantic_hash'],'source_span':node['span']}
        self.facts.append(fact);node['bound_arguments']=[{k:v for k,v in b.items() if k!='info'} for b in bound]
        return result

    def expression(self,node):
        kind=node['kind'];span=node['span']
        if kind=='literal':info=self.describe(primitive(node['type']),known=True,value=node['value'])
        elif kind=='context_default':info=self.describe(node['type'],'simple')
        elif kind=='name':
            local=self.variable(node['name'])
            if local:
                if self.deferred_depth and not local['info']['known']:
                    self.fail('ARTIFACT_INCOMPATIBLE','Dynamic outer captures require the next profile','rule.uncovered.request_captures',span,'PROFILE_UNCOVERED')
                node['binding_id']=local['binding_id'];info=copy.deepcopy(local['info'])
                if self.deferred_depth:node['constant_capture']=copy.deepcopy(info['value'])
            else:
                s=self.symbols.get(('variable',node['name'])) or self.symbols.get(('constant',node['name']))
                if not s:
                    if any('symbol.'+kind+'.'+node['name'] in self.known_symbols for kind in ('variable','constant')):
                        self.fail('ARTIFACT_INCOMPATIBLE','Known symbol outside this profile: '+node['name'],'rule.uncovered.symbol',span,'PROFILE_UNCOVERED')
                    invalid('Undefined symbol '+node['name'],'rule.scope',span)
                value=self.effective(s['value_assertion_ref'],span);node['symbol_id']=s['symbol_id']
                info=self.describe(value['type'],value['qualifier'])
                if s['name']=='ta.tr':self.rule('rule.tr.false',span);self.operations.add('series.true_range')
        elif kind=='call':info=self.resolve_call(node)
        elif kind=='tuple':
            infos=[self.expression(n) for n in node['members']];info=self.describe({'kind':'tuple','members':[i['type'] for i in infos]},self.strongest(infos))
        elif kind=='history':
            policy=self.rule('rule.history',span)
            if node['expression']['kind']=='literal' and policy['literal_history']=='forbidden':invalid('History of literal values is forbidden in v6','rule.history',span)
            value=self.expression(node['expression']);offset=self.expression(node['offset'])
            if offset['type']!=primitive('int'):invalid('History offset must be an integer','rule.types',span)
            if offset['known'] and offset['value']<0:invalid('History offset must be nonnegative','rule.types',span)
            self.operations.add('series.history');info=self.describe(value['type'],'series')
        elif kind=='unary':
            value=self.expression(node['operand']);op=node['operator']
            if op=='not' and value['type']!=primitive('bool') or op!='not' and value['type'].get('name') not in ('int','float'):invalid('Invalid unary operand','rule.types',span)
            self.operations.add('operator.'+op);info=self.describe(value['type'],value['qualifier'])
            if value['known']:
                info.update(known=True,value=not value['value'] if op=='not' else -value['value'] if op=='-' else +value['value'])
        elif kind=='binary':
            a=self.expression(node['left']);b=self.expression(node['right']);op=node['operator']
            if op in ('and','or'):
                if a['type']!=primitive('bool') or b['type']!=primitive('bool'):invalid('Boolean operands required','rule.types',span)
                typ=primitive('bool');self.rule('rule.execution.skipped_call',span)
            elif op in ('==','!=','<','>','<=','>='):
                an,bn=a['type'].get('name'),b['type'].get('name')
                if op in ('<','>','<=','>=') and not (an in ('int','float') and bn in ('int','float')):invalid('Ordering requires numeric operands','rule.types',span)
                if a['type']!=b['type'] and not ({an,bn}<={'int','float','na'}):invalid('Incompatible comparison operands','rule.types',span)
                typ=primitive('bool')
            else:
                if a['type'].get('name') not in ('int','float') or b['type'].get('name') not in ('int','float'):invalid('Numeric operands required','rule.types',span)
                typ=primitive('float' if op=='/' or 'float' in (a['type']['name'],b['type']['name']) else 'int')
            self.operations.add('operator.'+op);info=self.describe(typ,self.strongest([a,b]))
            if op=='%':self.rule('rule.numeric.modulo',span)
            if a['known'] and b['known']:
                av,bv=a['value'],b['value']
                if av is not None and bv is not None:
                    if op in ('/','%') and bv==0:info.update(known=True,value=None)
                    else:
                        folded={'+':lambda:av+bv,'-':lambda:av-bv,'*':lambda:av*bv,'/':lambda:av/bv,'%':lambda:av%bv,
                                '==':lambda:av==bv,'!=':lambda:av!=bv,'<':lambda:av<bv,'>':lambda:av>bv,'<=':lambda:av<=bv,'>=':lambda:av>=bv,
                                'and':lambda:av and bv,'or':lambda:av or bv}
                        info.update(known=True,value=folded[op]())
        elif kind=='conditional':
            cond=self.expression(node['condition']);a=self.expression(node['yes']);b=self.expression(node['no'])
            if cond['type']!=primitive('bool'):invalid('Bool condition required','rule.types',span)
            typ=a['type']
            if a['type']!=b['type']:
                names={a['type'].get('name'),b['type'].get('name')}
                if names<={'int','float','na'}:typ=primitive('float' if 'float' in names else 'int')
                else:invalid('Incompatible conditional branch types','rule.types',span)
            info=self.describe(typ,self.strongest([cond,a,b]))
            chosen=a if cond.get('value') else b
            if cond['known'] and chosen['known']:info.update(known=True,value=chosen['value'])
        else:invalid('Unsupported expression '+kind,'rule.grammar',span)
        node['resolved']=info;return info

    def statements(self,statements):
        for node in statements:
            kind=node['kind'];span=node['span']
            if kind in ('declaration','reassignment'):
                info=self.expression(node['value']);annotation=node.get('annotation')
                if info['type']==primitive('void'):
                    if node['value'].get('kind')=='call' and node['value'].get('name')=='plot':self.fail('ARTIFACT_INCOMPATIBLE','Pine plot handles are outside the observation harness','rule.uncovered.plot_handle',span,'PROFILE_UNCOVERED')
                    invalid('A void result cannot be assigned','rule.types',span)
                if kind=='declaration' and not annotation and info['type']==primitive('na'):invalid('An na initializer needs an explicit type or cast','rule.types',span)
                if annotation:
                    if not self.match(primitive(annotation),info,{}):invalid('Declared type mismatch','rule.types',span)
                    info={**info,'type':primitive(annotation)}
                    if annotation=='float' and info['known'] and type(info['value']) is int:info['value']=float(info['value'])
                if kind=='declaration':
                    if node.get('mutable'):info={**info,'qualifier':'series','known':False}
                    node['binding_id']=self.bind_new(node['name'],info,span,node['mode'])
                else:
                    binding=self.variable(node['name'])
                    if not binding:invalid('Reassignment needs an existing declaration','rule.scope',span)
                    if not self.match(binding['info']['type'],info,{}):invalid('Reassignment type mismatch','rule.types',span)
                    info={**info,'type':binding['info']['type'],'qualifier':'series','known':False}
                    binding['info']=info;node['binding_id']=binding['binding_id']
                    node['annotation']=info['type'].get('name')
                node['resolved']=info
            elif kind=='tuple_declaration':
                info=self.expression(node['value'])
                if info['type']['kind']!='tuple' or len(info['type']['members'])!=len(node['names']):invalid('Tuple arity mismatch','rule.types',span)
                node['binding_ids']=[self.bind_new(name,self.describe(t,info['qualifier']),span,node['mode']) for name,t in zip(node['names'],info['type']['members'])]
            elif kind=='expression_statement':self.expression(node['expression'])
            elif kind in ('if','once'):
                if node.get('condition') and self.expression(node['condition'])['type']!=primitive('bool'):invalid('Bool condition required','rule.types',span)
                self.scopes.append({});self.statements(node['body']);self.scopes.pop()
                if kind=='if':self.scopes.append({});self.statements(node['otherwise']);self.scopes.pop()
                else:self.rule('rule.execution.rollback',span)

    def compile(self,source):
        phase='parse'
        try:
            grammar_policy=self.rule('rule.grammar');ast=parse(source,self.bundle['semantic']['grammar'])
            phase='compile'
            # Pine v6 mutable bindings are series across the whole lexical scope,
            # including calls that precede a later assignment. Shadowed names are separate.
            def mark_mutable(statements,scopes):
                for node in statements:
                    if node['kind']=='declaration':scopes[-1][node['name']]=node
                    elif node['kind']=='tuple_declaration':
                        for name in node['names']:scopes[-1][name]=node
                    elif node['kind']=='reassignment':
                        target=next((scope[node['name']] for scope in reversed(scopes) if node['name'] in scope),None)
                        if target is not None:target['mutable']=True
                    elif node['kind'] in ('if','once'):
                        mark_mutable(node['body'],scopes+[{}]);mark_mutable(node.get('otherwise',[]),scopes+[{}])
            mark_mutable(ast['statements'],[{}]);self.statements(ast['statements'])
            declarations=[c for c in self.facts if c['operation']==grammar_policy['program_declaration_operation']]
            if len(declarations)!=grammar_policy['program_declaration_count']:invalid('Exactly one indicator declaration is required','rule.grammar',ast['span'])
            if not any(c['operation']==grammar_policy['profile_output_operation'] for c in self.facts):
                self.fail('ARTIFACT_INCOMPATIBLE','A plot observation is required by this executable profile','rule.uncovered.output',ast['span'],'PROFILE_UNCOVERED')
        except Diagnostic as error:
            error.data['phase']=phase
            rule=self.rules.get(error.data.get('rule_id'))
            if rule:
                a=self.assertions[rule['semantic_assertion']];error.data['evidence_refs']=self.evidence.get(a['assertion_id'],[]);error.data['decision_ref']=a['decision_ref']
            raise
        return {'format':'pine-wiki.resolved-program.1','language_version':6,'semantic_profile_id':self.manifest['semantic_profile_id'],
                'semantic_hash':self.manifest['semantic_hash'],'source_sha256':hashlib.sha256(source.encode()).hexdigest(),'ast':ast,'resolved_calls':self.facts,
                'required_operations':sorted(self.operations),'rule_refs':sorted(self.used_rules),'runtime_obligations':self.obligations}
