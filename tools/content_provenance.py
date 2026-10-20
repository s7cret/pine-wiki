"""Content attribution is independent of the method used to translate it."""
import hashlib
from semantic_contracts import meaningful_text


def classify_content(item):
    if not meaningful_text(item):
        return 'missing'
    attribution = item.get('content_provenance', {})
    if attribution.get('kind') in ('primary_source','editorial'):
        return attribution['kind']
    if item.get('original_kind') == 'editorial_english_summary' or item.get('basis') == 'editorial_summary':
        return 'editorial'
    provenance = item.get('translation_provenance', {})
    # Exact primary EN attribution is evidence of content origin. A label
    # describing translation style alone is deliberately insufficient.
    original = item.get('original', '')
    if (provenance.get('status') == 'verified_official' and original and
        provenance.get('original_sha256') == hashlib.sha256(original.encode()).hexdigest() and
        any(s.get('language') == 'en' and s.get('sha256') for s in provenance.get('sources', []))):
        return 'primary_source'
    return 'unknown'
