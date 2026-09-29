"""Shared, dependency-free catalog utilities. Python 3.10+."""
from __future__ import annotations
import csv
import io
import json
import re
from datetime import date
from pathlib import Path
from urllib.parse import quote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
STATUSES = {'journal', 'conference', 'preprint', 'report', 'chapter'}
SCOPES = {'direct', 'context', 'transfer'}
RECORD_TYPES = {'annotated', 'bibliographic'}
REQUIRED = {'id','year','title','authors','authors_complete','venue',
            'publication_status','category','scope','method','inputs',
            'target_and_horizon','summary','summary_zh','region','url',
            'doi','arxiv','code_url','preprint_year','caveat','sources','verification','record_type'}

def load(root: Path = ROOT) -> tuple[list[dict], list[dict], dict, list[dict]]:
    def read(name: str):
        return json.loads((root / 'data' / name).read_text(encoding='utf-8'))
    return read('papers.json'), read('categories.json'), read('config.json'), read('routes.json')

def safe_url(value: object) -> bool:
    if not isinstance(value, str) or any(ch.isspace() for ch in value):
        return False
    try:
        parts = urlsplit(value)
        return parts.scheme == 'https' and bool(parts.hostname) and not parts.username and not parts.password
    except ValueError:
        return False

def normalized_title(value: str) -> str:
    return re.sub(r'[^\w]+', '', value.casefold())

def doi_url(doi: str) -> str:
    """Keep legacy AMS DOI punctuation from breaking Markdown/HTML links."""
    return 'https://doi.org/' + quote(doi, safe='/')

def validate(papers: list[dict], categories: list[dict], config: dict,
             routes: list[dict]) -> list[str]:
    errors: list[str] = []
    try:
        snapshot = date.fromisoformat(config['snapshot_date'])
    except (KeyError, TypeError, ValueError):
        return ['config.snapshot_date must be an ISO calendar date']
    cat_ids = {c['id'] for c in categories}
    for c in categories:
        if not re.fullmatch(r'[a-z][a-z0-9-]*', c['id']):
            errors.append('Invalid category ID')
    if len(cat_ids) != len(categories):
        errors.append('Duplicate category ID')
    seen: dict[str, set] = {k: set() for k in ['id','doi','arxiv','title']}
    for index, p in enumerate(papers):
        name = str(p.get('id', f'row {index}'))
        missing = REQUIRED - p.keys()
        if missing:
            errors.append(f'{name}: missing {sorted(missing)}')
            continue
        if not re.fullmatch(r'[a-z][a-z0-9-]*', p['id']):
            errors.append(f'{name}: invalid ID')
        if not isinstance(p['year'], int) or not 1800 <= p['year'] <= snapshot.year:
            errors.append(f'{name}: invalid/future year')
        if p['publication_status'] not in STATUSES or p['scope'] not in SCOPES:
            errors.append(f'{name}: invalid status/scope')
        if p['record_type'] not in RECORD_TYPES:
            errors.append(f'{name}: invalid record type')
        if p['category'] not in cat_ids:
            errors.append(f'{name}: unknown category')
        if not isinstance(p['authors'], list) or not p['authors'] or not all(isinstance(a,str) and a.strip() for a in p['authors']):
            errors.append(f'{name}: authors must be non-empty strings')
        if type(p['authors_complete']) is not bool:
            errors.append(f'{name}: authors_complete must be boolean')
        for field in ['title','venue','method','inputs','target_and_horizon','summary','summary_zh','region','caveat']:
            if not isinstance(p[field], str) or not p[field].strip():
                errors.append(f'{name}: empty/invalid {field}')
        for field in ['url','code_url']:
            if (field == 'url' or p[field] is not None) and not safe_url(p[field]):
                errors.append(f'{name}: unsafe/invalid {field}')
        if not isinstance(p['sources'],list) or not p['sources'] or not all(safe_url(u) for u in p['sources']):
            errors.append(f'{name}: require HTTPS provenance URLs')
        if p['doi'] is not None and not re.fullmatch(r'10\.\d{4,9}/\S+',p['doi'],flags=re.I):
            errors.append(f'{name}: invalid DOI')
        if p['arxiv'] is not None and not re.fullmatch(r'\d{4}\.\d{4,5}',p['arxiv']):
            errors.append(f'{name}: invalid arXiv ID')
        if p['preprint_year'] is not None and (not isinstance(p['preprint_year'],int) or not 1800 <= p['preprint_year'] <= p['year']):
            errors.append(f'{name}: invalid preprint year')
        v=p['verification']
        if not isinstance(v,dict) or v.get('level') not in {'metadata','full_text','reproduced'} or type(v.get('reproduced')) is not bool:
            errors.append(f'{name}: invalid verification record')
        else:
            try:
                checked=date.fromisoformat(v.get('checked_on',''))
                if checked>snapshot:
                    errors.append(f'{name}: verification after snapshot')
            except (ValueError,TypeError):
                errors.append(f'{name}: invalid checked_on')
            if v.get('reproduced') != (v.get('level')=='reproduced'):
                errors.append(f'{name}: inconsistent reproduction claim')
        for key in seen:
            value=normalized_title(p[key]) if key=='title' else (p[key].casefold() if isinstance(p[key],str) else p[key])
            if value:
                if value in seen[key]:
                    errors.append(f'{name}: duplicate {key}: {value}')
                seen[key].add(value)
    route_ids=set()
    for route in routes:
        if not re.fullmatch(r'[a-z][a-z0-9-]*', route['id']):
            errors.append('Invalid route ID')
        if route['id'] in route_ids:
            errors.append(f"Duplicate route: {route['id']}")
        route_ids.add(route['id'])
        for paper_id in route['papers']:
            if paper_id not in seen['id']:
                errors.append(f"{route['id']}: unknown route paper {paper_id}")
    return errors

