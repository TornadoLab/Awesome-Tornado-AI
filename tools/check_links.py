"""Opt-in, serial URL diagnostics. A bot-blocked source is not necessarily a dead source."""
from __future__ import annotations
import argparse
import json
import time
import urllib.error
import urllib.request
from pathlib import Path
from catalog import load, ROOT

def main() -> int:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--network',action='store_true',help='Actually request external URLs; default only prints the queue')
    ap.add_argument('--limit',type=int,default=20)
    ap.add_argument('--output',type=Path,default=ROOT/'review'/'link-check.json')
    args=ap.parse_args()
    if args.limit<1:ap.error('--limit must be positive')
    papers,*_=load();urls=sorted({u for p in papers for u in [p['url'],p['code_url'],*p['sources']] if u})
    if not args.network:
        print('\n'.join(urls));print(f'{len(urls)} unique URLs. No requests made. Re-run with --network to check the first --limit URLs.');return 0
    results=[]
    for url in urls[:args.limit]:
        row={'url':url}
        try:
            req=urllib.request.Request(url,method='HEAD',headers={'User-Agent':'Awesome-Tornado-AI-link-check/0.1'})
            with urllib.request.urlopen(req,timeout=15) as response:row.update(status=response.status,final_url=response.url,classification='reachable')
        except urllib.error.HTTPError as exc:
            row.update(status=exc.code,classification='access-restricted-or-head-unsupported' if exc.code in {401,403,405,429} else 'manual-review')
        except (urllib.error.URLError,OSError) as exc:
            row.update(status=None,classification='network-error',detail=str(exc))
        results.append(row);print(row);time.sleep(1)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps({'checked_count':len(results),'total_queue':len(urls),'notice':'Network diagnostic only, not a scientific or availability verdict.','results':results},indent=2)+'\n',encoding='utf-8')
    return 0
if __name__=='__main__':raise SystemExit(main())
