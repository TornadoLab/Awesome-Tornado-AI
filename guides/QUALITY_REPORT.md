# Delivery checks — 2026-09-29

## Verified locally

| Check | Result |
|---|---|
| Canonical catalog integrity | 930 records, 15 populated directions; required fields, IDs, normalized titles, DOI/arXiv duplication, date/status/scope consistency, routes and provenance URL syntax passed. |
| Deterministic generation | 26 generated files match canonical JSON, templates and original artwork. Includes both READMEs, topic pages, paper/code index, BibTeX, CSV and browser data. |
| Offline regression suite | 32 tests run on Windows/Python 3.14: 31 passed; one symlink-creation case skipped because Windows denied the required privilege. The case remains enabled on Linux CI. |
| JavaScript syntax | `node --check` passed for app, generated catalog and motion controls. |
| Real browser interaction | 31 checks passed with installed Chrome/Playwright over a real loopback HTTP server plus a standalone offline page; no JavaScript errors or failed asset requests. |
| Motion behavior | Measured advancing flow between frames, freeze/resume from the control, offscreen pause/resume and reduced-motion behavior. Media-query event checks wait for the actual asynchronous state change. |
| Search and exports | English/Chinese search; topic/scope/year/status/entry-detail/code filters; direct code links; route order; random discovery; incremental loading; actual downloaded BibTeX matched all filtered records. |
| Reading list and accessibility | Same-origin reload preserved the reading list and URL filters; blocked storage retained session functionality; dialog dismissal, keyboard search and empty state worked. |
| Layout | Desktop 1440 × 1200 and mobile 390 × 844 / 320 px rendered without horizontal page overflow. Original artwork and rendered screenshots inspected. |
| Network-backed research | Live arXiv and Crossref retrieval/screening are recorded in the collection audits; three Crossref query families failed with HTTP 429 and remain documented. |
| Code destinations | 19 GitHub repositories responded successfully via the public API. NowcastNet's author-linked DOI resolved to Code Ocean but its automated retrieval returned HTTP 403. This is not a code-execution test. |
| GitHub access | SSH authenticated as `DerongDeng-dero`, with push permission to the specified private repository. Before first publication, the remote had no branches. GitHub Pages was not enabled. |

## Boundaries

The [collection log](COLLECTION_LOG.md) separates the 163 method-annotated entries from the 767 bibliography-only records. All current scientific evidence levels are `metadata`; no experiments were independently reproduced. A schema/CI pass does not validate scientific results, comprehensive retrieval, every publication's current correction/retraction status, or every external URL's availability.

Browser validation covers actual local HTTP, localStorage persistence and offline HTML. It is not a GitHub Pages deployment test. There is no claimed public website deployment. Remote CI results should be read from the repository Actions page for the relevant commit, rather than inferred from local tests.

## Re-run

```bash
python tools/validate.py
python tools/build.py --check
python -m unittest discover -s tests -v
node --check docs/app.js
node --check docs/catalog.js
node --check docs/motion.js
```

Optional browser checks require Playwright and Chromium, neither of which is a dependency of the published site:

```bash
python -m pip install playwright
python -m playwright install chromium
python tools/browser_smoke.py
# Or use an existing browser:
# python tools/browser_smoke.py --chromium /path/to/chromium
```

The smoke script derives paper counts and route membership from the canonical catalog. Browser evidence is written to the ignored `review/browser/` directory; downloaded metadata, raw source pages and local tooling under `review/` are not part of the published repository. See [setup](../SETUP.zh-CN.md) for preview and optional deployment.
