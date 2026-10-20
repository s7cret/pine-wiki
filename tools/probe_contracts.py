"""Validation runs apply to a precise definition, code and execution context."""
import hashlib,json


def definition_digest(definition):
    value={k:v for k,v in definition.items() if k!='definition_hash'}
    return hashlib.sha256((json.dumps(value,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False)+'\n').encode()).hexdigest()


def validate_definition(definition):
    return (hashlib.sha256(definition['code'].encode()).hexdigest()==definition['code_sha256'] and
            definition_digest(definition)==definition['definition_hash'])

def run_status_consistent(run,definition=None):
    compiler=run.get('compiler',{}).get('status');runtime=run.get('runtime',{}).get('status')
    if runtime in ('executed','error') and compiler!='compiled':return False
    passed=run.get('comparison',{}).get('passed')
    diagnostic=definition and definition.get('comparator',{}).get('kind')=='diagnostic'
    if compiler=='error' and passed is True:
        return bool(diagnostic and runtime=='not_executed' and run.get('comparison',{}).get('diagnostic')==definition.get('expected'))
    if passed is True and not diagnostic and compiler is not None and (compiler!='compiled' or runtime!='executed'):return False
    if diagnostic and passed is True:
        expected=definition.get('expected',{});phase=expected.get('phase')
        return bool(run.get('comparison',{}).get('diagnostic')==expected and (compiler=='error' and runtime=='not_executed' if phase in ('parse','bind','compile') else compiler=='compiled' and runtime=='error'))
    return True


def run_applies(item, run):
    return bool(isinstance(run,dict) and run_status_consistent(run,item.get('definition')) and run.get('code_sha256') == item.get('code_sha256') and
                run.get('language_version') == (item.get('language_version') or item.get('version_directive')) and
                run.get('definition_hash') and run.get('definition_hash') == item.get('probe_definition_hash') and
                (not item.get('validation_context_hash') or run.get('context_hash')==item['validation_context_hash']) and
                all(run.get(k) for k in ('date','data','environment','artifact')) and isinstance(run.get('parameters'),dict))
