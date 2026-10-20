'use strict';
const assert=require('node:assert/strict');
require('../wiki-examples.js');
const api=globalThis.PINE_EXAMPLES;
const item={code_sha256:'a'.repeat(64),language_version:6,probe_definition_hash:'b'.repeat(64),validation_context_hash:'c'.repeat(64)};
const run={code_sha256:item.code_sha256,language_version:6,definition_hash:item.probe_definition_hash,context_hash:item.validation_context_hash,date:'2026-10-20',data:{symbol:'fixture'},parameters:{},environment:{implementation:'fixture'},artifact:'spec/run-artifacts/test.json'};
let checks=0;
for(const compilation of ['not_compiled','compiled','error','blocked','unknown']){
 for(const execution of ['not_executed','executed','error','blocked','unknown']){
  const x=api.presentation({...item,compilation_status:compilation,execution_status:execution,validation_run:run});
  assert.equal(x.compilation,compilation);assert.equal(x.execution,execution);checks++;
 }
}
assert.equal(api.presentation({...item,compilation_status:'compiled',execution_status:'executed'}).execution,'stale');checks++;
for(const key of ['code_sha256','definition_hash','context_hash','language_version']){
 assert.equal(api.applies(item,{...run,[key]:'changed'}),false,key);checks++;
}
assert.equal(api.presentation({...item,compilation_status:'future',execution_status:'future'}).execution,'unknown');checks++;
const fs=require('node:fs');const text=fs.readFileSync(require('node:path').join(__dirname,'../wiki-i18n.js'),'utf8');
const ui=JSON.parse(text.split('window.PINE_UI=')[1].trim().replace(/;$/,''));
for(const key of ['notCompiled','compiledStatus','notExecutedStatus','executedStatus','exampleError','exampleBlocked','exampleUnknown','exampleStale','runRecord']){
 assert.equal(ui[key].length,2,key);assert(ui[key].every(x=>typeof x==='string'&&x.length));checks++;
}
console.log(`${checks} example-status cases passed (negative/success/error/blocked/unknown/stale, RU/EN)`);
