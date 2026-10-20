"""Validation runs apply to a precise definition, code and execution context."""
import hashlib,json


def definition_digest(definition):
    value={k:v for k,v in definition.items() if k!='definition_hash'}
    return hashlib.sha256((json.dumps(value,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False)+'\n').encode()).hexdigest()


def validate_definition(definition):
    return (hashlib.sha256(definition['code'].encode()).hexdigest()==definition['code_sha256'] and
            definition_digest(definition)==definition['definition_hash'])

def run_applies(item, run):
    return bool(isinstance(run,dict) and run.get('code_sha256') == item.get('code_sha256') and
                run.get('language_version') == (item.get('language_version') or item.get('version_directive')) and
                run.get('definition_hash') and run.get('definition_hash') == item.get('probe_definition_hash') and
                (not item.get('validation_context_hash') or run.get('context_hash')==item['validation_context_hash']) and
                all(run.get(k) for k in ('date','data','environment','artifact')) and isinstance(run.get('parameters'),dict))
