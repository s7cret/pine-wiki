"""python -m consumer.cli --lock consumer/lock.json --source spec/programs/ema.pine ..."""
import argparse,json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
from spec_bundle import load_bundle,read_json
from .errors import Diagnostic
from .frontend import Frontend
from .runtime import Runtime,lower,DEFAULT_OPERATIONS,source_identity,hash_value


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--lock',type=Path,required=True);parser.add_argument('--source',type=Path,required=True);parser.add_argument('--context',type=Path);parser.add_argument('--compile-only',action='store_true');parser.add_argument('--omit-operation');parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    try:
        lock=read_json(args.lock);root=Path(__file__).resolve().parents[1]
        if lock.get('consumer_source_sha256') and lock['consumer_source_sha256']!=source_identity():
            raise Diagnostic('ARTIFACT_INCOMPATIBLE','Consumer source differs from its pinned build')
        bundle=load_bundle(root/lock['bundle'],lock['manifest_sha256'],lock['semantic_profile_id'])
        resolved=Frontend(bundle).compile(args.source.read_text(encoding='utf8'))
        operations=DEFAULT_OPERATIONS-({args.omit_operation} if args.omit_operation else set())
        ir=lower(resolved,operations)
        if args.compile_only:result={'resolved_program':resolved,'artifact':ir}
        elif not args.context:raise Diagnostic('CONTEXT_UNAVAILABLE','--context is required to execute')
        else:result={'resolved_program':resolved,'artifact':ir,'result':Runtime(bundle,operations).run(ir,read_json(args.context))}
        result['consumer']={'implementation_commit':lock.get('implementation_commit'),'source_sha256':source_identity()}
        if args.context:result['context_sha256']=hash_value(read_json(args.context))
        code=0
    except Diagnostic as error:result={'diagnostic':error.data};code=2
    except (ValueError,FileNotFoundError,KeyError) as error:result={'diagnostic':{'category':'ARTIFACT_INCOMPATIBLE','message':str(error)}};code=2
    text=json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False)+'\n'
    if args.output:args.output.write_text(text,encoding='utf8',newline='\n')
    else:print(text,end='')
    return code


if __name__=='__main__':raise SystemExit(main())
