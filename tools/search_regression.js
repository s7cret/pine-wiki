#!/usr/bin/env node
'use strict';
// Run the same ranking and tie-breakers as the browser, without browser packages.
const fs=require('node:fs'),path=require('node:path'),vm=require('node:vm');
const {performance}=require('node:perf_hooks');
const root=path.resolve(__dirname,'..');
const gold=JSON.parse(fs.readFileSync(path.join(__dirname,'search_gold.json'),'utf8'));
const context={window:{PINE_CATALOG:{}}};
vm.createContext(context);
for(const file of [`catalog-v${gold.version}.js`,'wiki-search.js'])vm.runInContext(fs.readFileSync(path.join(root,file),'utf8'),context,{filename:file});
const cat=context.window.PINE_CATALOG[gold.version],search=context.window.PINE_SEARCH,index=search.index(cat);
function ranked(query){
 return cat.entries.filter(e=>!e.technical).map(entry=>({entry,score:search.score(index.get(entry.id),query)})).filter(x=>x.score>=0)
  .sort((a,b)=>b.score-a.score||a.entry.namespace.localeCompare(b.entry.namespace)||a.entry.name.localeCompare(b.entry.name)||a.entry.id.localeCompare(b.entry.id)).map(x=>x.entry);
}
let failed=0;
for(const test of gold.cases){
 const found=ranked(test.query),position=found.findIndex(e=>test.expected.includes(e.name)&&(!test.category||e.category===test.category))+1;
 const excluded=found.filter(e=>(test.exclude||[]).includes(e.name));
 const pass=position>0&&position<=gold.max_rank&&!excluded.length;
 if(!pass)failed++;
 console.log(`${pass?'PASS':'FAIL'} ${test.query.padEnd(28)} rank=${String(position||'missing').padEnd(7)} top=${found.slice(0,3).map(e=>e.name).join(', ')}${excluded.length?' excluded='+excluded.map(e=>e.name).join(', '):''}`);
}
const guards=require('./search_alias_tests.js')(search);
for(const guard of guards)console.log(`${guard.passed?'PASS':'FAIL'} guard: ${guard.name}`);
const guardFailures=guards.filter(guard=>!guard.passed).length;
// Warm up before timing; sorting and indexing are deliberately excluded.
const samples=[];
for(let repeat=0;repeat<18;repeat++){
 const query=gold.cases[repeat%gold.cases.length].query,start=performance.now();
 for(const entry of cat.entries)search.score(index.get(entry.id),query);
 if(repeat>=6)samples.push(performance.now()-start);
}
samples.sort((a,b)=>a-b);
console.log(`score: median ${samples[Math.floor(samples.length/2)].toFixed(2)} ms for ${cat.entries.length} cards (informational; hardware-dependent)`);
console.log(`${gold.cases.length-failed}/${gold.cases.length} search regression cases passed`);
console.log(`${guards.length-guardFailures}/${guards.length} alias matching guards passed`);
process.exitCode=failed||guardFailures?1:0;
