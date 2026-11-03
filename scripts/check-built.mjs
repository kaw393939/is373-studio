import fs from 'node:fs'
import path from 'node:path'
const site=JSON.parse(fs.readFileSync('site.json','utf8'))
const root=path.resolve('docs/.vitepress/dist')
const files=[];const walk=d=>{for(const e of fs.readdirSync(d,{withFileTypes:true})){const p=path.join(d,e.name);e.isDirectory()?walk(p):files.push(p)}};walk(root)
const html=files.filter(x=>x.endsWith('.html'));const ids=new Map();const failures=new Set();let checked=0
for(const p of html){const source=fs.readFileSync(p,'utf8');ids.set(p,new Set([...source.matchAll(/\bid=["']([^"']+)["']/g)].map(m=>m[1])))}
for(const p of html){
 const route=site.base+path.relative(root,p).split(path.sep).join('/')
 const source=fs.readFileSync(p,'utf8')
 for(const m of source.matchAll(/\b(?:href|src)=["']([^"']+)["']/g)){
  const raw=m[1].replace(/&amp;/g,'&');if(/^(?:https?:|mailto:|tel:|data:|javascript:)/.test(raw)||!raw)continue
  const url=new URL(raw,'https://site.test'+route)
  if(!url.pathname.startsWith(site.base)){failures.add(`${route} → outside Pages base: ${raw}`);continue}
  const rel=decodeURIComponent(url.pathname.slice(site.base.length));let target=path.join(root,rel)
  if(fs.existsSync(target)&&fs.statSync(target).isDirectory())target=path.join(target,'index.html')
  else if(!fs.existsSync(target)&&!path.extname(target))target+='.html'
  if(!fs.existsSync(target)){failures.add(`${route} → missing: ${raw}`);continue}
  checked++
  if(url.hash&&ids.has(target)&&!ids.get(target).has(decodeURIComponent(url.hash.slice(1))))failures.add(`${route} → missing anchor: ${raw}`)
 }
 // Standalone examples must stay full-page HTML routes, not VitePress SPA navigation.
 if(!p.includes(path.join('examples',path.sep))||source.includes('VitePress')){
  for(const m of source.matchAll(/<a\b([^>]*\bhref=["'][^"']*\/examples\/[^"']+\/[^"']+\.html[^>]*>)/g)){
   if(!/target=["']_self["']/.test(m[1]))failures.add(`${route}: standalone example link missing native navigation: ${m[0].slice(0,180)}`)
  }
 }
}

// Future class cards are client-selected: verify every destination, not only the SSR first date.
const sections=JSON.parse(fs.readFileSync('data/classes.json','utf8'))
for(const [section,data] of Object.entries(sections))for(const c of data.classes)for(const item of [c.guide,c.example]){
 const [route,hash]=item.link.split('#');if(/^https?:/.test(route))continue
 let dest=path.join(root,route);dest=route.endsWith('/')?path.join(dest,'index.html'):/\.[a-z]+$/i.test(route)?dest:dest+'.html'
 if(!fs.existsSync(dest))failures.add(`Class ${section}/${c.date} → missing ${item.link}`)
 else if(hash&&!ids.get(dest)?.has(decodeURIComponent(hash)))failures.add(`Class ${section}/${c.date} → missing anchor ${item.link}`)
 checked++
}

if(failures.size)throw Error([...failures].join('\n'))
console.log(`Checked ${checked} local links/assets/anchors across ${html.length} built HTML pages.`)
