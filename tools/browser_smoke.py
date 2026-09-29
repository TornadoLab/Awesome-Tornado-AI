"""Optional Playwright checks over local HTTP or a deployed HTTPS site, plus offline HTML.

Install Playwright separately; --chromium accepts an existing browser.
Counts and route expectations follow the canonical catalog.
"""
from __future__ import annotations
import argparse
import base64
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import threading

from playwright.sync_api import sync_playwright
from catalog import ROOT, load, safe_url
from standalone import render


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_):
        pass


def changed_pixels(page, before: bytes, after: bytes) -> float:
    """Compare rendered PNG pixels, without needing an image-library dependency."""
    frames = ['data:image/png;base64,' + base64.b64encode(b).decode('ascii')
              for b in (before, after)]
    return page.evaluate('''async frames => {
      const images = await Promise.all(frames.map(src => new Promise((resolve, reject) => {
        const image = new Image();
        image.onload = () => resolve(image); image.onerror = reject; image.src = src;
      })));
      const canvas = document.createElement('canvas');
      canvas.width = images[0].width; canvas.height = images[0].height;
      const ctx = canvas.getContext('2d', {willReadFrequently:true});
      const pixels = images.map(image => {
        ctx.clearRect(0, 0, canvas.width, canvas.height); ctx.drawImage(image, 0, 0);
        return ctx.getImageData(0, 0, canvas.width, canvas.height).data;
      });
      let changed = 0;
      for (let i = 0; i < pixels[0].length; i += 4) {
        if ([0,1,2].some(c => Math.abs(pixels[0][i+c] - pixels[1][i+c]) > 12)) changed++;
      }
      return changed / (canvas.width * canvas.height);
    }''', frames)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--chromium', help='Installed Chromium executable; defaults to Playwright Chromium')
    parser.add_argument('--url', help='Test a deployed HTTPS site instead of starting local HTTP')
    parser.add_argument('--output', type=Path, default=ROOT/'review'/'browser')
    args = parser.parse_args()
    if args.url and not safe_url(args.url):
        parser.error('--url must be an HTTPS URL without embedded credentials')
    args.output.mkdir(parents=True, exist_ok=True)
    papers, _, _, routes = load()
    total = len(papers)
    checks, errors, failed_requests = [], [], []

    def record(name):
        checks.append(name)
        print('PASS', name, flush=True)

    def observe(page):
        page.on('pageerror', lambda e: errors.append(str(e)))
        page.on('requestfailed', lambda r: failed_requests.append(r.url))
        page.on('response', lambda r: failed_requests.append(f'{r.status} {r.url}') if r.status >= 400 else None)
        page.on('console', lambda m: errors.append(m.text) if m.type == 'error' else None)

    server = thread = None
    if args.url:
        origin = args.url
    else:
        server = ThreadingHTTPServer(('127.0.0.1', 0), partial(QuietHandler, directory=str(ROOT/'docs')))
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        origin = f'http://127.0.0.1:{server.server_port}/'
    try:
        with sync_playwright() as pw:
            browser = pw.chromium.launch(executable_path=args.chromium, headless=True)
            ctx = browser.new_context(viewport={'width':1440, 'height':1200}, device_scale_factor=1,
                                      accept_downloads=True, reduced_motion='no-preference')
            page = ctx.new_page()
            observe(page)
            response = page.goto(origin, wait_until='networkidle')
            assert response and response.ok, f'Page load failed: {origin}'
            assert page.locator('#stat-count').inner_text() == str(total)
            assert page.locator('.paper-card').count() == min(12, total)
            record('HTTP(S) desktop render with catalog-derived counts')
            assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
            record('Desktop: no horizontal overflow')
            page.screenshot(path=str(args.output/'desktop.png'))

            # Compare actual artwork pixels with the radar hidden: changing CSS values
            # or a moving radar alone must not pass a test for a moving tornado.
            flow = page.locator('.vortex-flow').first
            frame = page.locator('.storm-frame')
            page.locator('.radar-sweep').evaluate("e=>e.style.visibility='hidden'")
            offset = flow.evaluate('(e)=>getComputedStyle(e).strokeDashoffset')
            before = frame.screenshot(path=str(args.output/'motion-0.png'), animations='allow')
            page.wait_for_timeout(600)
            assert flow.evaluate('(e)=>getComputedStyle(e).strokeDashoffset') != offset
            after = frame.screenshot(path=str(args.output/'motion-1.png'), animations='allow')
            assert changed_pixels(page, before, after) > .005
            record('Tornado visibly changes rendered pixels with the radar hidden')
            page.locator('#motion-toggle').click()
            assert page.locator('#motion-toggle').get_attribute('aria-pressed') == 'true'
            page.wait_for_timeout(80)
            offset = flow.evaluate('(e)=>getComputedStyle(e).strokeDashoffset')
            before = frame.screenshot(animations='allow')
            page.wait_for_timeout(250)
            assert flow.evaluate('(e)=>getComputedStyle(e).strokeDashoffset') == offset
            assert changed_pixels(page, before, frame.screenshot(animations='allow')) == 0
            record('Pause control freezes tornado flow')
            page.locator('#motion-toggle').click()
            page.wait_for_timeout(150)
            assert flow.evaluate('(e)=>getComputedStyle(e).strokeDashoffset') != offset
            record('Play control resumes tornado flow')
            page.locator('.radar-sweep').evaluate("e=>e.style.removeProperty('visibility')")
            page.evaluate('scrollTo(0,document.body.scrollHeight)')
            page.wait_for_function("document.querySelector('.hero-visual').classList.contains('motion-paused')")
            page.evaluate('scrollTo(0,0)')
            page.wait_for_function("!document.querySelector('.hero-visual').classList.contains('motion-paused')")
            record('Artwork pauses outside viewport and resumes on return')

            page.locator('#collection').evaluate("e=>e.scrollIntoView({block:'start',behavior:'instant'})")
            page.screenshot(path=str(args.output/'desktop-collection.png'))
            page.locator('#search').fill('AgentCaster')
            assert page.locator('.paper-card').count() == 1
            record('English search')
            page.locator('[data-open="agentcaster2025"]').first.click()
            assert page.locator('#paper-dialog').is_visible()
            assert '12' in page.locator('#dialog-body').inner_text()
            assert page.locator('.source-list a').count() > 0
            page.screenshot(path=str(args.output/'desktop-dialog.png'))
            record('Paper dialog includes horizon and primary provenance')
            page.keyboard.press('Escape')
            assert not page.locator('#paper-dialog').is_visible()
            record('Keyboard dialog dismissal')
            page.locator('#papers [data-save="agentcaster2025"]').click()
            assert page.locator('#saved-count').inner_text() == '1'
            page.reload(wait_until='networkidle')
            assert page.locator('#saved-count').inner_text() == '1'
            assert page.locator('#search').input_value() == 'AgentCaster'
            record('Reading list and URL search persist across same-origin reload')
            page.locator('#clear-filters').click()
            page.locator('#saved-toggle').click()
            assert page.locator('.paper-card').count() == 1
            record('Saved reading-list filtering')
            page.locator('#clear-filters').click()
            page.locator('#search').fill('雷达')
            assert page.locator('.paper-card').count() > 0
            record('Chinese annotation search')
            page.locator('#clear-filters').click()
            page.locator('#scope').select_option('transfer')
            transfers = sum(p['scope']=='transfer' for p in papers)
            assert page.locator('#result-count').inner_text().startswith(f'{transfers} ')
            assert set(page.locator('.paper-bottom .scope').all_text_contents()) == {'transfer'}
            record('Transfer scope remains separate from tornado-specific evidence')
            page.locator('#clear-filters').click()
            page.locator('[data-category="rating"]').click()
            assert page.locator('.paper-card').count() > 0
            assert page.evaluate("[...document.querySelectorAll('.paper-card')].every(e=>TORNADO_CATALOG.papers.find(p=>p.id===e.dataset.id).category==='rating')")
            record('Research-direction filter')
            page.locator('#clear-filters').click()
            page.locator('#curation').select_option('bibliographic')
            bibliography_count = sum(p['record_type']=='bibliographic' for p in papers)
            assert page.locator('#result-count').inner_text().startswith(f'{bibliography_count} ')
            page.locator('#papers [data-open]').first.click()
            assert 'Not extracted' in page.locator('#dialog-body').inner_text()
            assert 'Code repository: not verified' in page.locator('#dialog-body').inner_text()
            page.keyboard.press('Escape')
            page.reload(wait_until='networkidle')
            assert page.locator('#curation').input_value() == 'bibliographic'
            assert page.locator('#result-count').inner_text().startswith(f'{bibliography_count} ')
            record('Bibliographic filter, pending-method disclosure and reload persistence')
            page.locator('#curation').select_option('annotated')
            annotated_count = sum(p['record_type']=='annotated' for p in papers)
            assert page.locator('#result-count').inner_text().startswith(f'{annotated_count} ')
            page.locator('#clear-filters').click()
            assert page.locator('#curation').input_value() == ''
            record('Annotated filter and reset preserve entry-detail distinction')
            newest = str(max(p['year'] for p in papers))
            page.locator('#year').select_option(newest)
            page.locator('#status').select_option('preprint')
            assert page.locator('.paper-card').count() > 0
            assert set(page.locator('.paper-meta .year').all_text_contents()) == {newest}
            record('Combined year and publication-status filters')
            page.locator('#clear-filters').click()
            page.locator('#code-only').check()
            assert page.locator('.paper-card').count() > 0
            assert page.evaluate("[...document.querySelectorAll('.paper-card')].every(e=>!!TORNADO_CATALOG.papers.find(p=>p.id===e.dataset.id).code_url)")
            assert page.evaluate("[...document.querySelectorAll('.paper-card')].every(e=>[...e.querySelectorAll('.paper-links a')].some(a=>a.href===TORNADO_CATALOG.papers.find(p=>p.id===e.dataset.id).code_url))")
            record('Author-linked code filter')
            with page.expect_download() as downloaded:
                page.locator('#export-bib').click()
            download = downloaded.value
            assert download.suggested_filename == 'tornadolab-filtered.bib'
            target = args.output/'export.bib'
            download.save_as(str(target))
            exported = target.read_text(encoding='utf-8')
            for paper in papers:
                assert (f"{paper['id']}," in exported) == bool(paper['code_url'])
            record('Downloaded BibTeX matches the entire filtered set')
            page.locator('#clear-filters').click()
            page.locator('#sort').select_option('oldest')
            assert page.locator('.paper-meta .year').first.inner_text() == str(min(p['year'] for p in papers))
            record('Chronological ordering reaches the earliest catalog paper')
            page.locator('#clear-filters').click()
            page.locator('#load-more').click()
            assert page.locator('.paper-card').count() == min(24, total)
            record('Progressive loading')
            for route in routes:
                page.locator(f'[data-route="{route["id"]}"]').click()
                actual = page.locator('.paper-card').evaluate_all('(es)=>es.map(e=>e.dataset.id)')
                assert actual == route['papers'][:12]
            record('Every reading route preserves its editorial order')
            page.locator('#random-hero').click()
            assert page.locator('#paper-dialog').is_visible()
            page.locator('#close-dialog').click()
            record('Random paper discovery')
            page.locator('#clear-filters').click()
            page.locator('#search').fill('no-match-fixture-9283492834')
            assert page.locator('.empty-state').is_visible()
            assert page.locator('#export-bib').is_disabled()
            record('Empty state and disabled empty export')
            page.locator('#clear-filters').click()
            page.locator('#search').blur()
            page.keyboard.press('/')
            assert page.locator('#search').evaluate('(e)=>e===document.activeElement')
            record('Search keyboard shortcut')
            page.evaluate("scrollTo({top:0,behavior:'instant'})")
            page.emulate_media(reduced_motion='reduce')
            # Chromium dispatches MediaQueryList.change asynchronously after CSS updates.
            page.wait_for_function("document.getElementById('motion-toggle').getAttribute('aria-pressed') === 'true'")
            assert flow.evaluate('(e)=>getComputedStyle(e).animationPlayState') == 'paused'
            assert page.locator('.radar-sweep').evaluate('(e)=>getComputedStyle(e).animationPlayState') == 'paused'
            assert page.locator('#motion-toggle').is_enabled()
            record('Reduced motion pauses vortex and sweep with Play still available')
            page.locator('#motion-toggle').click()
            offset = flow.evaluate('(e)=>getComputedStyle(e).strokeDashoffset')
            page.wait_for_timeout(350)
            assert flow.evaluate('(e)=>getComputedStyle(e).strokeDashoffset') != offset
            assert page.locator('.radar-sweep').evaluate('(e)=>getComputedStyle(e).animationPlayState') == 'running'
            record('Explicit Play overrides reduced-motion default for both animations')
            page.locator('#motion-toggle').click()
            page.evaluate("scrollTo({top:document.body.scrollHeight,behavior:'instant'})")
            page.wait_for_timeout(100)
            page.evaluate("scrollTo({top:0,behavior:'instant'})")
            page.wait_for_timeout(100)
            assert flow.evaluate('(e)=>getComputedStyle(e).animationPlayState') == 'paused'
            record('Manual pause survives leaving and returning to the viewport')
            page.emulate_media(reduced_motion='no-preference')
            page.wait_for_function("!document.querySelector('.hero-visual').classList.contains('motion-paused')")
            record('Changing the system motion preference updates playback')

            for width in (1440, 1100, 820, 760, 390, 320):
                page.set_viewport_size({'width':width, 'height':1000})
                assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'), width
                sizes = page.evaluate('''() => Object.fromEntries(
                  ['.paper-card h3','.paper-summary','#search','.filters select','.text-button',
                   '.category-button','.paper-meta'].map(s => [s,parseFloat(getComputedStyle(document.querySelector(s)).fontSize)]))''')
                assert sizes['.paper-card h3'] >= 20, sizes
                assert sizes['.paper-meta'] >= 13, sizes
                assert all(value >= 16 for key, value in sizes.items() if key != '.paper-meta'), sizes
            record('Larger reading and control text without overflow at six viewport widths')

            mobile = browser.new_context(viewport={'width':390, 'height':844}, device_scale_factor=1,
                                         is_mobile=True, has_touch=True, reduced_motion='reduce')
            mp = mobile.new_page()
            observe(mp)
            mp.goto(origin, wait_until='networkidle')
            assert mp.locator('#motion-toggle').is_enabled()
            assert mp.locator('.vortex-flow').first.evaluate('(e)=>getComputedStyle(e).animationPlayState') == 'paused'
            assert mp.evaluate('document.documentElement.scrollWidth <= innerWidth')
            mp.screenshot(path=str(args.output/'mobile.png'), full_page=True)
            mp.screenshot(path=str(args.output/'mobile-viewport.png'))
            mp.locator('#search').evaluate("(e)=>e.scrollIntoView({block:'start',behavior:'instant'})")
            mp.screenshot(path=str(args.output/'mobile-filters.png'))
            mp.locator('#search').fill('TorNet')
            assert mp.locator('.paper-card').count() >= 1
            mp.locator('#papers [data-open]').first.click()
            assert mp.locator('#paper-dialog').is_visible()
            assert mp.evaluate('document.documentElement.scrollWidth <= innerWidth')
            mp.screenshot(path=str(args.output/'mobile-dialog.png'))
            record('390 px mobile search and detail dialog without overflow')
            mp.keyboard.press('Escape')
            mp.set_viewport_size({'width':320, 'height':700})
            assert mp.evaluate('document.documentElement.scrollWidth <= innerWidth')
            record('320 px narrow viewport without overflow')
            mp.locator('#motion-toggle').click()
            mp.locator('.storm-frame').scroll_into_view_if_needed()
            mf = mp.locator('.vortex-flow').first
            offset = mf.evaluate('(e)=>getComputedStyle(e).strokeDashoffset')
            mp.wait_for_timeout(350)
            assert mf.evaluate('(e)=>getComputedStyle(e).strokeDashoffset') != offset
            mp.locator('.hero-visual').screenshot(path=str(args.output/'mobile-tornado.png'))
            record('Mobile reduced-motion visitor can explicitly play the tornado')

            blocked = browser.new_context(reduced_motion='reduce')
            bp = blocked.new_page()
            observe(bp)
            bp.add_init_script("Object.defineProperty(window,'localStorage',{get(){throw new DOMException('Blocked','SecurityError')}})")
            bp.goto(origin, wait_until='networkidle')
            bp.locator('#search').fill('AgentCaster')
            bp.locator('#papers [data-save="agentcaster2025"]').click()
            bp.locator('#saved-toggle').click()
            assert bp.locator('.paper-card').count() == 1
            assert bp.locator('#saved-count').inner_text() == '1'
            record('Blocked storage retains a working session reading list')

            offline = browser.new_context(reduced_motion='reduce')
            op = offline.new_page()
            observe(op)
            requests = []
            op.on('request', lambda r: requests.append(r.url))
            op.set_content(render(), wait_until='load')
            assert op.locator('#stat-count').inner_text() == str(total)
            op.locator('#search').fill('Stout')
            assert op.locator('.paper-card').count() >= 1
            assert not [u for u in requests if u.startswith(('http:', 'https:'))]
            record('Standalone HTML renders and searches without external requests')
            assert not errors, errors
            assert not failed_requests, failed_requests
            record('No JavaScript console errors or failed asset requests')
            browser.close()
    finally:
        if server:
            server.shutdown()
            server.server_close()
            thread.join(timeout=2)
    (args.output/'results.json').write_text(json.dumps({
        'mode':'remote HTTPS plus standalone HTML' if args.url else 'loopback HTTP plus standalone HTML',
        'origin':origin, 'checks':checks, 'count':len(checks),
        'catalog_records':total, 'errors':errors, 'failed_requests':failed_requests
    }, indent=2)+'\n', encoding='utf-8')


if __name__ == '__main__':
    main()
