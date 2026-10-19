(function(root){
 'use strict';
 const sorted=x=>[...new Set(x||[])].sort();
 const same=(a,b)=>JSON.stringify(sorted(a))===JSON.stringify(sorted(b));
 function required(a,b){
  a=sorted(a?.length?a:['unknown']);b=sorted(b?.length?b:['unknown']);
  if(same(a,b))return 'same';
  if(a.includes('conflict')||b.includes('conflict')||a.filter(x=>x!=='unknown').length>1||b.filter(x=>x!=='unknown').length>1)return 'conflict';
  const au=a.every(x=>x==='unknown'),bu=b.every(x=>x==='unknown');
  if(au&&!bu)return 'clarified';
  if(!au&&bu)return 'less_documented';
  if(a.includes('unknown')||b.includes('unknown'))return 'coverage';
  return 'source_difference';
 }
 function defaults(a,b,oldText,newText){
  const av=sorted(a?.values),bv=sorted(b?.values);
  if(av.length&&bv.length)return same(av,bv)?'same':'source_difference';
  if(!av.length&&bv.length)return 'clarified';
  if(av.length&&!bv.length)return 'less_documented';
  return same(oldText,newText)?'same':'wording';
 }
 function description(a,b){
  if(a?.description_content_status==='missing_description_notice'||b?.description_content_status==='missing_description_notice')return 'missing';
  return same(a?.description_hashes,b?.description_hashes)?'same':'changed';
 }
 root.PINE_COMPARE={required,defaults,description};
})(typeof window==='object'?window:globalThis);
