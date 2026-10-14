/* Paws Answered: pet filter on the home cards + live search with suggestions (index: /search.json, built by seo_site.py). */
(function(){
var pet="all";
document.querySelectorAll(".switch button").forEach(function(b){b.onclick=function(){
  document.querySelectorAll(".switch button").forEach(function(x){x.classList.remove("on")});b.classList.add("on");pet=b.dataset.pet;
  var n=0;document.querySelectorAll("#qlist .qcard").forEach(function(c){var ok=pet=="all"||c.dataset.pet==pet;c.hidden=!ok;if(ok)n++});
  var e=document.getElementById("empty");if(e)e.hidden=n>0;}});

var me=document.currentScript&&document.currentScript.src||"";var ROOT=me.replace(/assets\/app\.js.*$/,"");
var STOP={a:1,an:1,the:1,is:1,are:1,my:1,can:1,do:1,does:1,i:1,to:1,of:1,for:1,it:1,and:1,or:1,how:1,what:1,why:1,should:1,eat:0,in:1,on:1,with:1,be:1,safe:0,if:1,much:1,so:1,at:1,me:1,you:1,your:1,will:1,ok:1};
function stem(w){if(w.length>4&&/ies$/.test(w))return w.slice(0,-3)+"y";if(w.length>4&&/(ches|shes|xes|ses)$/.test(w))return w.slice(0,-2);if(w.length>3&&/s$/.test(w)&&!/ss$/.test(w))return w.slice(0,-1);return w}
function toks(s){return (s||"").toLowerCase().replace(/[^a-z0-9 ]+/g," ").split(/\s+/).filter(function(w){return w&&!STOP[w]}).map(stem)}
var IDX=null,loading=null;
function load(){if(IDX)return Promise.resolve(IDX);if(!loading)loading=fetch(ROOT+"search.json").then(function(r){return r.json()}).then(function(d){
  d.items.forEach(function(it){it._t=toks(it.t);it._k=toks(it.k+" "+it.topic+" "+it.pet);it._a=toks(it.a)});IDX=d;return d});return loading}
function hit(q,list){for(var i=0;i<list.length;i++){var w=list[i];if(w==q)return 2;if(w.indexOf(q)==0||(q.length>3&&q.indexOf(w)==0&&w.length>3))return 1}return 0}
function search(q){var qt=toks(q);if(!qt.length||!IDX)return[];var out=[];
  IDX.items.forEach(function(it){var sc=0,all=true;qt.forEach(function(w){var s=hit(w,it._t)*3||hit(w,it._k)*2||hit(w,it._a);if(!s)all=false;sc+=s});
    if(sc>0){if(it.kind=="answer")sc+=0.5;out.push([sc,it,all])}});
  if(out.some(function(x){return x[2]}))out=out.filter(function(x){return x[2]});
  out.sort(function(a,b){return b[0]-a[0]||a[1].t.length-b[1].t.length});return out.slice(0,6).map(function(x){return x[1]})}
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]})}

document.querySelectorAll("form.search").forEach(function(form){
  var inp=form.querySelector("input"),btn=form.querySelector("button");if(!inp)return;
  form.removeAttribute("onsubmit");form.setAttribute("role","search");form.style.position="relative";
  var box=document.createElement("div");box.className="sugg";box.id="sugg-"+Math.random().toString(36).slice(2,7);box.setAttribute("role","listbox");box.hidden=true;form.appendChild(box);
  inp.setAttribute("autocomplete","off");inp.setAttribute("role","combobox");inp.setAttribute("aria-autocomplete","list");inp.setAttribute("aria-controls",box.id);inp.setAttribute("aria-expanded","false");
  var res=[],sel=-1;
  function close(){box.hidden=true;inp.setAttribute("aria-expanded","false");sel=-1}
  function render(){var q=inp.value.trim();if(!q){close();return}res=search(q);sel=-1;
    if(!res.length){box.innerHTML='<div class="sg-none">No answer yet. Browse <a href="'+ROOT+'cats/">cat answers</a> or <a href="'+ROOT+'dogs/">dog answers</a>.</div>'}
    else box.innerHTML=res.map(function(it,i){return '<a class="sg" role="option" id="'+box.id+'-'+i+'" href="'+ROOT+it.u+'"><span class="sg-ic '+(it.pet||"all")+'">'+(IDX.icons[it.pet]||"")+'</span><span class="sg-tx"><b>'+esc(it.t)+'</b><small>'+esc(it.kind=="answer"?(it.a.length>100?it.a.slice(0,100).replace(/\s\S*$/,"")+"…":it.a):(it.kind=="hub"?"All "+it.pet+" answers":"Topic page"))+'</small></span></a>'}).join("");
    box.hidden=false;inp.setAttribute("aria-expanded","true")}
  function mark(){box.querySelectorAll(".sg").forEach(function(a,i){a.classList.toggle("on",i==sel);a.setAttribute("aria-selected",i==sel)});
    if(sel>=0)inp.setAttribute("aria-activedescendant",box.id+"-"+sel);else inp.removeAttribute("aria-activedescendant")}
  inp.addEventListener("focus",function(){load().then(function(){if(inp.value.trim())render()})});
  inp.addEventListener("input",function(){load().then(render)});
  inp.addEventListener("keydown",function(e){if(box.hidden)return;var n=box.querySelectorAll(".sg").length;
    if(e.key=="ArrowDown"){e.preventDefault();sel=(sel+1)%Math.max(n,1);mark()}else if(e.key=="ArrowUp"){e.preventDefault();sel=sel<=0?n-1:sel-1;mark()}else if(e.key=="Escape"){close()}});
  form.addEventListener("submit",function(e){e.preventDefault();load().then(function(){var q=inp.value.trim();if(!q){inp.focus();return}
    var r=search(q),pick=sel>=0?r[sel]:r[0];if(pick){location.href=ROOT+pick.u}else{render()}})});
  document.addEventListener("click",function(e){if(!form.contains(e.target))close()});
});
})();
