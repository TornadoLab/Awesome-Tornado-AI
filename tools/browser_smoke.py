"""Optional Playwright checks over local HTTP or a deployed HTTPS site, plus offline HTML.

Install Playwright separately; --chromium accepts an existing browser.
Counts and route expectations follow the canonical catalog.
"""
from __future__ import annotations
import argparse
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

            # Measure animation state over time, beyond checking CSS class names.
            flow = page.locator('.vortex-flow').first
            offset = flow.evaluate('(e)=>getComputedStyle(e).strokeDashoffset')
            page.locator('.storm-frame').screenshot(path=str(args.output/'motion-0.png'))
            page.wait_for_timeout(350)
            assert flow.evaluate('(e)=>getComputedStyle(e).strokeDashoffset') != offset
            page.locator('.storm-frame').screenshot(path=str(args.output/'motion-1.png'))
            record('Tornado flow advances between animation frames')
            page.locator('#motion-toggle').click()
            assert page.locator('#motion-toggle').get_attribute('aria-pressed') == 'true'
            page.wait_for_timeout(80)
            offset = flow.evaluate('(e)=>getComputedStyle(e).strokeDashoffset')
            page.wait_for_timeout(250)
            assert flow.evaluate('(e)=>getComputedStyle(e).strokeDashoffset') == offset
            record('Pause control freezes tornado flow')
            page.locator('#motion-toggle').click()
            page.wait_for_timeout(150)
            assert flow.evaluate('(e)=>getComputedStyle(e).strokeDashoffset') != offset
            record('Play control resumes tornado flow')
            page.evaluate('scrollTo(0,document.body.scrollHeight)')
            page.wait_for_function("document.querySelector('.hero-visual').classList.contains('motion-paused')")
            page.evaluate('scrollTo(0,0)')
            page.wait_for_function("!document.querySelector('.hero-visual').classList.contains('motion-paused')")
            record('Artwork pauses outside viewport and resumes on return')

            page.locator('#search').fill('AgentCaster')
            assert page.locator('.paper-card').count() == 1
            record('English search')
            page.locator('[data-open="agentcaster2025"]').first.click()
            assert page.locator('#paper-dialog').is_visible()
            assert '12' in page.locator('#dialog-body').inner_text()
            assert page.locator('.source-list a').count() > 0
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
            page.emulate_media(reduced_motion='reduce')
            # Chromium dispatches MediaQueryList.change asynchronously after CSS updates.
            page.wait_for_function("document.getElementById('motion-toggle').disabled")
            assert flow.evaluate('(e)=>getComputedStyle(e).animationName') == 'none'
            assert page.locator('.radar-sweep').evaluate('(e)=>getComputedStyle(e).animationName') == 'none'
            assert page.locator('#motion-toggle').is_disabled()
            record('Reduced motion stops vortex and sweep')

            mobile = browser.new_context(viewport={'width':390, 'height':844}, device_scale_factor=1,
                                         is_mobile=True, has_touch=True, reduced_motion='reduce')
            mp = mobile.new_page()
            observe(mp)
            mp.goto(origin, wait_until='networkidle')
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
            record('390 px mobile search and detail dialog without overflow')
            mp.keyboard.press('Escape')
            mp.set_viewport_size({'width':320, 'height':700})
            assert mp.evaluate('document.documentElement.scrollWidth <= innerWidth')
            record('320 px narrow viewport without overflow')

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
