/* Shared page engine for Telcodex.io topic pages.
   Each page sets window.PAGE = { md: "<file>.md", key: "<topicKey>" } before this loads.
   Renders markdown into #doc, builds the TOC, injects Related topics, wires consent. */

/* ---------- Topic registry (for nav active-state + related links) ---------- */
const TOPICS = [
  { key:"standardization", url:"standardization.html", nav:"Standardization & Timeline", title:"Standardization & Timeline", blurb:"Release 20 vs 21 and the approved 6G freeze dates." },
  { key:"features",        url:"features.html",        nav:"Features",                   title:"6G Features",            blurb:"Sub-THz, AI-native radio, ISAC, ambient IoT and more." },
  { key:"architecture",    url:"architecture.html",    nav:"Network Architecture",       title:"Network Architecture",   blurb:"How the RAN and core evolve for 6G, with diagrams." },
  { key:"ran",             url:"ran.html",             nav:"RAN",                        title:"6G RAN",                 blurb:"The radio access network: spectrum, air interface, MIMO." },
  { key:"core",            url:"core.html",            nav:"Core",                       title:"6G Core",                blurb:"The next-generation core and service-based architecture." },
  { key:"management",      url:"management.html",      nav:"Network Management",         title:"Network Management",     blurb:"Intent-driven, AI-assisted, closed-loop operation." },
  { key:"isac",            url:"isac.html",            nav:null,                         title:"ISAC",                   blurb:"Integrated Sensing and Communication — sensing over the network." }
];