def bib_escape(value: str) -> str:
    mapping={'\\':r'\textbackslash{}','{':r'\{','}':r'\}','&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_','~':r'\textasciitilde{}','^':r'\textasciicircum{}'}
    return ''.join(mapping.get(c,c) for c in value)

def bibtex(p: dict) -> str:
    kind={'journal':'article','conference':'inproceedings','report':'techreport','chapter':'incollection'}.get(p['publication_status'],'misc')
    fields={'title':bib_escape(p['title']), 'author':' and '.join(bib_escape(a) for a in p['authors'])+(' and others' if not p['authors_complete'] else ''),'year':str(p['year'])}
    venue_key={'journal':'journal','conference':'booktitle','chapter':'booktitle','report':'institution'}.get(p['publication_status'],'howpublished')
    fields[venue_key]=bib_escape(p['venue'])
    if p['doi']: fields['doi']=p['doi']
    fields['url']=p['url']
    if p['arxiv'] and p['publication_status']=='preprint':
        fields.update({'archivePrefix':'arXiv','eprint':p['arxiv']})
    if not p['authors_complete']:
        fields['note']='Partial author metadata; verify the full author list at the primary source before manuscript submission'
    return '@'+kind+'{'+p['id']+',\n'+',\n'.join(f'  {k} = {{{v}}}' for k,v in fields.items())+'\n}\n'

def csv_text(papers: list[dict]) -> str:
    buf=io.StringIO(newline='')
    fields=['id','year','title','authors','authors_complete','venue','publication_status','category','scope','record_type','method','inputs','target_and_horizon','summary','summary_zh','region','doi','arxiv','url','code_url','checked_on']
    out=csv.DictWriter(buf,fieldnames=fields,lineterminator='\n');out.writeheader()
    for p in papers:
        row={k:p.get(k,'') for k in fields}
        row['authors']='; '.join(p['authors'])+(' et al. [incomplete metadata]' if not p['authors_complete'] else '')
        row['checked_on']=p['verification']['checked_on']
        for k,v in row.items():
            if isinstance(v,str) and v.startswith(('=','+','-','@')):row[k]="'"+v
        out.writerow(row)
    return buf.getvalue()

def filter_papers(papers: list[dict], query: str = '', category: str = '', scope: str = '') -> list[dict]:
    tokens=query.casefold().split()
    fields=['title','authors','summary','summary_zh','method','inputs','target_and_horizon','venue','region','id']
    def matches(p):
        text=' '.join(' '.join(p[k]) if isinstance(p[k],list) else str(p[k]) for k in fields).casefold()
        return all(t in text for t in tokens) and (not category or p['category']==category) and (not scope or p['scope']==scope)
    return [p for p in papers if matches(p)]
