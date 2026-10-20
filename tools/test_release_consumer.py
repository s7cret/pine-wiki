"""Execute the shipped, externally pinned bundle through the real CLI offline."""
import hashlib,json,os,subprocess,sys,tempfile
from pathlib import Path
from spec_bundle import ROOT,read_json,export_bundle
sys.path.insert(0,str(ROOT))
from consumer.runtime import source_identity


def main():
    lock=read_json(ROOT/'consumer/lock.json');bundle=ROOT/lock['bundle'];manifest=read_json(bundle/'manifest.json')
    assert lock['consumer_source_sha256']==source_identity(),'Consumer differs from pinned implementation'
    assert len(lock['implementation_commit'])==40 and manifest['source_commit']==lock['implementation_commit'],'Implementation SHA must identify the exported source'
    expected=read_json(ROOT/'spec/fixtures/expected.json')['plots']
    bootstrap="import socket,runpy; from unittest.mock import patch; patcher=patch.object(socket,'create_connection',side_effect=RuntimeError('Network disabled')); patcher.start(); runpy.run_module('consumer.cli',run_name='__main__')"
    checks=0
    for program in sorted((ROOT/'spec/programs').glob('*.pine')):
        command=[sys.executable,'-c',bootstrap,'--lock',str(ROOT/'consumer/lock.json'),'--source',str(program),'--context',str(ROOT/'spec/fixtures/context.json')]
        run=subprocess.run(command,cwd=ROOT,capture_output=True,text=True,encoding='utf8');assert run.returncode==0,run.stderr+run.stdout
        result=json.loads(run.stdout);assert result['result']['plots']==expected[program.stem],program.name
        assert result['consumer']['implementation_commit']==lock['implementation_commit'];assert result['context_sha256'];checks+=1
    (ROOT/'.runtime').mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='release-reexport-',dir=ROOT/'.runtime') as tmp:
        output=Path(tmp)/'bundle'
        command=[sys.executable,'tools/spec_bundle.py','--output',str(output.relative_to(ROOT)),'--source-commit',manifest['source_commit'],'--write-lock',str(Path(tmp)/'lock.json')]
        subprocess.run(command,cwd=ROOT,capture_output=True,text=True,encoding='utf8',check=True)
        for path in bundle.iterdir():assert path.read_bytes()==(output/path.name).read_bytes(),'Published bundle differs from canonical source: '+path.name
        checks+=1
    print(f'{checks} release-consumer checks passed: 6 full CLI programs offline; byte-identical re-export; pinned implementation {lock["implementation_commit"]}')


if __name__=='__main__':main()
