(function(root){
 'use strict';
 const compileStates=new Set(['not_compiled','compiled','error','expected_error','blocked','unknown']);
 const executeStates=new Set(['not_executed','executed','error','blocked','unknown']);
 function applies(item,run){
  if(run){const c=run.compiler?.status,r=run.runtime?.status;if((r==='executed'||r==='error')&&c!=='compiled')return false;if(run.comparison?.passed===true&&c&&(c!=='compiled'||r!=='executed'))return false;}
  return !!(run&&run.code_sha256===item.code_sha256&&run.language_version===(item.language_version||item.version_directive)&&
   run.definition_hash&&run.definition_hash===item.probe_definition_hash&&(!item.validation_context_hash||run.context_hash===item.validation_context_hash)&&run.date&&run.data&&run.parameters&&run.environment&&run.artifact);
 }
 function presentation(item){
  let compilation=compileStates.has(item.compilation_status)?item.compilation_status:'unknown';
  let execution=executeStates.has(item.execution_status)?item.execution_status:'unknown';
  const bound=applies(item,item.validation_run);
  if(compilation==='compiled'&&!bound)compilation='stale';
  if(execution==='executed'&&!bound)execution='stale';
  return {compilation,execution,run:bound?item.validation_run:null};
 }
 root.PINE_EXAMPLES={applies,presentation};
})(typeof window==='object'?window:globalThis);
