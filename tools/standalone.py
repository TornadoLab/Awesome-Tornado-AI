"""Create a single-file, offline HTML preview with inline assets and catalog."""
from __future__ import annotations
import argparse
import base64
from pathlib import Path
from catalog import ROOT

def render(root: Path = ROOT) -> str:
    docs=root/'docs';text=(docs/'index.html').read_text(encoding='utf-8')
    text=text.replace('<link rel="stylesheet" href="style.css">','<style>\n'+(docs/'style.css').read_text(encoding='utf-8')+'\n</style>')
    favicon=base64.b64encode((docs/'favicon.svg').read_bytes()).decode('ascii')
    text=text.replace('href="favicon.svg"','href="data:image/svg+xml;base64,'+favicon+'"')
    for name in ['catalog.js','motion.js','app.js']:
        content=(docs/name).read_text(encoding='utf-8').replace('</script','<\\/script')
        text=text.replace(f'<script src="{name}"></script>','<script>\n'+content+'\n</script>')
    return text

def main() -> int:
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(render(),encoding='utf-8');print(args.output);return 0
if __name__=='__main__':raise SystemExit(main())
