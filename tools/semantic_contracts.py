"""Small, explicit normalization rules; raw source text is never rewritten."""
import re
from decimal import Decimal

PLACEHOLDER_REFS = frozenset({'a37534c04dab7f30', '180bedf878ee24aa', 'd16318992318f93e'})
NUMBER = r'[+-]?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?'


def canonical_number(spelling):
    if not re.fullmatch(NUMBER, spelling):
        raise ValueError('Not a prose numeric literal: ' + spelling)
    return format(Decimal(spelling.replace(',', '')), 'f')


def default_number(text):
    match = re.search(r'\b(?:The )?[Dd]efault (?:is|value is)\s+(' + NUMBER + r')(?!\d|,\d)', text)
    return None if not match else {'value': canonical_number(match[1]), 'source_spelling': match[1], 'quote': match[0]}


def meaningful_text(item):
    if not isinstance(item, dict) or item.get('content_status') == 'missing_description_notice':
        return False
    return any(str(item.get(k) or '').strip() for k in ('ru', 'en', 'original'))


def explicit_optional(text):
    # An independent sentence in this parameter's own description. Do not
    # infer optionality from defaults or mentions of other optional arguments.
    return bool(re.search(r'(?:^|[.!?]\s+)Optional\.(?:\s|$)', text))


def contract_errors(contract, texts):
    values = set(contract.get('values', []))
    evidence = contract.get('evidence', [])
    if values != {e.get('value') for e in evidence}:
        yield 'DEFAULT_EVIDENCE: normalized values differ from evidence'
    for e in evidence:
        raw = texts.get(e.get('text_ref'), {}).get('en', '')
        quote, value = e.get('quote', ''), e.get('value', '')
        if quote not in raw:
            yield 'DEFAULT_EVIDENCE: quote is absent from its source text'
        numeric = default_number(raw)
        if re.fullmatch(NUMBER, value) and numeric and value != numeric['value']:
            yield 'DEFAULT_EVIDENCE: numeric literal was truncated or changed'
        literal = e.get('source_spelling', value)
        if not isinstance(literal, str) or not isinstance(value, str):
            yield 'DEFAULT_EVIDENCE: spelling and value must be strings'
            continue
        if re.fullmatch(NUMBER, literal) and re.fullmatch(NUMBER, value):
            equivalent = Decimal(literal.replace(',', '')) == Decimal(value.replace(',', ''))
        else:
            equivalent = literal == value
        if not equivalent:
            yield 'DEFAULT_EVIDENCE: source spelling and normalized value are not equivalent'
        if not re.search(r'(?<![\w.])' + re.escape(literal) + r'(?![\w.])', quote):
            yield 'DEFAULT_EVIDENCE: value is absent from quoted evidence'


def history_contracts(entries):
    result = {}
    for entry in entries:
        for p in entry['parameters']:
            dc = p.get('default_contract', {})
            out = result.setdefault(p['name'], {'values': [], 'states': [], 'evidence': []})
            for key, vals in [('values', dc.get('values', [])), ('states', [dc.get('state', 'not_documented')]), ('evidence', dc.get('evidence', []))]:
                for val in vals:
                    if val not in out[key]:
                        out[key].append(val)
    return result
