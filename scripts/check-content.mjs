import fs from 'node:fs'
import path from 'node:path'
const docs=path.resolve('docs')
const site=JSON.parse(fs.readFileSync('site.json','utf8'))
const walk=d=>fs.readdirSync(d,{withFileTypes:true}).flatMap(e=>e.name.startsWith('.')?[]:e.isDirectory()?walk(path.join(d,e.name)):[path.join(d,e.name)])
const pages=walk(docs).filter(p=>p.endsWith('.md')&&!p.startsWith(path.join(docs,'public')+path.sep))
const failures=[]
function resolveLink(link,source){
 if(link.startsWith(site.base))link='/'+link.slice(site.base.length)
 if(/^(?:https?:|mailto:|tel:|data:)/.test(link))return
 const route=decodeURIComponent(link.split('#')[0].split('?')[0]);if(!route)return
 const p=route.startsWith('/')?path.join(docs,route):path.resolve(path.dirname(source),route)
 const list=[p,p+'.md',p.replace(/\.html$/,'.md'),path.join(p,'index.md')]
 if(route.startsWith('/'))list.push(path.join(docs,'public',route))
 if(!list.some(x=>fs.existsSync(x)&&fs.statSync(x).isFile()))failures.push(`${path.relative(docs,source)} → ${link}`)
}
for(const page of pages){
 const source=fs.readFileSync(page,'utf8').replace(/```[\s\S]*?```/g,'')
 for(const m of source.matchAll(/\]\(([^\s)]+)\)|\b(?:href|src)=["']([^"']+)["']/g))resolveLink(m[1]||m[2],page)
}
const sections=JSON.parse(fs.readFileSync('data/classes.json','utf8'))
if(!Object.keys(sections).length)failures.push('No section class cards')
for(const [id,section] of Object.entries(sections)){
 const keys=new Set();const dates=new Set()
 if(!Number.isInteger(section.courseId))failures.push(`Section ${id}: missing Canvas course ID`)
 for(const c of section.checkpoints){
  if(keys.has(c.key))failures.push(`Section ${id}: duplicate checkpoint ${c.key}`);keys.add(c.key)
  if(!['posted','planned'].includes(c.status))failures.push(`Invalid status ${c.key}`)
  if((c.status==='posted')!==Number.isInteger(c.assignmentId))failures.push(`${id}/${c.key}: posted must have real assignment ID; planned must not`)
  if(!/^2026-\d\d-\d\d$/.test(c.date)||!c.time)failures.push(`Missing date/time ${c.key}`)
 }
 for(const c of section.classes){
  if(dates.has(c.date))failures.push(`${id}: duplicate class date ${c.date}`);dates.add(c.date)
  for(const field of ['label','bring','work','review','update'])if(!c[field])failures.push(`${id}/${c.date}: missing ${field}`)
  for(const key of [...(c.due||[]),...(c.next||[])])if(!keys.has(key))failures.push(`${id}/${c.date}: unknown ${key}`)
  for(const obj of [c.guide,c.example])if(!obj?.text||!obj.link)failures.push(`${id}/${c.date}: incomplete guide/example`);else resolveLink(obj.link,path.join(docs,'index.md'))
 }
}
// Prevent another stale/current-student mismatch on the course homepage.
const home=fs.readFileSync(path.join(docs,'index.md'),'utf8')
for(const snippet of [
  '<ClassWorkCard section="001" />',
  '/assignments/769188',
  '/assignments/769189',
  '/course/get-unstuck',
  'two submission boxes',
  '/students/from-app-studio'
]) if(!home.includes(snippet))failures.push('Homepage missing current student path: '+snippet)
for(const obsolete of ['## Today: start the research and find a partner', '**Existing Server and App Studios remain due Nov 6']) {
  if(home.includes(obsolete))failures.push('Homepage still presents historical instruction as current: '+obsolete)
}
const instructorFiles=['instructor/canvas-homepage.html','instructor/canvas-rag-clarification.html','instructor/CANVAS-UPDATE.md']
for(const file of instructorFiles)if(!fs.existsSync(file))failures.push('Missing instructor Canvas copy: '+file)
if(failures.length)throw Error(failures.join('\n'))
console.log(`Checked ${pages.length} content pages and ${Object.keys(sections).length} section schedules.`)
