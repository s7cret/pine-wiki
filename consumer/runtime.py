"""Lower resolved calls into operations; execute without rebinding names/prose."""
import copy,hashlib,json,math,sys
from pathlib import Path
from .errors import Diagnostic


OPERATORS=['+','-','*','/','%','==','!=','<','>','<=','>=','and','or','not']
DEFAULT_OPERATIONS={'numeric.abs','numeric.round','numeric.int','numeric.float','series.ema','series.true_range',
                    'collection.from','collection.get','context.request','harness.indicator','visual.plot','series.history',
                    *('operator.'+op for op in OPERATORS)}


def hash_value(value):return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()


def source_identity():
    files=sorted(Path(__file__).parent.glob('*.py'))
    return hash_value({p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in files})


def build_identity(operations):return hash_value({'implementation':'pine-wiki-offline-consumer.1','source_sha256':source_identity(),'python_version':list(sys.version_info[:3]),'operations':sorted(operations)})


def lower(resolved,operations=None):
    operations=set(DEFAULT_OPERATIONS if operations is None else operations)
    missing=set(resolved['required_operations'])-operations
    if missing:raise Diagnostic('IMPLEMENTATION_MISSING','Missing operations: '+', '.join(sorted(missing)),'rule.admission.capabilities')
    ir=copy.deepcopy(resolved)
    facts={f['call_node']:f for f in resolved['resolved_calls']}
    def walk(value):
        if isinstance(value,list):return [walk(v) for v in value]
        if not isinstance(value,dict):return value
        out={k:walk(v) for k,v in value.items() if k not in ('arguments',) or value.get('kind')!='call'}
        if value.get('kind')=='call':
            out['kind']='operation';out['operation']=facts[value['node_id']]['operation']
            # Runtime receives already resolved parameter identities/order.
            out.pop('name',None)
        return out
    ir['ast']=walk(resolved['ast']);ir['format']='pine-wiki.lowered-program.1';ir['build_identity']=build_identity(operations)
    ir['compile_cache_key']=hash_value({'source':ir['source_sha256'],'semantic_hash':ir['semantic_hash'],'build':ir['build_identity']})
    ir['artifact_hash']=hash_value(ir)
    return ir


def formula(expr,arguments):
    kind=expr['kind']
    if kind=='literal':return expr['value']
    if kind=='argument':return arguments[expr['name']]
    if kind!='operation':raise Diagnostic('SPEC_UNRESOLVED','Unknown formula node','rule.formula')
    values=[formula(x,arguments) for x in expr['arguments']];op=expr['operation']
    if any(v is None for v in values):return None
    if op=='add':return sum(values)
    if op=='subtract':return values[0]-values[1]
    if op=='multiply':return math.prod(values)
    if op=='divide':return values[0]/values[1]
    if op=='abs':return abs(values[0])
    if op=='max':return max(values)
    raise Diagnostic('SPEC_UNRESOLVED','Unknown formula operation '+op,'rule.formula')


def boolean_evaluation(policy,version,operator,left,right):
    mode=policy['v'+str(version)+'_and_or'];a=left()
    if mode=='lazy':
        if operator=='and' and not a:return False
        if operator=='or' and a:return True
    elif mode!='strict':raise Diagnostic('IMPLEMENTATION_MISSING','Unknown boolean evaluation policy','rule.execution.skipped_call')
    b=right();return bool(a and b) if operator=='and' else bool(a or b)


class StatePhases:
    """The shared initialize/update/commit/rollback policy, independently testable."""
    def __init__(self,policy):self.policy=policy;self.committed={};self.ordinary={};self.varip={}
    def update(self,confirmed=False):
        if self.policy.get('ordinary')!='restore_last_commit_before_update' or self.policy.get('varip')!='persist_intrabar':
            raise Diagnostic('IMPLEMENTATION_MISSING','Rollback policy not implemented','rule.execution.rollback')
        self.ordinary=copy.deepcopy(self.committed)
        return self.ordinary,self.varip
    def commit(self):self.committed=copy.deepcopy(self.ordinary)


