import {validateDraft,publishDraft,parseFixtures,mergeRecords} from './workflow.mjs';
const config=JSON.parse(document.querySelector('#demo-config').textContent);
const storageKey='is373-preview-'+config.slug;
const get=id=>document.getElementById(id);
let queue=[];
try {const saved=JSON.parse(localStorage.getItem(storageKey)||'[]');if(Array.isArray(saved))queue=saved;} catch {}
const node=(tag,text,cls)=>{const el=document.createElement(tag);if(text!==undefined)el.textContent=text;if(cls)el.className=cls;return el;};
function announce(message,error=false){get('notice').textContent=message;get('notice').className=error?'notice error':'notice';}
function save(){try{localStorage.setItem(storageKey,JSON.stringify(queue));}catch{announce('Browser storage is unavailable. This page can only keep the current session.',true);}}
function render(){
  const list=get('queue');list.replaceChildren();get('count').textContent=String(queue.length);
  if(!queue.length){list.append(node('p','No saved items yet. Try the task on this page.','empty'));return;}
  for(const record of queue){
    const card=node('article',undefined,'item');card.append(node('span',record.status,'badge'),node('h3',record.title),node('p',record.body||'No summary supplied.'));
    if(config.kind==='etl'){
      card.append(node('p',`Category: ${record.category} · Source: ${record.source} (${record.sourceId})`,'meta'),node('code',record.url,'source'));
      if(record.status==='Needs human review'){
        const approve=node('button','Mark reviewed in preview','secondary');approve.type='button';approve.addEventListener('click',()=>{queue=queue.map(r=>r.key===record.key?{...r,status:'Reviewed in preview'}:r);save();render();announce('Marked reviewed in this browser. Nothing was published or sent.');});card.append(approve);
      }
    }else{
      card.append(node('p','Synthetic item · saved only in this browser','meta'));
      if(get('role').value==='admin'&&record.status==='Pending review'){
        const publish=node('button','Publish in preview');publish.type='button';publish.addEventListener('click',()=>{try{const updated=publishDraft(record,get('role').value);queue=queue.map(r=>r.id===record.id?updated:r);save();render();announce('Published in the preview only. The real app still needs server-enforced permissions.');}catch(e){announce(e.message,true);}});card.append(publish);
      }
    }
    list.append(card);
  }
}
get('reset').addEventListener('click',()=>{queue=[];save();render();announce('Only this synthetic preview queue was cleared.');});
if(config.kind==='content'){
  get('role').addEventListener('change',()=>{render();announce('Demo role changed. This dropdown is not authentication or secure authorization.');});
  get('main-form').addEventListener('submit',event=>{
    event.preventDefault();const checked=validateDraft({title:get('title').value,body:get('body').value});
    if(!checked.ok){announce(checked.error,true);return;}
    queue.push({id:String(Date.now())+'-'+Math.random().toString(16).slice(2),title:checked.title,body:checked.body,status:'Pending review'});save();render();get('main-form').reset();announce('Draft saved: Pending review. Switch to the simulated admin to review it.');
  });
}else{
  get('fixtures').value=JSON.stringify(config.fixtures,null,2);
  get('main-form').addEventListener('submit',event=>{
    event.preventDefault();const parsed=parseFixtures(get('fixtures').value);if(!parsed.ok){announce(parsed.error,true);return;}
    const result=mergeRecords(queue,parsed.records);queue=result.queue;save();render();
    get('added').textContent=String(result.added);get('skipped').textContent=String(parsed.duplicates+result.skipped);get('rejected').textContent=String(parsed.rejected.length);
    get('problems').replaceChildren(...parsed.rejected.map(text=>node('li',text)));
    announce(`Import complete: ${result.added} added; ${parsed.duplicates+result.skipped} duplicates/already saved skipped; ${parsed.rejected.length} rejected. Every new item still needs human review.`);
  });
}
render();
