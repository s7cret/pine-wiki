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
 // Expand only complete, single-word aliases. These few noun patterns cover
 // common concept names without altering stemming of descriptions/API names.
 // This is deliberately not a general Russian morphological analyser.
 function nounForms(alias){
  if(!/^[а-я]{4,}$/.test(alias))return [];
  if(alias.endsWith('ия')){
   const base=alias.slice(0,-1);
   return ['я','и','ю','й','ям','ями','ях'].map(ending=>base+ending);
  }
  if(alias.endsWith('а')&&alias.length>=5){
   const base=alias.slice(0,-1),plural=/[гкхжчшщ]$/.test(base)?'и':'ы';
   const forms=['а',plural,'е','у','ам','ами','ах'].map(ending=>base+ending);
   // A consonant cluster before -ка admits the fleeting vowel: метка→меток.
   forms.push(/[бвгджзклмнпрстфхцчшщ]ка$/.test(alias)?base.slice(0,-1)+'ок':base);
   return forms;
  }
  if(/[бвгджзклмнпрстфхцчшщ]$/.test(alias)){
   const plural=/[гкхжчшщ]$/.test(alias)?'и':'ы';
   return ['а','у','е',plural,'ов','ам','ами','ах'].map(ending=>alias+ending);
  }
  return [];
 }
 const weights={names:230,aliases:190,title:145,search:80,body:23,context:12,extra:3};
 let previousQuery=Symbol('unset'),prepared;
 function prepare(query){
  if(query!==previousQuery){const q=normalize(query);prepared={q,qt:words(q),short:q.length<=3};previousQuery=query;}
  return prepared;
 }
 function index(c){
  const tr=r=>typeof r==='object'?[r?.ru,r?.en].join(' '):[c.texts[r]?.ru,c.texts[r]?.en].join(' ');
  return new Map(c.entries.map(e=>{
   const name=normalize(e.name),names=[name,...e.family.names.map(normalize)],aliases=(e.synonyms||[]).map(normalize);
   const title=tr(e.title),search=(e.search_terms||[]).map(normalize);
   const purpose=(e.purposes||[e.purpose]).map(p=>tr(p.domain)+' '+tr(p.topic)).join(' ');
   const params=e.parameters.map(p=>p.name+' '+tr(p.description)).join(' ');
   const f={names:words(names.join(' ')),aliases:words(aliases.join(' ')),title:words(title),search:words(search.join(' ')),body:words(tr(e.description)),context:words(purpose),extra:words([...e.syntax,params].join(' '))};
   return [e.id,{name,names,aliases,inflections:new Set(aliases.flatMap(nounForms)),search,title:normalize(title),namespace:normalize(e.namespace),f,all:[...new Set(Object.values(f).flat())],rank:Number(e.search_rank||0),core:['functions','types','keywords'].includes(e.category)}];
  }));
 }
 function score(z,query){
  const {q,qt,short}=prepare(query);
  if(!q)return 0;
  const exactAlias=z.aliases.includes(q),inflectedAlias=z.inflections.has(q);
  if(!qt.length||(!exactAlias&&!inflectedAlias&&!qt.every(w=>matches(z.all,w))))return -1;
  const last=z.name.split('.').pop();
  let s=z.name===q?11000:z.names.includes(q)?9500:last===q?8500:exactAlias?5500:inflectedAlias?5200:z.title===q?4500:z.search.includes(q)?1800:
        z.names.some(n=>n.startsWith(q))?900:z.aliases.some(a=>a.startsWith(q))?500:0;
  // Exact aliases for declarations and core types outrank incidental mentions
  // on values or members, without special-casing any particular query.
  if(z.core&&(exactAlias||inflectedAlias))s+=120;
  for(const w of qt)for(const [f,weight] of Object.entries(weights))if(matches(z.f[f],w))s+=short&&['body','extra'].includes(f)?weight/12:weight;
  // Editorial preference is allowed only when the query matches an entry's
  // own aliases. It must never beat exact function-name matches.
  if(exactAlias||inflectedAlias||qt.every(w=>matches(z.f.aliases,w)))s+=Math.min(z.rank,350);
  return s;
 }
 root.PINE_SEARCH={index,score,normalize,tokens,stem};
})(typeof window==='object'?window:globalThis);
