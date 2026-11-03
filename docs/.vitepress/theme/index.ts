import DefaultTheme from 'vitepress/theme'
import { nextTick, onMounted } from 'vue'
import ClassWorkCard from './ClassWorkCard.vue'
import ProcessFlow from './ProcessFlow.vue'
import './custom.css'
function revealHash(){let el;try{el=document.getElementById(decodeURIComponent(location.hash.slice(1)))}catch{return}if(!el)return;let opened=false;for(let p=el.parentElement;p;p=p.parentElement){if(p instanceof HTMLDetailsElement&&!p.open){p.open=true;opened=true}}if(opened)requestAnimationFrame(()=>el.scrollIntoView({block:'start'}))}
export default {extends:DefaultTheme,setup(){onMounted(revealHash)},enhanceApp({app,router}){app.component('ClassWorkCard',ClassWorkCard);app.component('ProcessFlow',ProcessFlow);if(typeof window!=='undefined'){window.addEventListener('hashchange',revealHash);document.addEventListener('click',(event)=>{const a=event.target instanceof Element?event.target.closest('a[href]'):null;if(!a)return;const u=new URL(a.getAttribute('href'),location.href);if(u.origin===location.origin&&u.pathname===location.pathname&&u.hash===location.hash)revealHash()},true);router.onAfterRouteChange=async()=>{await nextTick();revealHash()}}}}
