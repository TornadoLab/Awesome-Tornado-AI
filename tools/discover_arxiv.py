"""Find arXiv candidates, never auto-admit papers. Network access is opt-in by execution."""
from __future__ import annotations
import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date, timedelta
from pathlib import Path
from catalog import ROOT, load, normalized_title

ATOM={'a':'http://www.w3.org/2005/Atom','o':'http://a9.com/-/spec/opensearch/1.1/'}
ENDPOINT='https://export.arxiv.org/api/query'

def parse_feed(raw: bytes, known_ids: set[str], known_titles: set[str]) -> tuple[list[dict],int]:
    if len(raw)>4_000_000 or b'<!DOCTYPE' in raw.upper():
        raise ValueError('Feed too large or contains a document type declaration')
    root=ET.fromstring(raw)
    total=int(root.findtext('o:totalResults','0',ATOM))
    candidates=[];seen=set(known_ids);titles=set(known_titles)
    for entry in root.findall('a:entry',ATOM):
        entry_id=entry.findtext('a:id','',ATOM)
        if '/api/errors' in entry_id:
            raise ValueError('arXiv API error: '+entry.findtext('a:summary','unknown',ATOM))
        match=re.search(r'/abs/([^/]+?)(?:v\d+)?$',entry_id)
        if not match:continue
        arxiv=match.group(1)
        title=' '.join(entry.findtext('a:title','',ATOM).split())
        normalized=normalized_title(title)
        if arxiv in seen or normalized in titles:continue
        seen.add(arxiv);titles.add(normalized)
        candidates.append({'arxiv':arxiv,'title':title,
          'authors':[' '.join(x.findtext('a:name','',ATOM).split()) for x in entry.findall('a:author',ATOM)],
          'first_submitted':entry.findtext('a:published','',ATOM),
          'updated':entry.findtext('a:updated','',ATOM),
          'url':'https://arxiv.org/abs/'+arxiv,'review_status':'unreviewed',
          'required_review':['Confirm tornado relevance and scope','Check publication and corrections','Verify title, complete authors and original sources','Read task, inputs and horizon','Write original annotations; do not copy abstracts']})
    return candidates,total

def request_feed(url: str) -> bytes:
    request=urllib.request.Request(url,headers={'User-Agent':'Awesome-Tornado-AI/0.1 (research bibliography; https://github.com/TornadoLab/Awesome-Tornado-AI)','Accept':'application/atom+xml'})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request,timeout=20) as response:
                return response.read(4_000_001)
        except urllib.error.HTTPError as exc:
            if exc.code not in {429,500,502,503,504} or attempt==2:raise
        except urllib.error.URLError:
            if attempt==2:raise
        time.sleep(3*(attempt+1))
    raise RuntimeError('Unreachable retry state')

def main() -> int:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--since',default=(date.today()-timedelta(days=30)).isoformat())
    ap.add_argument('--until',default=date.today().isoformat())
    ap.add_argument('--max-results',type=int,default=100)
    ap.add_argument('--output',type=Path,default=ROOT/'review'/'candidates.json')
    ap.add_argument('--fixture',type=Path,help='Parse a local Atom fixture without network access')
    args=ap.parse_args()
    try:
        since,until=date.fromisoformat(args.since),date.fromisoformat(args.until)
        if since>until:raise ValueError('--since must not be after --until')
        if not 1<=args.max_results<=200:raise ValueError('--max-results must be 1..200; split large searches into date windows')
        query=f'(ti:tornado OR abs:tornado OR ti:tornadic OR abs:tornadic) AND submittedDate:[{since:%Y%m%d}0000 TO {until:%Y%m%d}2359]'
        url=ENDPOINT+'?'+urllib.parse.urlencode({'search_query':query,'start':0,'max_results':args.max_results,'sortBy':'submittedDate','sortOrder':'descending'})
        papers,*_=load()
        raw=args.fixture.read_bytes() if args.fixture else request_feed(url)
        candidates,total=parse_feed(raw,{p['arxiv'] for p in papers if p['arxiv']},{normalized_title(p['title']) for p in papers})
        payload={'mode':'offline_fixture' if args.fixture else 'arxiv_api','query':query,'query_url':url,
                 'since':str(since),'until':str(until),'total_api_results':total,
                 'requested_limit':args.max_results,'possibly_truncated':total>args.max_results,
                 'notice':'CANDIDATES ONLY. Human source review required. Not a comprehensive journal search. No full abstracts are copied.',
                 'candidates':candidates}
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        print(f'{len(candidates)} unreviewed candidates written to {args.output}. Formal catalog unchanged.')
        if payload['possibly_truncated']:print('WARNING: Narrow the date window; the API result set exceeds the requested limit.')
        return 0
    except (OSError,ValueError,ET.ParseError,urllib.error.URLError) as exc:
        print(f'Discovery failed; no catalog entries added: {exc}',file=sys.stderr);return 1
if __name__=='__main__':raise SystemExit(main())
