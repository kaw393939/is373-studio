<script setup>
import {computed,onMounted,ref} from 'vue'
import {withBase} from 'vitepress'
import allSections from '../../../data/classes.json'
const props=defineProps({section:{type:String,default:''}})
const data=computed(()=>allSections[props.section]||Object.values(allSections)[0])
const selected=ref(data.value?.classes[0]?.date||'')
const card=computed(()=>data.value.classes.find(c=>c.date===selected.value)||data.value.classes[0])
const link=path=>{if(/^https?:/.test(path))return path;const [route,hash]=path.split('#');return withBase(route+(route.endsWith('/')||/\.[a-z]+$/i.test(route)?'':'.html')+(hash?'#'+hash:''))}
const checkpoint=key=>data.value.checkpoints.find(c=>c.key===key)
const dueText=key=>{const c=checkpoint(key);const [y,m,d]=c.date.split('-');return `${Number(m)}/${Number(d)}/${y}, ${c.time} Eastern`}
onMounted(()=>{const today=new Intl.DateTimeFormat('en-CA',{timeZone:'America/New_York',year:'numeric',month:'2-digit',day:'2-digit'}).format(new Date());selected.value=(data.value.classes.find(c=>c.date>=today)||data.value.classes.at(-1)).date})
</script>
<template>
<section class="class-work-card" aria-label="Your next class task">
<label :for="'class-date-'+section">Choose your class date</label>
<select :id="'class-date-'+section" v-model="selected"><option v-for="c in data.classes" :key="c.date" :value="c.date">{{c.label}}</option></select>
<h3>{{card.label}}</h3>
<p v-if="card.win" class="class-win"><strong>Your goal</strong>{{card.win}}</p>
<dl><dt>In class</dt><dd>{{card.work}}</dd><dt>Together</dt><dd>{{card.review}}</dd><dt>Keep</dt><dd>{{card.update}}</dd></dl>
<div v-for="kind in ['due','next']" :key="kind"><template v-if="card[kind]?.length"><strong>{{kind==='due'?'Due / target':'Next hand-in'}}</strong><ul class="handins"><li v-for="key in card[kind]" :key="key"><span class="status">{{checkpoint(key).status==='posted'?'Posted':'Planned'}}</span> <a v-if="checkpoint(key).assignmentId" :href="'https://njit.instructure.com/courses/'+data.courseId+'/assignments/'+checkpoint(key).assignmentId">{{checkpoint(key).title}}</a><span v-else>{{checkpoint(key).title}}</span><strong v-if="checkpoint(key).points" class="points">{{checkpoint(key).points}} points</strong><small>{{dueText(key)}}</small></li></ul></template></div>
<p class="card-links"><a :href="link(card.guide.link)">{{card.guide.text}}</a> · <a :href="link(card.example.link)">{{card.example.text}}</a></p>
<details><summary>What to bring and class notes</summary><p><strong>Bring:</strong> {{card.bring}}</p><p v-if="card.note">{{card.note}}</p></details>
<small>Canvas confirms deadlines and points. Planned targets are preparation only. Update the same project record.</small>
</section>
</template>
<style scoped>
.class-work-card{padding:22px;border:2px solid var(--vp-c-brand-1);border-radius:12px;background:var(--vp-c-bg-soft);margin:18px 0 28px}.class-work-card label{font-weight:700;display:block;margin-bottom:6px}.class-work-card select{width:100%;padding:10px;border:1px solid var(--vp-c-divider);border-radius:6px;background:var(--vp-c-bg);color:var(--vp-c-text-1);font:inherit}.class-work-card h3{margin:18px 0 14px}.class-win{padding:12px 14px;background:var(--vp-c-bg);border-left:4px solid var(--vp-c-brand-1);line-height:1.5}.class-win strong{display:block;font-size:.78rem;text-transform:uppercase;letter-spacing:.06em;margin-bottom:4px;color:var(--vp-c-brand-1)}.class-work-card dl{display:grid;grid-template-columns:85px 1fr;gap:12px;margin:18px 0 22px}.class-work-card dt{font-weight:700}.class-work-card dd{margin:0}.class-work-card .handins{list-style:none;padding:0;margin:8px 0 18px}.handins li{padding:10px 0;border-bottom:1px solid var(--vp-c-divider);line-height:1.5}.handins small{display:block;margin-top:4px}.points{display:inline-block;font-size:.8rem;margin-left:8px;padding:1px 6px;border-radius:4px;background:var(--vp-c-bg);white-space:nowrap}.status{font-size:.72rem;border:1px solid var(--vp-c-divider);padding:2px 5px;border-radius:4px;margin-right:5px;font-weight:700}.class-work-card small{font-size:.8rem;line-height:1.5}.class-work-card details{padding:10px 0;margin:12px 0;border:0;border-top:1px solid var(--vp-c-divider)}.class-work-card summary{cursor:pointer;font-size:.88rem}.class-work-card details p{font-size:.88rem}.card-links{font-weight:650}.class-work-card :focus-visible{outline:3px solid var(--vp-c-brand-1);outline-offset:3px}@media(max-width:520px){.class-work-card{padding:16px}.class-work-card dl{grid-template-columns:1fr;gap:3px}.class-work-card dd{margin-bottom:10px}.points{margin-left:5px}}
</style>
