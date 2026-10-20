"""Pratt frontend adapter for spec/grammar.json; no runtime grammar parsing."""
from dataclasses import dataclass
import ast,re
from .errors import Diagnostic,invalid


@dataclass
class Token:
    kind:str
    text:str
    line:int
    column:int
    end:int


class Parser:
    def __init__(self,source,grammar):
        self.grammar=grammar;self.source=source;self.serial=0;self.i=0
        self.precedence={op['token']:op['precedence'] for op in grammar['operators']}
        self.tokens,self.version=self.lex(source)

    def lex(self,source):
        matcher=re.compile(self.grammar['token_pattern']);tokens=[];indent=[0];depth=0;version=None
        for lineno,line in enumerate(source.splitlines(),1):
            directive=re.fullmatch(self.grammar['directive_pattern'],line)
            if directive:
                if version is not None or tokens:invalid('Version directive must appear once before code',span={'line':lineno,'column':1})
                version=int(directive[1]);continue
            if not line.strip() or line.lstrip().startswith('//'):continue
            if re.match(r'\s*(?:method\s+)?[A-Za-z_]\w*\s*\([^)]*\)\s*=>',line):
                raise Diagnostic('ARTIFACT_INCOMPATIBLE','User-defined functions require another profile','rule.uncovered.functions',{'line':lineno,'column':1},reason='PROFILE_UNCOVERED')
            pos=len(line)-len(line.lstrip(' '))
            if '\t' in line[:len(line)-len(line.lstrip())]:raise Diagnostic('ARTIFACT_INCOMPATIBLE','Tab indentation is outside this profile','rule.uncovered.indentation',{'line':lineno,'column':1},reason='PROFILE_UNCOVERED')
            if depth==0:
                if pos%self.grammar['indentation']['block_spaces']:raise Diagnostic('ARTIFACT_INCOMPATIBLE','Unparenthesized continuation is outside this profile','rule.uncovered.continuation',{'line':lineno,'column':1},reason='PROFILE_UNCOVERED')
                if pos>indent[-1]:indent.append(pos);tokens.append(Token('INDENT','',lineno,1,pos))
                while pos<indent[-1]:indent.pop();tokens.append(Token('DEDENT','',lineno,1,pos))
                if pos!=indent[-1]:invalid('Inconsistent indentation',span={'line':lineno,'column':1})
            at=pos
            while at<len(line):
                if line.startswith('//',at):break
                found=matcher.match(line,at)
                if not found:invalid('Unrecognized token '+line[at:at+8],span={'line':lineno,'column':at+1})
                kind,text=found.lastgroup,found.group();start=at;at=found.end()
                if kind=='SPACE':continue
                if text in ('(', '['):depth+=1
                if text in (')', ']'):
                    depth-=1
                    if depth<0:invalid('Unmatched closing bracket',span={'line':lineno,'column':start+1})
                tokens.append(Token(kind,text,lineno,start+1,at+1))
            if depth==0:tokens.append(Token('NEWLINE','',lineno,len(line)+1,len(line)+1))
        if depth:invalid('Unclosed bracket',span={'line':len(source.splitlines()),'column':1})
        if version is None:invalid('Explicit version directive required by the pinned profile')
        while len(indent)>1:indent.pop();tokens.append(Token('DEDENT','',len(source.splitlines())+1,1,1))
        tokens.append(Token('EOF','',len(source.splitlines())+1,1,1))
        return tokens,version

    @property
    def token(self):return self.tokens[self.i]

    def node(self,kind,token=None,**fields):
        token=token or self.token;self.serial+=1
        return {'kind':kind,'node_id':'node.'+str(self.serial),'span':{'line':token.line,'column':token.column,'end_column':token.end},**fields}

    def take(self,text=None,kind=None):
        t=self.token
        if text is not None and t.text!=text:invalid('Expected '+text+', got '+(t.text or t.kind),span=self.span())
        if kind is not None and t.kind!=kind:invalid('Expected '+kind+', got '+t.kind,span=self.span())
        self.i+=1;return t

    def span(self):return {'line':self.token.line,'column':self.token.column,'end_column':self.token.end}

    def parse(self):
        if self.version!=6:
            raise Diagnostic('ARTIFACT_INCOMPATIBLE','This profile only formalizes Pine v6','rule.profile',self.span(),reason='PROFILE_UNCOVERED')
        statements=[]
        while self.token.kind!='EOF':statements.append(self.statement())
        return self.node('program',self.tokens[0],language_version=self.version,statements=statements)

    def block(self):
        self.take(kind='NEWLINE');self.take(kind='INDENT');statements=[]
        while self.token.kind not in ('DEDENT','EOF'):statements.append(self.statement())
        self.take(kind='DEDENT');return statements

    def statement(self):
        token=self.token
        if token.text in self.grammar['uncovered_keywords'] or token.text=='strategy' or token.text.startswith('strategy.'):
            raise Diagnostic('ARTIFACT_INCOMPATIBLE','Known construct outside the declared slice','rule.uncovered.'+token.text.split('.')[0],self.span(),reason='PROFILE_UNCOVERED')
        if token.text=='if':
            self.take();condition=self.expression();body=self.block();otherwise=[]
            if self.token.text=='else':self.take();otherwise=self.block()
            return self.node('if',token,condition=condition,body=body,otherwise=otherwise)
        if token.text=='once':
            self.take();condition=None if self.token.kind=='NEWLINE' else self.expression()
            return self.node('once',token,condition=condition,body=self.block())
        mode='normal';annotation=None
        if self.token.text in ('var','varip'):mode=self.take().text
        if self.token.text in ('int','float','bool','string') and self.tokens[self.i+1].kind=='NAME':annotation=self.take().text
        if self.token.text=='[':
            saved=self.i;names=[]
            try:
                self.take('[');names.append(self.take(kind='NAME').text)
                while self.token.text==',':self.take(',');names.append(self.take(kind='NAME').text)
                self.take(']');self.take('=')
            except Diagnostic:self.i=saved
            else:
                value=self.expression();self.take(kind='NEWLINE')
                return self.node('tuple_declaration',token,names=names,value=value,mode=mode)
        if self.token.kind=='NAME' and self.tokens[self.i+1].text in ('=',':='):
            name=self.take().text;operator=self.take().text;value=self.expression();self.take(kind='NEWLINE')
            if not re.fullmatch(r'[A-Za-z_][A-Za-z_0-9]*',name):invalid('A variable identifier cannot contain a dot','rule.grammar',{'line':token.line,'column':token.column})
            if operator==':=' and (annotation or mode!='normal'):invalid('Reassignment cannot declare a type or mode','rule.grammar',{'line':token.line,'column':token.column})
            return self.node('declaration' if operator=='=' else 'reassignment',token,name=name,value=value,mode=mode,annotation=annotation)
        if mode!='normal' or annotation:invalid('Declaration expected',span=self.span())
        expression=self.expression();self.take(kind='NEWLINE');return self.node('expression_statement',token,expression=expression)

    def expression(self,minimum=0):
        token=self.take()
        if token.kind=='NUMBER':
            value=float(token.text) if any(c in token.text.lower() for c in '.e') else int(token.text)
            left=self.node('literal',token,value=value,type='float' if isinstance(value,float) else 'int')
        elif token.kind=='STRING':
            try:value=ast.literal_eval(token.text)
            except (SyntaxError,ValueError):invalid('Invalid string literal',span={'line':token.line,'column':token.column})
            left=self.node('literal',token,value=value,type='string')
        elif token.text in ('true','false','na'):left=self.node('literal',token,value={'true':True,'false':False,'na':None}[token.text],type='na' if token.text=='na' else 'bool')
        elif token.text in self.grammar['unary']:left=self.node('unary',token,operator=token.text,operand=self.expression(70))
        elif token.text=='(':
            left=self.expression();self.take(')')
        elif token.text=='[':
            members=[]
            if self.token.text!=']':
                members.append(self.expression())
                while self.token.text==',':self.take(',');members.append(self.expression())
            self.take(']');left=self.node('tuple',token,members=members)
        elif token.kind=='NAME':left=self.node('name',token,name=token.text)
        else:invalid('Expected an expression',span={'line':token.line,'column':token.column})
        while True:
            if self.token.text=='(':
                if left['kind']!='name':invalid('Callable name required',span=self.span())
                self.take('(');arguments=[]
                if self.token.text!=')':
                    while True:
                        name=None
                        if self.token.kind=='NAME' and self.tokens[self.i+1].text=='=':name=self.take().text;self.take('=')
                        arguments.append({'name':name,'expression':self.expression()})
                        if self.token.text!=',':break
                        self.take(',')
                self.take(')');left=self.node('call',token,name=left['name'],arguments=arguments);continue
            if self.token.text=='[':
                self.take('[');offset=self.expression();self.take(']');left=self.node('history',token,expression=left,offset=offset);continue
            precedence=self.precedence.get(self.token.text,-1)
            if precedence<minimum:break
            op=self.take();right=self.expression(precedence+1)
            left=self.node('binary',op,operator=op.text,left=left,right=right)
        if minimum==0 and self.token.text=='?':
            self.take('?');yes=self.expression();self.take(':');no=self.expression()
            left=self.node('conditional',token,condition=left,yes=yes,no=no)
        return left


def parse(source,grammar):return Parser(source,grammar).parse()
