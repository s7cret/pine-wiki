/* Field-aware bilingual ranking for the archived Pine Script reference.
 * Avoids matching 3-letter API names ("sma") against unrelated prefixes ("small").
 * Search priorities are data-driven rather than special-cased query strings.
 */
(function(root){
 'use strict';
 const normalize=s=>String(s??'').normalize('NFKC').toLowerCase().replace(/ё/g,'е').trim();
 const tokens=s=>normalize(s).match(/[\p{L}\p{N}_]+/gu)||[];
 const stem=s=>/[а-я]/.test(s)&&s.length>5?s.replace(/(иями|ями|ами|ого|ему|ыми|ими|ий|ый|ой|ая|яя|ое|ее|ые|ие|ую|юю|ом|ем|ах|ях|ов|ев|ам|ям|ы|и|а|я|у|ю|е)$/,''):s;
 const words=s=>[...new Set(tokens(s).map(stem))];
 const matches=(field,w)=>field.some(t=>t===w||(w.length>=4&&t.startsWith(w)));
 function index(c){
  const tr=r=>typeof r==='object'?[r?.ru,r?.en].join(' '):[c.texts[r]?.ru,c.texts[r]?.en].join(' ');
  return new Map(c.entries.map(e=>{
   const name=normalize(e.name),names=[name,...e.family.names.map(normalize)],aliases=(e.synonyms||[]).map(normalize);
   const title=tr(e.title),search=(e.search_terms||[]).map(normalize);
   const purpose=(e.purposes||[e.purpose]).map(p=>tr(p.domain)+' '+tr(p.topic)).join(' ');
   const params=e.parameters.map(p=>p.name+' '+tr(p.description)).join(' ');
   const f={names:words(names.join(' ')),aliases:words(aliases.join(' ')),title:words(title),search:words(search.join(' ')),body:words(tr(e.description)),context:words(purpose),extra:words([...e.syntax,params].join(' '))};
   return [e.id,{name,names,aliases,search,title:normalize(title),namespace:normalize(e.namespace),f,all:[...new Set(Object.values(f).flat())],rank:Number(e.search_rank||0)}];
  }));
 }
 function score(z,query){
  const q=normalize(query),qt=words(q);
  if(!q)return 0;
  if(!qt.length||!qt.every(w=>matches(z.all,w)))return -1;
  const last=z.name.split('.').pop();
  let s=z.name===q?11000:z.names.includes(q)?9500:last===q?8500:z.aliases.includes(q)?5500:z.title===q?4500:z.search.includes(q)?1800:
        z.names.some(n=>n.startsWith(q))?900:z.aliases.some(a=>a.startsWith(q))?500:0;
  const weights={names:230,aliases:190,title:145,search:80,body:23,context:12,extra:3};
  for(const w of qt)for(const [f,weight] of Object.entries(weights))if(matches(z.f[f],w))s+=weight;
  // Editorial preference is allowed only when the query matches an entry's
  // own aliases. It must never beat exact function-name matches.
  if(qt.every(w=>matches(z.f.aliases,w)))s+=Math.min(z.rank,350);
  return s;
 }
 root.PINE_SEARCH={index,score,normalize,tokens,stem};
})(typeof window==='object'?window:globalThis);
