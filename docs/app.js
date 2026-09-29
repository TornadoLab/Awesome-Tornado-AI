/* Original dependency-free explorer. Data and citations live in data/papers.json. */
(() => {
  'use strict';
  const {papers, categories, config, routes} = window.TORNADO_CATALOG;
  const $ = id => document.getElementById(id);
  const escape = value => String(value ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const byId = new Map(papers.map(p => [p.id, p]));
  const categoryNames = new Map(categories.map(c => [c.id, c.name]));
  const state = {q:'', category:'', scope:'', year:'', status:'', curation:'', sort:'newest', code:false, saved:false, route:'', limit:12};
  const storageKey = 'tornadolab-reading-list-v1';
  let saved = new Set();
  let toastTimer;
  let filtered = [];
  try {
    const stored = JSON.parse(localStorage.getItem(storageKey) || '[]');
    if (Array.isArray(stored)) saved = new Set(stored.filter(id => byId.has(id)));
  } catch (_) { /* A blocked browser store must not break the explorer. */ }
  const plainSearch = p => [p.id,p.title,...p.authors,p.venue,p.method,p.inputs,p.target_and_horizon,p.summary,p.summary_zh,p.region,categoryNames.get(p.category)].join(' ').toLowerCase();
  const searchIndex = new Map(papers.map(p => [p.id,plainSearch(p)]));
  function notify(message) {
    $('toast').textContent = message;
    $('toast').classList.add('visible');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => $('toast').classList.remove('visible'), 2600);
  }
  function syncHash() {
    const params = new URLSearchParams();
    for (const key of ['q','category','scope','year','status','curation','route']) if (state[key]) params.set(key,state[key]);
    if (state.sort !== 'newest') params.set('sort',state.sort);
    if (state.code) params.set('code','1');
    if (state.saved) params.set('saved','1');
    try { history.replaceState(null,'',location.pathname + location.search + '#collection' + (params.size ? '?' + params.toString() : '')); }
    catch (_) { /* file:// history policy varies between browsers. */ }
  }
  function readHash() {
    const query = location.hash.split('?')[1];
    if (!query) return;
    const params = new URLSearchParams(query);
    for (const key of ['q','category','scope','year','status','curation','route']) state[key] = params.get(key) || '';
    state.code = params.get('code') === '1'; state.saved = params.get('saved') === '1';
    state.sort = ['newest','oldest','title'].includes(params.get('sort')) ? params.get('sort') : 'newest';
    if (!categories.some(c => c.id === state.category)) state.category = '';
    if (!routes.some(r => r.id === state.route)) state.route = '';
    if (!['','direct','context','transfer'].includes(state.scope)) state.scope = '';
    if (!['','annotated','bibliographic'].includes(state.curation)) state.curation = '';
    if (!['','journal','conference','preprint','report','chapter'].includes(state.status)) state.status = '';
    if (!papers.some(p => String(p.year) === state.year)) state.year = '';
  }
  function syncControls() {
    $('search').value = state.q;
    for (const key of ['scope','year','status','curation','sort']) $(key).value = state[key];
    $('code-only').checked = state.code;
    $('saved-toggle').setAttribute('aria-pressed',String(state.saved));
    $('saved-count').textContent = saved.size;
  }
  function renderCategories() {
    const rows = [{id:'',name:'All directions',name_zh:'全部方向'},...categories];
    $('category-list').innerHTML = rows.map(c => `<button class="category-button ${state.category===c.id ? 'active':''}" data-category="${escape(c.id)}" title="${escape(c.name_zh)}" aria-pressed="${state.category===c.id}"><span>${escape(c.name)}</span><small>${c.id ? papers.filter(p=>p.category===c.id).length : papers.length}</small></button>`).join('');
  }
  function card(p) {
    const shortAuthor = p.authors[0] + ((p.authors.length>1 || !p.authors_complete) ? ' et al.' : '');
    return `<article class="paper-card" data-id="${p.id}">
      <button class="save-button ${saved.has(p.id)?'saved':''}" data-save="${p.id}" aria-pressed="${saved.has(p.id)}" aria-label="${saved.has(p.id)?'Remove from':'Add to'} reading list: ${escape(p.title)}">${saved.has(p.id)?'★':'☆'}</button>
      <div class="paper-meta"><span class="year">${p.year}</span><span>/</span><span>${escape(p.publication_status.toUpperCase())}</span><span>· ${escape(p.record_type.toUpperCase())}</span>${p.code_url?'<span>· CODE</span>':''}</div>
      <h3><button data-open="${p.id}">${escape(p.title)}</button></h3>
      <p class="paper-author">${escape(shortAuthor)} · ${escape(categoryNames.get(p.category))}</p>
      <p class="paper-summary">${escape(p.summary)}</p>
      <div class="paper-bottom"><span class="scope"><b class="dot ${p.scope}"></b>${p.scope}</span><div class="paper-links"><button class="text-button" data-open="${p.id}">Details</button>${p.code_url?`<a href="${escape(p.code_url)}" target="_blank" rel="noopener noreferrer">Code ↗</a>`:''}<a href="${escape(p.url)}" target="_blank" rel="noopener noreferrer" aria-label="Primary source: ${escape(p.title)}">Paper ↗</a></div></div>
    </article>`;
  }
  function render(updateHash=true) {
    const tokens = state.q.toLowerCase().trim().split(/\s+/).filter(Boolean);
    const route = routes.find(r=>r.id===state.route);
    filtered = papers.filter(p => tokens.every(t=>searchIndex.get(p.id).includes(t)) &&
      (!state.category || p.category===state.category) && (!state.scope || p.scope===state.scope) &&
      (!state.year || String(p.year)===state.year) && (!state.status || p.publication_status===state.status) &&
      (!state.curation || p.record_type===state.curation) &&
      (!state.code || p.code_url) && (!state.saved || saved.has(p.id)) && (!route || route.papers.includes(p.id)));
    filtered.sort((a,b) => state.sort==='title' ? a.title.localeCompare(b.title) :
      (state.sort==='oldest' ? a.year-b.year : b.year-a.year) || a.title.localeCompare(b.title));
    if (route && !state.q) filtered.sort((a,b)=>route.papers.indexOf(a.id)-route.papers.indexOf(b.id));
    $('papers').innerHTML = filtered.length ? filtered.slice(0,state.limit).map(card).join('') : '<div class="empty-state"><strong>No signals in this slice.</strong><br>Try a broader term, another scope, or Reset.</div>';
    $('result-count').textContent = `${filtered.length} ${filtered.length===1?'record':'records'} / ${papers.length} in the atlas`;
    $('load-more').hidden = filtered.length <= state.limit;
    $('load-more').textContent = `More signals (${Math.min(12,Math.max(0,filtered.length-state.limit))}) ↓`;
    $('active-route').hidden = !route;
    $('active-route').textContent = route ? `Reading route: ${route.name} / ${route.name_zh} · route order; other filters still apply` : '';
    $('export-bib').disabled = !filtered.length;
    renderCategories(); syncControls();
    if (updateHash) syncHash();
  }
  function reset() {
    Object.assign(state,{q:'',category:'',scope:'',year:'',status:'',curation:'',sort:'newest',code:false,saved:false,route:'',limit:12});
    render();
  }
  function savePaper(id) {
    if (!byId.has(id)) return;
    if (saved.has(id)) saved.delete(id); else saved.add(id);
    try {localStorage.setItem(storageKey,JSON.stringify([...saved]));}
    catch (_) {notify('Saved for this session. Browser storage is unavailable.');}
    render(false);
  }
  function openPaper(id) {
    const p = byId.get(id); if (!p) return;
    $('dialog-body').innerHTML = `
      <div class="dialog-meta">${p.year} / ${escape(p.publication_status.toUpperCase())} / ${escape(p.scope.toUpperCase())} / ${escape(p.record_type.toUpperCase())}</div>
      <h2 class="dialog-title" id="dialog-title">${escape(p.title)}</h2>
      <p class="dialog-authors">${escape(p.authors.join('; '))}${p.authors_complete?'':' et al. — author metadata incomplete'}<br>${escape(p.venue)}</p>
      <p class="dialog-abstract">${escape(p.summary)}</p><p class="dialog-zh" lang="zh-CN">${escape(p.summary_zh)}</p>
      <div class="field-grid"><div><strong>Method</strong>${escape(p.method)}</div><div><strong>Inputs</strong>${escape(p.inputs)}</div><div><strong>Target &amp; horizon</strong>${escape(p.target_and_horizon)}</div><div><strong>Research direction / region</strong>${escape(categoryNames.get(p.category))} / ${escape(p.region)}</div></div>
      <p class="caution">${escape(p.caveat)}</p>
      ${p.code_url?'':'<p class="provenance">Code repository: not verified in this snapshot. This does not mean no code exists.</p>'}
      <p class="provenance">Verification: ${escape(p.verification.level)} · checked ${escape(p.verification.checked_on)} · independently reproduced: ${p.verification.reproduced?'yes':'no'}${p.preprint_year?` · initial preprint ${p.preprint_year}`:''}.</p>
      <div class="dialog-links"><a class="button primary" href="${escape(p.url)}" target="_blank" rel="noopener noreferrer">Primary source ↗</a>${p.code_url?`<a class="button ghost" href="${escape(p.code_url)}" target="_blank" rel="noopener noreferrer">Author-linked code ↗</a>`:''}<button class="button ghost" data-copy="${p.id}">Copy BibTeX</button><button class="button ghost" data-save="${p.id}">Toggle reading list ☆</button></div>
      <details><summary class="dialog-bibsummary">Inspect bibliographic metadata</summary><pre class="bib-box">${escape(p.bibtex)}</pre></details>
      <p class="provenance">Primary provenance &amp; corrections:</p><div class="source-list">${p.sources.map((u,i)=>`<p><a href="${escape(u)}" target="_blank" rel="noopener noreferrer">${i+1}. ${escape(u)} ↗</a></p>`).join('')}</div>`;
    if (!$('paper-dialog').open) $('paper-dialog').showModal();
    $('paper-dialog').scrollTop=0;
  }
  function download(text,filename,mime) {
    const url=URL.createObjectURL(new Blob([text],{type:mime}));
    const a=document.createElement('a');a.href=url;a.download=filename;document.body.appendChild(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),1000);
  }
  async function copyCitation(id) {
    const p=byId.get(id);if(!p)return;
    try {await navigator.clipboard.writeText(p.bibtex);notify('BibTeX copied. Verify partial author lists before submission.');}
    catch (_) {download(p.bibtex,p.id+'.bib','application/x-bibtex;charset=utf-8');notify('Clipboard unavailable; citation exported as a .bib file.');}
  }
  document.addEventListener('click',event=>{
    const open=event.target.closest('[data-open]'); if(open){openPaper(open.dataset.open);return;}
    const save=event.target.closest('[data-save]'); if(save){savePaper(save.dataset.save);return;}
    const copy=event.target.closest('[data-copy]'); if(copy){copyCitation(copy.dataset.copy);return;}
    const cat=event.target.closest('[data-category]'); if(cat){state.category=cat.dataset.category;state.route='';state.limit=12;render();return;}
    const route=event.target.closest('[data-route]'); if(route){reset();state.route=route.dataset.route;render();$('collection').scrollIntoView({behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'instant':'smooth'});}
  });
  $('search').addEventListener('input',e=>{state.q=e.target.value;state.limit=12;render();});
  for(const key of ['scope','year','status','curation','sort']) $(key).addEventListener('change',e=>{state[key]=e.target.value;state.limit=12;render();});
  $('code-only').addEventListener('change',e=>{state.code=e.target.checked;state.limit=12;render();});
  $('saved-toggle').addEventListener('click',()=>{state.saved=!state.saved;state.limit=12;render();});
  $('clear-filters').addEventListener('click',reset);
  $('load-more').addEventListener('click',()=>{state.limit+=12;render(false);});
  $('export-bib').addEventListener('click',()=>download('% Source-linked seed; verify metadata before manuscript submission.\n\n'+filtered.map(p=>p.bibtex).join('\n'),'tornadolab-filtered.bib','application/x-bibtex;charset=utf-8'));
  $('random-hero').addEventListener('click',()=>{const pool=filtered.length?filtered:papers;openPaper(pool[Math.floor(Math.random()*pool.length)].id);});
  $('close-dialog').addEventListener('click',()=>$('paper-dialog').close());
  $('paper-dialog').addEventListener('click',e=>{if(e.target===$('paper-dialog')){const b=$('paper-dialog').getBoundingClientRect();if(e.clientX<b.left||e.clientX>b.right||e.clientY<b.top||e.clientY>b.bottom)$('paper-dialog').close();}});
  document.addEventListener('keydown',e=>{if(e.key==='/' && !['INPUT','TEXTAREA','SELECT'].includes(document.activeElement.tagName) && !$('paper-dialog').open){e.preventDefault();$('search').focus();$('collection').scrollIntoView();}});
  window.addEventListener('hashchange',()=>{readHash();state.limit=12;render(false);});
  $('stat-count').textContent=papers.length;
  $('stat-categories').textContent=categories.length;
  $('stat-years').textContent=`${Math.min(...papers.map(p=>p.year))}—${Math.max(...papers.map(p=>p.year))}`;
  $('stat-date').textContent=config.snapshot_date;
  $('curation-counts').textContent=`${papers.filter(p=>p.record_type==='annotated').length} annotated papers · ${papers.filter(p=>p.record_type==='bibliographic').length} bibliographic records · ${papers.filter(p=>p.code_url).length} verified code links`;
  $('year').innerHTML+=[...new Set(papers.map(p=>p.year))].sort((a,b)=>b-a).map(y=>`<option value="${y}">${y}</option>`).join('');
  $('route-cards').innerHTML=routes.map(r=>`<button class="route-card" data-route="${r.id}"><small>${escape(r.level)}</small><span class="route-arrow" aria-hidden="true">↗</span><h3>${escape(r.name)}</h3><p>${escape(r.description)}</p></button>`).join('');
  readHash();render(false);
})();