class Runtime:
    def __init__(self,bundle,operations=None):
        self.bundle=bundle;self.operations=set(DEFAULT_OPERATIONS if operations is None else operations)
        registry=bundle['semantic']['registry'];assertions={a['assertion_id']:a for a in registry['assertions']};decisions={d['decision_id']:d for d in registry['decisions']}
        self.rules={}
        for r in registry['rules']:
            a=assertions[r['semantic_assertion']];d=decisions.get(a.get('decision_ref'))
            if a['review_status']=='corroborated' and d and d['status']=='accepted':self.rules[r['rule_id']]=assertions[d['selected_assertion']]['value']
        self.rule_proof={r['rule_id']:assertions[r['semantic_assertion']] for r in registry['rules']}
        self.source_proof={a['assertion_id']:a['evidence_refs'] for a in bundle['evidence']['assertion_evidence']}
        self.state={};self.events=[];self.plots={};self.current_plot={};self.values={};self.persisted={};self.once=set();self.request_cache={};self.histories={};self.request_keys=set()

    def failure(self,category,message,node=None,rule='rule.runtime',reason=None):
        a=self.rule_proof.get(rule,{})
        raise Diagnostic(category,message,rule,(node or {}).get('span'),reason,self.source_proof.get(a.get('assertion_id'),[]),a.get('decision_ref'))

    def admit(self,ir,context):
        if ir.get('artifact_hash')!=hash_value({k:v for k,v in ir.items() if k!='artifact_hash'}):self.failure('ARTIFACT_INCOMPATIBLE','Artifact contents were changed')
        if ir.get('format')!='pine-wiki.lowered-program.1' or ir.get('semantic_hash')!=self.bundle['manifest']['semantic_hash'] or ir.get('semantic_profile_id')!=self.bundle['manifest']['semantic_profile_id']:
            self.failure('ARTIFACT_INCOMPATIBLE','Artifact profile or semantic identity differs')
        if ir.get('build_identity')!=build_identity(self.operations):self.failure('ARTIFACT_INCOMPATIBLE','Artifact implementation build differs')
        if not context.get('chart_bars') or not context.get('symbol') or not context.get('timeframe'):self.failure('CONTEXT_UNAVAILABLE','Chart data/context missing')
        if context.get('mode')!='historical_confirmed':self.failure('ARTIFACT_INCOMPATIBLE','Only confirmed historical execution is in this profile',reason='PROFILE_UNCOVERED')
        needed=set(ir['required_operations'])-self.operations
        if needed:self.failure('IMPLEMENTATION_MISSING','Required operation not available: '+str(sorted(needed)))

    def symbol(self,name,bars,index,context):
        bar=bars[index]
        if name in ('open','high','low','close','time'):
            if name not in bar:self.failure('CONTEXT_UNAVAILABLE','Missing bar field '+name,rule='rule.context.current')
            return bar[name]
        if name=='bar_index':return index
        if name=='barstate.isconfirmed':return True
        if name=='barstate.isrealtime':return False
        if name=='barstate.islast':return index==len(bars)-1
        if name=='barstate.isfirst':return index==0
        if name=='syminfo.tickerid':return context['symbol']
        if name=='timeframe.period':return context['timeframe']
        if name=='ta.tr':return self.true_range(bars,index,False)
        if name.startswith('barmerge.') or name=='currency.NONE':return name
        self.failure('SPEC_UNRESOLVED','Missing symbol semantics '+name,rule='rule.symbol')

    def true_range(self,bars,index,handle_na):
        if not all(k in bars[index] for k in ('high','low')) or index and 'close' not in bars[index-1]:
            self.failure('CONTEXT_UNAVAILABLE','True range requires high, low and previous close',rule='rule.tr.true')
        previous=bars[index-1].get('close') if index else None
        policy=self.rules['rule.tr.true' if handle_na else 'rule.tr.false'];bar=bars[index]
        if previous is None:return bar['high']-bar['low'] if policy['previous_close_na']=='high-low' else None
        return formula(policy['formula'],{'high':bar['high'],'low':bar['low'],'previous_close':previous})

    def evaluate(self,node,bars,index,context,values):
        kind=node['kind']
        if kind=='literal':return node['value']
        if kind=='context_default':
            if node['rule_ref']=='rule.request.chart_bars':return len(self.context['chart_bars'])
            self.failure('SPEC_UNRESOLVED','Contextual default rule missing',node)
        if kind=='name':return values[node['binding_id']] if 'binding_id' in node else self.symbol(node['name'],bars,index,context)
        if kind=='tuple':return tuple(self.evaluate(n,bars,index,context,values) for n in node['members'])
        if kind=='unary':
            value=self.evaluate(node['operand'],bars,index,context,values)
            if node['operator']=='not':return not value
            return None if value is None else -value if node['operator']=='-' else +value
        if kind=='binary':
            op=node['operator']
            if op in ('and','or'):
                return boolean_evaluation(self.rules['rule.execution.skipped_call'],6,op,lambda:self.evaluate(node['left'],bars,index,context,values),lambda:self.evaluate(node['right'],bars,index,context,values))
            a=self.evaluate(node['left'],bars,index,context,values)
            b=self.evaluate(node['right'],bars,index,context,values)
            if a is None or b is None:return False if op in ('==','!=','<','>','<=','>=') else None
            if op=='+':return a+b
            if op=='-':return a-b
            if op=='*':return a*b
            if op=='/':return a/b if b else None
            if op=='%':return math.fmod(a,b) if b else None
            if op=='==':return a==b
            if op=='!=':return a!=b
            if op=='<':return a<b
            if op=='>':return a>b
            if op=='<=':return a<=b
            if op=='>=':return a>=b
        if kind=='conditional':
            value=self.evaluate(node['yes'] if self.evaluate(node['condition'],bars,index,context,values) else node['no'],bars,index,context,values)
            return float(value) if type(value) is int and node.get('resolved',{}).get('type',{}).get('name')=='float' else value
        if kind=='history':
            offset=self.evaluate(node['offset'],bars,index,context,values)
            if not isinstance(offset,int) or isinstance(offset,bool) or offset<0:self.failure('LANGUAGE_INVALID','History offset must be nonnegative int',node,'rule.types')
            expression=node['expression'];key=(context['context_id'],node['node_id'])
            if expression['kind']=='name' and 'symbol_id' in expression:
                return None if index-offset<0 else self.symbol(expression['name'],bars,index-offset,context)
            if expression['kind']=='name' and 'binding_id' in expression:
                return values.get(expression['binding_id']) if offset==0 else self.histories.get((context['context_id'],expression['binding_id']),{}).get(index-offset)
            current=self.evaluate(expression,bars,index,context,values)
            history=self.histories.setdefault(key,{})
            history[index]=current
            return history.get(index-offset)
        if kind=='operation':return self.operation(node,bars,index,context,values)
        self.failure('ARTIFACT_INCOMPATIBLE','Unknown IR node '+kind,node)

    def operation(self,node,bars,index,context,values):
        op=node['operation']
        if op not in self.operations:self.failure('IMPLEMENTATION_MISSING',op,node)
        params=node['bound_arguments'];arguments={};deferred={}
        evaluation=[]
        for p in params:
            if p['evaluation_policy']=='requested_context':deferred[p['name']]=p['nodes'][0]
            else:
                for rank,expr in zip(p['source_order'],p['nodes']):evaluation.append((rank,p,expr))
        for _,p,expr in sorted(evaluation,key=lambda item:item[0]):
            value=self.evaluate(expr,bars,index,context,values)
            if p['variadic']:arguments.setdefault(p['name'],[]).append(value)
            else:arguments[p['name']]=value
        if op=='harness.indicator':return None
        if op=='visual.plot':
            title=arguments['title'] or node['node_id'];self.current_plot[title]=arguments['series'];return None
        if op=='numeric.abs':return None if arguments['number'] is None else abs(arguments['number'])
        if op=='numeric.round':
            if self.rules['rule.numeric.round']['ties']!='toward_positive_infinity':self.failure('IMPLEMENTATION_MISSING','Rounding tie policy not implemented',node,'rule.numeric.round')
            number=arguments['number']
            if number is None:return None
            precision=arguments.get('precision',0)
            bounds=self.rules['rule.numeric.round']['precision_profile']
            if not isinstance(precision,int) or isinstance(precision,bool) or not bounds[0]<=precision<=bounds[1]:
                self.failure('ARTIFACT_INCOMPATIBLE','Precision outside declared numeric profile',node,'rule.numeric.round','PROFILE_UNCOVERED')
            scale=10**precision;result=math.floor(number*scale+0.5)/scale
            return float(result) if 'precision' in arguments else int(result)
        if op in ('numeric.int','numeric.float'):
            value=arguments['x'];return None if value is None else int(value) if op=='numeric.int' else float(value)
        if op=='collection.from':
            array=list(arguments['args'])
            if any(type(x) is float for x in array):array=[float(x) if type(x) is int else x for x in array]
            self.events.append({'event':'allocate_array','node':node['node_id'],'context':context['context_id'],'bar':index})
            return array
        if op=='collection.get':
            array=arguments['id'];offset=arguments['index']
            if type(offset) is not int or not 0<=offset<len(array):self.failure('LANGUAGE_INVALID','Array index out of range',node,'rule.array.index')
            return array[offset]
        if op=='series.true_range':return self.true_range(bars,index,arguments['handle_na'])
        if op=='series.ema':
            source,length=arguments['source'],arguments['length']
            if type(length) is not int or length<=0:self.failure('LANGUAGE_INVALID','EMA length must be a positive integer',node,'rule.ema.length')
            policy=self.rules['rule.ema'];key=(node['node_id'],context['context_id']);previous=self.state.get(key)
            if policy['seed']!='first_non_na_source':self.failure('IMPLEMENTATION_MISSING','EMA seed policy not implemented',node,'rule.ema')
            if source is None and policy['na_policy']=='ignore_source_na':return previous
            alpha=formula(policy['alpha'],{'length':length})
            value=source if previous is None else formula(policy['update'],{'source':source,'previous':previous,'alpha':alpha})
            self.state[key]=value;self.events.append({'event':'state_update','node':node['node_id'],'context':context['context_id'],'bar':index,'value':value})
            return value
        if op=='context.request':
            symbol=arguments['symbol'] or context['symbol'];timeframe=arguments['timeframe'] or context['timeframe']
            if arguments['currency']!='currency.NONE':self.failure('ARTIFACT_INCOMPATIBLE','Currency conversion is outside this profile',node,'rule.uncovered.currency','PROFILE_UNCOVERED')
            if arguments.get('ignore_invalid_symbol'):self.failure('ARTIFACT_INCOMPATIBLE','Ignoring invalid symbols requires another profile',node,'rule.uncovered.request_symbol','PROFILE_UNCOVERED')
            if arguments['lookahead']!='barmerge.lookahead_off':self.failure('ARTIFACT_INCOMPATIBLE','lookahead_on is known but outside the confirmed-history profile',node,'rule.request.alignment','PROFILE_UNCOVERED')
            requested=next((c for c in self.context.get('requested_contexts',[]) if c['symbol']==symbol and c['timeframe']==timeframe),None)
            if requested is None:
                if symbol==self.context['symbol'] and timeframe==self.context['timeframe']:
                    requested={'context_id':self.context['context_id'],'symbol':symbol,'timeframe':timeframe,'bars':self.context['chart_bars']}
                else:self.failure('CONTEXT_UNAVAILABLE','Requested context missing: '+symbol+' / '+timeframe,node,'rule.request.alignment')
            count=arguments['calc_bars_count']
            if type(count) is not int or count<=0:self.failure('LANGUAGE_INVALID','calc_bars_count must be positive in this profile',node,'rule.request.chart_bars')
            def semantic_expression(value):
                if isinstance(value,list):return [semantic_expression(v) for v in value]
                if isinstance(value,dict):return {k:semantic_expression(v) for k,v in value.items() if k not in ('node_id','span','resolved','source_span')}
                return value
            request_key=(symbol,timeframe,hash_value(semantic_expression(deferred['expression'])),arguments['gaps'],arguments['lookahead'],count)
            self.request_keys.add(request_key)
            limit=self.rules['rule.platform.request.unique']['limits']['ultimate' if self.context.get('plan')=='ultimate' else 'standard']
            if len(self.request_keys)>limit:self.failure('CONTEXT_UNAVAILABLE','Unique request limit exceeded',node,'rule.platform.request.unique')
            cache=(node['node_id'],requested['context_id'],count)
            if cache not in self.request_cache:
                if not requested.get('bars') or not all('close_time' in b for b in requested['bars']) or not all('close_time' in b for b in bars):
                    self.failure('CONTEXT_UNAVAILABLE','Request alignment requires nonempty bars with close_time',node,'rule.request.alignment')
                remote_bars=requested['bars'][-count:];remote_context={**requested,'mode':'historical_confirmed'};series=[]
                for remote_index,bar in enumerate(remote_bars):
                    result=self.evaluate(deferred['expression'],remote_bars,remote_index,remote_context,{})
                    series.append((bar['close_time'],result))
                self.request_cache[cache]=series
            eligible=[(i,value) for i,(close,value) in enumerate(self.request_cache[cache]) if close<=bars[index]['close_time']]
            if not eligible:
                typ=node.get('resolved',{}).get('type',{})
                return tuple(None for _ in typ.get('members',[])) if typ.get('kind')=='tuple' else None
            remote_index,value=eligible[-1]
            if arguments['gaps']=='barmerge.gaps_on':
                previous_end=bars[index-1]['close_time'] if index else float('-inf')
                if self.request_cache[cache][remote_index][0]<=previous_end:
                    return tuple(None for _ in value) if isinstance(value,tuple) else None
            return value
        self.failure('IMPLEMENTATION_MISSING','Unknown semantic operation '+op,node)

    def statements(self,statements,bars,index,context,values):
        for node in statements:
            kind=node['kind']
            if kind in ('declaration','reassignment'):
                key=(node['binding_id'],context['context_id'])
                if kind=='declaration' and node['mode'] in ('var','varip') and key in self.persisted:value=self.persisted[key]
                else:value=self.evaluate(node['value'],bars,index,context,values)
                if node.get('annotation')=='float' and type(value) is int:value=float(value)
                values[node['binding_id']]=value
                if node.get('mode') in ('var','varip') or key in self.persisted:self.persisted[key]=value
            elif kind=='tuple_declaration':
                result=self.evaluate(node['value'],bars,index,context,values)
                for bid,value in zip(node['binding_ids'],result):values[bid]=value
            elif kind=='expression_statement':self.evaluate(node['expression'],bars,index,context,values)
            elif kind=='if':self.statements(node['body'] if self.evaluate(node['condition'],bars,index,context,values) else node['otherwise'],bars,index,context,values)
            elif kind=='once':
                key=(node['node_id'],context['context_id'])
                if key not in self.once and (node['condition'] is None or self.evaluate(node['condition'],bars,index,context,values)):
                    self.statements(node['body'],bars,index,context,values);self.once.add(key)

    def run(self,ir,context):
        self.admit(ir,context);self.context=context
        bars=context['chart_bars']
        for index,bar in enumerate(bars):
            self.current_plot={};values={};self.statements(ir['ast']['statements'],bars,index,context,values)
            for title in set(self.plots)|set(self.current_plot):self.plots.setdefault(title,[None]*index).append(self.current_plot.get(title))
            for bid,value in values.items():self.histories.setdefault((context['context_id'],bid),{})[index]=copy.deepcopy(value)
        return {'plots':self.plots,'events':self.events,'semantic_hash':ir['semantic_hash'],'build_identity':ir['build_identity'],
                'context_identity':hash_value(context),'runtime_cache_key':hash_value({'compile_key':ir['compile_cache_key'],'context':hash_value(context)})}
