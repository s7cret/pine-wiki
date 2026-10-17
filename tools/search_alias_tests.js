'use strict';

// Exercise public index()/score() behavior with small, deliberately ambiguous
// fixtures. Catalog gold cases alone cannot reveal accidental broad matching.
module.exports=function aliasGuards(search){
 const results=[];
 const entry=(name,aliases=[],body='',category='types')=>({
  id:name,name,namespace:'',category,family:{names:[]},synonyms:aliases,
  title:{ru:name,en:name},description:{ru:body,en:''},syntax:[],parameters:[],
  purposes:[{domain:{ru:'',en:''},topic:{ru:'',en:''}}]
 });
 const concepts=[
  ['line','линия',['лин','линейный','линейка']],
  ['label','метка',['мет','меткость','металл','метoк']],
  ['map','карта',['кар','картина','карман']],
  ['box','бокс',['бок','боксер','боковой']],
  ['array','массив',['мас','массивный']],
  ['table','таблица',['таб','табличный']]
 ];
 const entries=concepts.map(([name,alias])=>entry(name,[alias]));
 entries.push(entry('body-only',[],'линия метка'),entry('phrase-only',['линия тренда']),
  entry('literal-alias',['линии'],'','variables'),entry('title-match'),
  entry('ta.sma'),entry('size.small'),entry('short-alias',['год']));
 entries.find(e=>e.name==='title-match').title={ru:'массивы',en:''};
 const index=search.index({entries,texts:{}}),score=(name,query)=>search.score(index.get(name),query);
 const check=(name,passed)=>results.push({name,passed});
 for(const [name,,unrelated] of concepts){
  check(`${name}: no short-prefix or unrelated-word match`,unrelated.every(query=>score(name,query)<0));
 }
 check('body text is not given alias inflections',score('body-only','линий')<0&&score('body-only','меток')<0);
 check('a word inside a phrase is not a whole alias',score('phrase-only','линий')<0);
 check('three-letter Russian aliases are not expanded',score('short-alias','годы')<0);
 check('case and outer whitespace normalize before alias matching',score('line','  ЛИНИЙ  ')===score('line','линий'));
 check('explicit alias outranks a generated inflection',score('literal-alias','линии')>score('line','линии'));
 check('concept alias inflection outranks an incidental title match',score('array','массивы')>score('title-match','массивы'));
 check('exact API name outranks its Russian alias forms',score('line','line')>score('line','линий'));
 check('short API names keep token boundaries',score('ta.sma','sma')>=0&&score('size.small','sma')<0);
 check('empty search still matches all entries',score('line','')===0&&score('line',undefined)===0);
 return results;
};