/* ---------- Markdown renderer ---------- */
function esc(s){return s.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");}
function inline(s){
  s=esc(s);
  s=s.replace(/!\[([^\]]*)\]\(([^)]+)\)/g,'<img alt="$1" src="$2" />');
  s=s.replace(/\[([^\]]+)\]\(([^)]+)\)/g,'<a href="$2">$1</a>');
  s=s.replace(/`([^`]+)`/g,'<code>$1</code>');
  s=s.replace(/\*\*([^*]+)\*\*/g,'<strong>$1</strong>');
  s=s.replace(/\*([^*]+)\*/g,'<em>$1</em>');
  return s;
}
function renderTable(rows){
  const cells=r=>r.trim().replace(/^\||\|$/g,"").split("|").map(c=>c.trim());
  const head=cells(rows[0]);
  let html='<div class="table-wrap"><table><thead><tr>';
  head.forEach(h=>html+="<th>"+inline(h)+"</th>");
  html+="</tr></thead><tbody>";
  for(let i=2;i<rows.length;i++){
    if(!rows[i].trim())continue;
    html+="<tr>";cells(rows[i]).forEach(c=>html+="<td>"+inline(c)+"</td>");html+="</tr>";
  }
  return html+"</tbody></table></div>";
}
function mdToHtml(md){
  const lines=md.replace(/\r\n/g,"\n").split("\n");
  let out=[],i=0;
  const isSep=s=>/^\s*\|?[\s:|-]+\|[\s:|-]*$/.test(s)&&s.includes("-");
  while(i<lines.length){
    let line=lines[i];
    if(/^\s*$/.test(line)){i++;continue;}
    if(/^\s*---\s*$/.test(line)){out.push("<hr/>");i++;continue;}
    const h=line.match(/^(#{1,6})\s+(.*)$/);
    if(h){out.push(`<h${h[1].length}>${inline(h[2])}</h${h[1].length}>`);i++;continue;}
    if(/^\s*>\s?/.test(line)){
      let buf=[];
      while(i<lines.length&&/^\s*>\s?/.test(lines[i])){buf.push(lines[i].replace(/^\s*>\s?/,""));i++;}
      out.push("<blockquote>"+mdToHtml(buf.join("\n"))+"</blockquote>");continue;
    }
    if(line.includes("|")&&i+1<lines.length&&isSep(lines[i+1])){
      let buf=[line];i++;buf.push(lines[i]);i++;
      while(i<lines.length&&lines[i].includes("|")&&lines[i].trim()){buf.push(lines[i]);i++;}
      out.push(renderTable(buf));continue;
    }
    if(/^\s*[-*]\s+/.test(line)){
      let buf=[];
      while(i<lines.length&&/^\s*[-*]\s+/.test(lines[i])){
        let item=lines[i].replace(/^\s*[-*]\s+/,"");i++;
        while(i<lines.length&&lines[i].trim()&&/^\s+/.test(lines[i])&&!/^\s*[-*]\s+/.test(lines[i])&&!/^\s*\d+\.\s+/.test(lines[i])){item+=" "+lines[i].trim();i++;}
        buf.push("<li>"+inline(item)+"</li>");
      }
      out.push("<ul>"+buf.join("")+"</ul>");continue;
    }
    if(/^\s*\d+\.\s+/.test(line)){
      let buf=[];
      while(i<lines.length&&/^\s*\d+\.\s+/.test(lines[i])){
        let item=lines[i].replace(/^\s*\d+\.\s+/,"");i++;
        while(i<lines.length&&lines[i].trim()&&/^\s+/.test(lines[i])&&!/^\s*[-*]\s+/.test(lines[i])&&!/^\s*\d+\.\s+/.test(lines[i])){item+=" "+lines[i].trim();i++;}
        buf.push("<li>"+inline(item)+"</li>");
      }
      out.push("<ol>"+buf.join("")+"</ol>");continue;
    }
    let buf=[line];i++;
    while(i<lines.length&&!/^\s*$/.test(lines[i])&&!/^(#{1,6})\s/.test(lines[i])&&!/^\s*[-*]\s+/.test(lines[i])&&!/^\s*\d+\.\s+/.test(lines[i])&&!/^\s*>/.test(lines[i])&&!/^\s*---\s*$/.test(lines[i])&&!lines[i].includes("|")){buf.push(lines[i]);i++;}
    out.push("<p>"+inline(buf.join(" "))+"</p>");
  }
  return out.join("\n");
}

function buildTOC(docEl,tocEl){
  tocEl.innerHTML="";
  const heads=docEl.querySelectorAll("h2");
  if(!heads.length){tocEl.innerHTML='<span style="font-size:13px;color:var(--ink-faint)">—</span>';return;}
  heads.forEach((hh,idx)=>{const id="sec-"+idx;hh.id=id;const a=document.createElement("a");a.href="#"+id;a.textContent=hh.textContent;tocEl.appendChild(a);});
}

function injectRelated(key){
  const others=TOPICS.filter(t=>t.key!==key&&t.nav);  // exclude self and isac (no nav)
  const picks=others.slice(0,3);
  const wrap=document.createElement("div");
  wrap.className="related";
  wrap.innerHTML='<h4>Related topics</h4><div class="cards">'+
    picks.map(t=>`<a href="${t.url}"><strong>${t.title}</strong><span>${t.blurb}</span></a>`).join("")+
    '</div>';
  const main=document.querySelector("main");
  const bottomAd=main.querySelector(".ad-inline");
  if(bottomAd) main.insertBefore(wrap,bottomAd); else main.appendChild(wrap);
}

async function renderDoc(){
  const docEl=document.getElementById("doc");
  const tocEl=document.getElementById("toc");
  if(!window.PAGE||!window.PAGE.md){return;}
  // If the build step already injected the content, don't fetch again.
  if(docEl && docEl.innerHTML.indexOf("<!-- prerendered -->")!==-1){return;}
  try{
    const res=await fetch(window.PAGE.md,{cache:"no-store"});
    if(!res.ok)throw new Error(res.status);
    docEl.innerHTML=mdToHtml(await res.text());
    if(tocEl)buildTOC(docEl,tocEl);
    if(window.PAGE.key)injectRelated(window.PAGE.key);
  }catch(err){
    docEl.innerHTML='<p class="loading">Couldn\'t load this page. If you opened the file directly, run a local server (e.g. <code>python -m http.server 8000</code>) and reload.</p>';
  }
}

/* ================= CONSENT / CMP (shared) ================= */
const USE_GOOGLE_CMP = false;      // flip true after pasting Funding Choices snippet + setting ADS_CLIENT
const ENABLE_AUTO_ADS = true;      // use AdSense Auto Ads (one tag) instead of manual slots
const CONSENT_KEY = "cc_consent_v2";
const CONSENT_VERSION = 2;
const ADS_CLIENT = "ca-pub-1740697015974190";   // AdSense Publisher ID
const ANALYTICS_ID = "";           // e.g. "G-XXXXXXXXXX"

const $ = id => document.getElementById(id);
function readConsent(){try{const c=JSON.parse(localStorage.getItem(CONSENT_KEY));if(!c||c.version!==CONSENT_VERSION)return null;return c;}catch{return null;}}
function saveConsent(a,ads){const r={version:CONSENT_VERSION,necessary:true,analytics:!!a,ads:!!ads,timestamp:new Date().toISOString()};localStorage.setItem(CONSENT_KEY,JSON.stringify(r));applyConsent(r);return r;}

let adsLoaded=false,analyticsLoaded=false;
function loadAds(){
  if(adsLoaded||!ADS_CLIENT)return;adsLoaded=true;
  const s=document.createElement("script");s.async=true;
  s.src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client="+ADS_CLIENT;
  s.crossOrigin="anonymous";document.head.appendChild(s);
  if(ENABLE_AUTO_ADS){
    try{(window.adsbygoogle=window.adsbygoogle||[]).push({google_ad_client:ADS_CLIENT,enable_page_level_ads:true});}catch(e){}
  }else{
    document.querySelectorAll(".ad").forEach(slot=>{
      const l=slot.querySelector(".ad-label");if(l)l.remove();
      const ins=document.createElement("ins");ins.className="adsbygoogle";ins.style.display="block";
      ins.setAttribute("data-ad-client",ADS_CLIENT);ins.setAttribute("data-ad-format","auto");
      ins.setAttribute("data-full-width-responsive","true");slot.appendChild(ins);
      try{(window.adsbygoogle=window.adsbygoogle||[]).push({});}catch(e){}
    });
  }
}
function loadAnalytics(){
  if(analyticsLoaded||!ANALYTICS_ID)return;analyticsLoaded=true;
  const s=document.createElement("script");s.async=true;s.src="https://www.googletagmanager.com/gtag/js?id="+ANALYTICS_ID;document.head.appendChild(s);
  window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}window.gtag=gtag;gtag("js",new Date());gtag("config",ANALYTICS_ID,{anonymize_ip:true});
}
function applyConsent(c){if(c.ads)loadAds();if(c.analytics)loadAnalytics();}

function wireConsent(){
  const banner=$("ccBanner"),overlay=$("ccOverlay");
  if(!banner)return;
  const show=()=>banner.classList.remove("hidden"),hide=()=>banner.classList.add("hidden");
  const openPrefs=()=>{const c=readConsent();$("catAnalytics").checked=c?c.analytics:false;$("catAds").checked=c?c.ads:false;overlay.classList.remove("hidden");};
  const closePrefs=()=>overlay.classList.add("hidden");
  $("ccAccept").onclick=()=>{saveConsent(true,true);hide();};
  $("ccReject").onclick=()=>{saveConsent(false,false);hide();};
  $("ccCustomize").onclick=openPrefs;
  $("ccModalSave").onclick=()=>{saveConsent($("catAnalytics").checked,$("catAds").checked);closePrefs();hide();};
  $("ccModalReject").onclick=()=>{saveConsent(false,false);closePrefs();hide();};
  if($("ccSettings"))$("ccSettings").onclick=openPrefs;
  if($("ccDoNotSell"))$("ccDoNotSell").onclick=()=>{const c=readConsent()||{};saveConsent(c.analytics||false,false);alert("Advertising/sharing has been turned off for this browser.");};
  overlay.onclick=e=>{if(e.target===overlay)closePrefs();};
  const yr=$("yr");if(yr)yr.textContent=new Date().getFullYear();

  if(USE_GOOGLE_CMP){hide();closePrefs();banner.remove();overlay.remove();
    const g=()=>{if(window.googlefc&&googlefc.showRevocationMessage)googlefc.showRevocationMessage();};
    if($("ccSettings"))$("ccSettings").onclick=g;if($("ccDoNotSell"))$("ccDoNotSell").onclick=g;return;}

  const gpc=navigator.globalPrivacyControl===true;
  const existing=readConsent();
  if(existing){if(gpc&&existing.ads)saveConsent(existing.analytics,false);else applyConsent(existing);return;}
  show();
}

/* ---------- init ---------- */
document.addEventListener("DOMContentLoaded",()=>{
  // mark active nav link
  if(window.PAGE&&window.PAGE.key){
    document.querySelectorAll("nav.topics a").forEach(a=>{
      if(a.dataset.key===window.PAGE.key)a.classList.add("active");
    });
  }
  renderDoc();
  wireConsent();
});
