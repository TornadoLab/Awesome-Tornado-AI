# Data, code and research infrastructure

These are source-linked starting points, not mirrored datasets or guarantees of unrestricted access. Read each upstream license, version, provenance and data-use policy. Inclusion does not imply independent installation or testing. “Code” may mean inference code, not a full training pipeline.

The generated [paper and code index](papers/CODE_INDEX.md) puts every verified paper/code pair in one table, including ASTRA, TornadoNet, TorViNet, TorDet, TorNet, AgentCaster, WoFSCast and HRRRCast. Code Ocean releases are labeled separately from GitHub.

## Tornado and storm datasets

| Resource | Research use | Boundary / provenance |
|---|---|---|
| [TorNet · MIT Lincoln Laboratory](https://github.com/mit-ll/tornet) | Full-resolution polarimetric radar benchmark and reference code | MIT Lincoln Laboratory authorship; preserve event/time splits and metadata; [paper record](https://journals.ametsoc.org/view/journals/aies/4/1/AIES-D-24-0006.1.xml). |
| [AgentCaster dataset](https://huggingface.co/datasets/agentcaster/agentcaster) | Context for reasoning-guided tornado forecasting | Follow the [paper](https://arxiv.org/abs/2510.03349) for regional forecasting targets; not a replacement for radar-event labels. |
| [WeatherQA](https://github.com/chengqianma/WeatherQA) | Multimodal severe-weather reasoning | Distinguish this 2024 benchmark from later datasets with reused names. |
| [RadarQA](https://github.com/hexmSeeU/RadarQA) | Radar forecast quality analysis | Not itself a tornado-occurrence dataset. |
| [NOAA NEXRAD open-data registry](https://registry.opendata.aws/noaa-nexrad/) | Raw radar archive access and format entry points | A raw observation archive, not a ready-made tornado labeling/splitting pipeline. |
| [NOAA Storm Events Database](https://www.ncei.noaa.gov/access/storm-events-database/) | Event reports and historical impacts | Reporting/metadata limitations must be audited before treating every row as ground truth. |
| [The Tornado Archive paper](https://repository.library.noaa.gov/view/noaa/69259) | Worldwide database compilation and visualization | Read the paper for cross-source harmonization and provenance. |
| [PERiLS project paper](https://repository.library.noaa.gov/view/noaa/66398) | Linear-storm evolution and rotation field campaign | A useful collection route beyond supercell-only work; use the campaign's official access instructions. |
| [European climatology / ESWD study](https://journals.ametsoc.org/view/journals/mwre/142/12/mwr-d-14-00107.1.xml) | European tornado reporting and climatology | The paper is an entry point; do not assume unrestricted download rights for underlying records. |

## Radar and meteorological tooling

| Tool | What to inspect |
|---|---|
| [Py-ART](https://arm-doe.github.io/pyart/) | Radar reading, analysis and visualization; confirm support for the specific radar format and coordinate assumptions. |
| [xradar](https://docs.openradarscience.org/projects/xradar/en/stable/) | Radar data structures and input/output workflows in the scientific Python ecosystem. |
| [MetPy](https://unidata.github.io/MetPy/latest/index.html) | Meteorological calculations and unit-aware analysis; keep units and conventions explicit. |
| [TorDet](https://github.com/Tornado-AI/TorDet) | Author-linked tornado-detection repository; inspect what is released rather than assuming the training system is complete. |
| [ProbSevere](https://cimss.ssec.wisc.edu/probsevere/ps/) | Operational/research product context; [v3 publication](https://repository.library.noaa.gov/view/noaa/67694) defines the method. |

## Adjacent weather-AI implementations

These remain **transfer/context resources**, not established tornado solutions merely because they forecast weather.

| Resource | Why follow it |
|---|---|
| [ClimaX](https://github.com/microsoft/ClimaX) | Weather/climate foundation-model transfer; [ICML paper](https://proceedings.mlr.press/v202/nguyen23a.html). |
| [Aurora](https://github.com/microsoft/aurora) | Earth-system foundation-model methodology; [Nature paper](https://www.nature.com/articles/s41586-025-09005-y). |
| [WeatherBench 2](https://github.com/google-research/weatherbench2) | Benchmark/evaluation practices for global forecasting; tornado-scale evaluation still needs separate design. |
| [Weather-R1](https://github.com/Marcowky/Weather-R1) | Meteorological reasoning and reinforcement fine-tuning; not automatically an adaptive radar-observation policy. |

## Institutional starting points

[NOAA NSSL tornado detection](https://www.nssl.noaa.gov/education/svrwx101/tornadoes/detection/) and [tornado types](https://www.nssl.noaa.gov/education/svrwx101/tornadoes/types/) are useful orientation resources, separate from peer-reviewed papers. Cite original research when making a quantitative scientific claim.

## Retrieval etiquette

Do not scrape full-text paywalls, mirror papers without permission or repeatedly hammer publisher sites. External link diagnostics are opt-in through `tools/check_links.py`; a 403, 405 or 429 response is recorded as an access/method restriction rather than proof that a source is nonexistent. The offline starter validation does not claim all external URLs were successfully fetched at runtime.
