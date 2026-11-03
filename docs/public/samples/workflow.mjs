// Shared preview behavior. This browser code is not an authorization boundary.
export function validateDraft(input) {
  const title=String(input.title??'').trim(), body=String(input.body??'').trim();
  if(!title||!body) return {ok:false,error:'Add a title and a short message before saving.'};
  if(title.length>80) return {ok:false,error:'Keep the title to 80 characters.'};
  if(body.length>500) return {ok:false,error:'Keep the message to 500 characters.'};
  return {ok:true,title,body};
}
export function publishDraft(record,role) {
  if(role!=='admin') throw new Error('Only the simulated admin can publish in this preview.');
  if(record.status!=='Pending review') throw new Error('This item is already published in the preview.');
  return {...record,status:'Published in preview'};
}
export function parseFixtures(raw) {
  let input;
  try {input=JSON.parse(raw)} catch {return {ok:false,error:'The fixture must be valid JSON. Existing saved items were kept.'};}
  if(!Array.isArray(input)) return {ok:false,error:'Use a JSON array of fixture records. Existing saved items were kept.'};
  const records=[],rejected=[],seen=new Set();let duplicates=0;
  input.forEach((item,index)=>{
    if(!item||typeof item!=='object'||Array.isArray(item)) {rejected.push(`Row ${index+1}: expected an object.`);return;}
    const title=String(item.title??'').trim().replace(/\s+/g,' ');
    if(!title||title.length>100) {rejected.push(`Row ${index+1}: title must contain 1–100 characters.`);return;}
    let url;
    try {const parsed=new URL(String(item.url??''));if(!['http:','https:'].includes(parsed.protocol))throw Error();parsed.hash='';url=parsed.href;} catch {rejected.push(`Row ${index+1}: use an http/https source identifier.`);return;}
    if(seen.has(url)){duplicates++;return;}seen.add(url);
    records.push({key:url,sourceId:String(item.id??`fixture-${index+1}`),source:String(item.source??'Synthetic classroom fixture').trim(),url,title,category:String(item.category??'General').trim().toLowerCase()||'general',body:String(item.body??'').trim().replace(/\s+/g,' '),status:'Needs human review'});
  });
  return {ok:true,records,rejected,duplicates,inputCount:input.length};
}
export function mergeRecords(existing,incoming) {
  const seen=new Set(existing.map(r=>r.key));const added=[];let skipped=0;
  for(const r of incoming){if(seen.has(r.key)){skipped++;continue;}seen.add(r.key);added.push({...r});}
  return {queue:[...existing,...added],added:added.length,skipped};
}
