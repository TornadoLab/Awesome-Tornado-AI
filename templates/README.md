<p align="center"><img src="assets/banner.svg" alt="Awesome Tornado AI — From the first echo to the next frontier." width="100%"></p>

<h1 align="center">🌪 Awesome Tornado AI</h1>
<p align="center"><strong>A living research atlas for understanding, detecting, rating and anticipating tornadoes.</strong><br>Physics → Radar → Statistics → Deep Learning → Multimodal Reasoning</p>
<p align="center"><a href="{{WEBSITE_URL}}">Live website</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="papers/README.md">Paper atlas</a> · <a href="guides/READING_ROUTES.md">Reading routes</a> · <a href="RESOURCES.md">Data & tools</a> · <a href="CONTRIBUTING.md">Contribute</a></p>

> **{{COUNT}} source-linked records · {{CATEGORY_COUNT}} directions · {{START_YEAR}}–{{END_YEAR}} · checked {{DATE}}**
>
> **{{ANNOTATED_COUNT}} annotated entries · {{BIBLIOGRAPHIC_COUNT}} bibliography-only entries · {{CODE_COUNT}} verified code links.** {{DIRECT_COUNT}} tornado-specific records, {{CONTEXT_COUNT}} severe-storm/operational-context records and {{TRANSFER_COUNT}} transferable weather-AI records. Retrieval is broad but not exhaustive. Metadata checking does not mean full-text review or independent experimental reproduction.

## Enter the observatory

**Browse the scholarship:** [Full catalog](papers/ALL_PAPERS.md) · [Paper + GitHub/code index](papers/CODE_INDEX.md) · [BibTeX](papers/references.bib) · [CSV](papers/catalog.csv).

**Explore the interactive atlas:** [open the website]({{WEBSITE_URL}}), open `docs/index.html` locally, or serve it with the command below. It includes search in English and Chinese, year/task-family/scope/publication/annotation filters, direct paper and code links, random paper discovery, three reading routes, a local reading list and filtered BibTeX export. It has no frontend dependencies, analytics, external fonts or live data calls.

```bash
python -m http.server 8000 --directory docs
# Open http://localhost:8000
```

The site is published on **GitHub Pages**, with HTTPS enforced, from the `main` branch's `docs/` directory. See [setup and publishing](SETUP.zh-CN.md). The decorative vortex is original vector artwork, not a measured radar field.

The vortex now rotates, sways and carries drifting particles. The site has a pause control, honors reduced-motion preferences, and pauses artwork when offscreen. The SVG banner also contains animation; hosts that suppress SVG motion show its static fallback.

**September expansion:** {{ADDED_COUNT}} additions beyond the original 67-record set. A 36-query Crossref pass (33 successful responses), individual publisher searches and a live 2026 arXiv sweep are documented in the [collection log](guides/COLLECTION_LOG.md), including exclusions, pending candidates and version merges. Bibliography-only entries have explicit pending-method fields; they are not presented as fully read papers.

## Follow the scientific question, not the model acronym

| # | Research direction | Records |
|---|---|---:|
{{CATEGORY_TABLE_EN}}

The scope deliberately includes non-AI foundations. A stronger network does not remove the need to understand a tornado vortex signature, debris signature, damage label, sampling limitation or causal forecast horizon.

## Signals worth following

