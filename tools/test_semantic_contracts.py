"""Regression checks for source normalization, availability and comparison."""
import json, subprocess, unittest
from pathlib import Path
from semantic_contracts import default_number, explicit_optional, meaningful_text

ROOT=Path(__file__).resolve().parents[1]


class NormalizationTests(unittest.TestCase):
    def test_numbers_and_punctuation(self):
        for raw,expected in [('100,000, which is the limit.','100000'),('12.5.','12.5'),('42, optional.','42'),('-0.5; next.','-0.5')]:
            self.assertEqual(default_number('The default is '+raw)['value'],expected)
        self.assertIsNone(default_number('fn(100, 000)'))

    def test_optional_scope(self):
        self.assertTrue(explicit_optional('Timezone. Optional. Uses exchange time.'))
        self.assertFalse(explicit_optional('Controls another Optional. argument.'))
        self.assertFalse(explicit_optional('The optional color argument controls it.'))

    def test_placeholders_do_not_improve_coverage(self):
        self.assertFalse(meaningful_text({'en':'No source description.', 'content_status':'missing_description_notice'}))
        self.assertFalse(meaningful_text({'en':''}))
        self.assertTrue(meaningful_text({'en':'Price series used in the calculation.'}))

    def test_snapshot_normalization(self):
        for v in range(1,7):
            c=json.loads((ROOT/f'catalog-v{v}.js').read_text(encoding='utf8').split(f'window.PINE_CATALOG[{v}]=')[1].rstrip(';\n'))
            if v in (1,2):
                placeholders=sum(c['texts'].get(p.get('description'),{}).get('content_status')=='missing_description_notice' for e in c['entries'] for p in e['parameters'])
                self.assertEqual(placeholders,{1:62,2:75}[v])
            if v in (5,6):
                e=next(e for e in c['entries'] if e['name']=='request.security')
                p=next(p for p in e['parameters'] if p['name']=='lookahead')
                self.assertEqual(p['default_contract']['values'],['barmerge.lookahead_off'])
                self.assertEqual(p['default_contract']['historical_semantics'][0]['versions'],[1,2])

    def test_compare_uses_source_content_not_translations(self):
        script="""require('./wiki-compare.js'); const C=globalThis.PINE_COMPARE;
const a={description_hashes:['raw'],description_content_status:'missing_description_notice'};
const b={...a,description_supplements:[{description:'manual'}]};
if(C.description(a,b)!=='missing')process.exit(1);
const c={description_hashes:['real'],translation:'ru'};
if(C.description(c,{...c,translation:'en'})!=='same')process.exit(2);
if(C.description(c,{description_hashes:['different']})!=='changed')process.exit(3);
"""
        subprocess.run(['node','-e',script],cwd=ROOT,check=True)


if __name__=='__main__':unittest.main()