| Starting point | Why it belongs here | Keep this distinction |
|---|---|---|
| [Stout & Huff, 1953](papers/radar.md#stout1953) → [Donaldson, 1970](papers/radar.md#donaldson1970) | Hook echoes and Doppler vortex recognition before modern detection algorithms | A radar signature and a confirmed tornado are different observations. |
| [Ward, 1972](papers/foundations.md#ward1972) → [Lemon & Doswell, 1979](papers/foundations.md#lemon1979) → [Lee & Wilhelmson, 1997](papers/foundations.md#lee1997b) | Laboratory vortices, supercell structure and nonsupercell tornadogenesis | Mechanisms depend on the modeled and observed storm family. |
| [Fujita, 1971](papers/rating.md#fujita1971) → [Edwards et al., 2013](papers/rating.md#edwards2013) | The damage/intensity-rating lineage | Damage-based rating is not a direct radar measurement. |
| [Brown et al., 1978](papers/radar.md#brown1978) → [NSSL TDA, 1998](papers/radar.md#mitchell1998) | Radar signatures and operational detection algorithms | A circulation signature is evidence, not an infallible tornado label. |
| [Marzban & Stumpf, 1996](papers/ml.md#marzban1996) | Neural tornado prediction predates the current deep-learning era | A title alone does not establish a forecast lead time. |
| [Lagerquist et al., 2020](papers/dl.md#lagerquist2020) | 3D multiscale inputs and next-hour tornado prediction | Specify the issue time, event definition and available inputs. |
| [TPA, 2023](papers/ml.md#sandmael2023) → [forecaster evaluation](papers/evaluation.md#sandmael2023hwt) | Probabilities and human-facing evaluation | Retrospective skill and operational usefulness are different questions. |
| [TorNet, 2025; preprint 2024](papers/data.md#tornet2025) | A full-resolution polarimetric radar benchmark | TorNet is an MIT Lincoln Laboratory dataset; not a TornadoLab product. |
| [TorDet, 2026 journal volume](papers/dl.md#tordet2025) → [TDA-DARKNet, 2026](papers/dl.md#darknet2026) → [cross-domain evaluation, 2026](papers/evaluation.md#jiang2026) | Recent radar-specific deep learning and geographic generalization | A released inference interface is not necessarily a complete training pipeline. |
| [AgentCaster, 2025](papers/agents.md#agentcaster2025) | Reasoning-guided tornado forecasting with meteorological context | Its regional 12–36 h guidance task differs from radar-event detection. |
| [Erickson et al., 2026](papers/forecast.md#erickson2026) | Explainable probabilistic radar-reflectivity nowcasting | Predicting reflectivity in tornadic storms is not predicting tornado onset. |
| [ASTRA](papers/impacts.md#umeike2026), [TornadoNet](papers/impacts.md#tornadonet2026) and [multi-stage vision-language assessment](papers/agents.md#shakya2026) | Recent post-tornado damage recognition and interpretation | Building damage states are separate from tornado occurrence and EF intensity. |

All entries link back to source records. [Wurman et al. (2021)](papers/rating.md#wurman2021) also carries its **2025 correction** in the provenance notes.

## A research compass

```text
Observe the atmosphere    Identify evidence          Ask the right question
──────────────────────    ─────────────────────      ────────────────────────────
Radar / sounding / NWP  →  Rotation, debris, storm  →  Is a tornado present now?
Satellite / lightning     structure, environment     Will one form after issue time?
Ground & damage imagery   Image or damage evidence   What intensity or damage class?
                                                     Can a model explain its evidence?
                                                     Does guidance help a forecaster?
```

Read [task definitions and evaluation](guides/TASKS.md) before comparing results. Six radar variables are not automatically six sensor modalities. EF labels are not free real-time features. A regional weather foundation model is not a demonstrated tornado detector unless tornado-specific evaluation is actually reported.

## Build and maintain

The canonical source is `data/papers.json`. Do not separately hand-edit generated paper pages, counts, CSV, BibTeX or the browser catalog.

```bash
python tools/validate.py
python tools/build.py
python tools/build.py --check
python -m unittest discover -s tests -v
node --check docs/app.js
```

New papers enter through a [source-checked contribution](CONTRIBUTING.md). The optional [arXiv scout](tools/discover_arxiv.py) only produces a human-review queue; it never silently promotes unreviewed results into the atlas. A manually triggered workflow is included. No recurring discovery is enabled by default.

```text
data/          Canonical paper records, categories, reading routes, configuration
papers/        Generated subject pages, full catalog, BibTeX and CSV
docs/          Static, accessible research explorer
assets/        Original radar/vortex identity and design notes
guides/        Task definitions, reading routes, search protocol and coverage gaps
tools/         Validate, build, discover, check links and safely install
tests/         Offline integrity, generation, discovery and installation tests
.github/       Contribution forms, CI and opt-in discovery workflow
```

## Coverage and provenance

The atlas spans early observations, vortex physics, traditional radar algorithms, intensity scales, statistical prediction, numerical simulation, machine learning, multimodal methods, wind engineering and social response. Coverage remains uneven across languages, regions and publication types; capped retrieval and bibliography-only indexing leave explicit work to do. See the [coverage backlog](guides/RESEARCH_GAPS.md) and [search protocol](guides/SEARCH_PROTOCOL.md).

Author lists follow the cited publisher or institutional metadata; unresolved authorship is flagged. Seventeen previously partial lists were completed during the first expansion. Verify publisher citation styles and later corrections before manuscript submission. Missing code links mean **not verified here**, not that no code exists. A journal label describes the publication venue, not a quality score. No paywalled PDFs are mirrored.

## Design references & acknowledgments

The structure draws inspiration from [Awesome WeatherAI](https://github.com/HeQinWill/awesome-WeatherAI), [Awesome AI4Earth](https://github.com/taohan10200/Awesome_AI4Earth), the searchable paper-database approach of [Awesome 3D Gaussian Splatting](https://github.com/MrNeRF/awesome-3D-gaussian-splatting), and the curation culture of [Awesome](https://github.com/sindresorhus/awesome). The interface, scripts, annotations and illustrations in this starter are original; third-party branding and figures are not reused.

Credit the original papers and dataset/tool authors. Use [CITATION.cff](CITATION.cff) to cite this **collection**, not in place of the research it indexes. [License scopes](LICENSE): MIT for code/site/artwork; CC BY 4.0 for original prose annotations. Third-party papers, datasets and trademarks retain their respective rights.

**This repository is for research discovery. It is not an operational warning service.**
