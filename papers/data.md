# Datasets & benchmarks

数据集与基准 · 10 records · snapshot 2026-09-29

[Back to the catalog](README.md) · [Scope and evaluation](../guides/TASKS.md)

<a id="chen2026xwod"></a>
### 2026 · XWOD: A Real-World Benchmark for Object Detection under Extreme Weather Conditions

Chih-Hsin Chen; Yu-Tung Liu; Amar Fadillah; Kuan-Ting Lai; Dong Liu · *arXiv* · **preprint** · `context` · `annotated`

Introduces a traffic-object benchmark whose weather taxonomy includes tornado scenes, useful for separating weather robustness from tornado recognition.

发布包含龙卷场景标签的恶劣天气交通目标检测基准，可用于研究灾害环境中的视觉鲁棒性。

- **Method / input:** Extreme-weather traffic-object detection benchmark / Real-world traffic images labeled with weather conditions, including tornadoes.
- **Target & horizon:** Detection of road users and vehicles in adverse-weather imagery.
- **Reading caution:** Preprint; targets are traffic objects, not tornado boxes, radar signatures or EF intensity labels. Aggregate transfer results are not tornado detection accuracy. Metadata/abstract-level review; experiments not independently reproduced.
- **Provenance:** metadata checked 2026-09-29; independently reproduced: false.

[Primary source](https://arxiv.org/abs/2605.11521) · [arXiv](https://arxiv.org/abs/2605.11521)

Code availability: not verified in this snapshot.

---

<a id="tornet2025"></a>
### 2025 · A Benchmark Dataset for Tornado Detection and Prediction using Full-Resolution Polarimetric Weather Radar Data

Mark S. Veillette; James M. Kurdzo; Phillip M. Stepanian; John Y. N. Cho; Tony Reis; Siddharth Samsi; Joseph McDonald; Nicholas Chisler · *Artificial Intelligence for the Earth Systems* · **journal** · `direct` · `annotated`

TorNet provides an open radar benchmark and baseline from MIT Lincoln Laboratory.

MIT Lincoln Laboratory 的开放雷达数据集与基线；为可复现的龙卷检测研究提供入口。

- **Method / input:** Dataset and CNN baseline / Full-resolution polarimetric weather radar.
- **Target & horizon:** Tornado detection benchmark; prediction extensions.
- **Reading caution:** TorNet belongs to MIT Lincoln Laboratory, not TornadoLab. Six radar fields are six variables, not six independent sensing modalities. The original benchmark baseline is chiefly detection; a forecasting claim needs explicit causal lead-time evaluation.
- **Provenance:** metadata checked 2026-09-29; independently reproduced: false.

[Primary source](https://journals.ametsoc.org/view/journals/aies/4/1/AIES-D-24-0006.1.xml) · [DOI](https://doi.org/10.1175/AIES-D-24-0006.1) · [arXiv](https://arxiv.org/abs/2401.16437) · [Author-linked code](https://github.com/mit-ll/tornet) · [Evidence 2](https://arxiv.org/html/2401.16437v1) · [Evidence 3](https://github.com/mit-ll/tornet) · [Evidence 4](https://api.crossref.org/works/10.1175%2Faies-d-24-0006.1)

Code availability: author-linked release above.

---

<a id="ref-b626e3bbb251"></a>
### 2025 · KANs Layer Integration: Benchmarking Deep Learning Architectures for Tornado Prediction

Shuo (Luna) Yang; Ehsaneh Vilataj; Muhammad Faizan Raza; Satish Mahadevan Srinivasan · *Big Data and Cognitive Computing* · **journal** · `direct` · `bibliographic`

书目与主题已核对；方法、输入、时间窗及结果待阅读原文。Bibliographic record; detailed study annotation pending.

Bibliographic identity and topical relevance reviewed from the cited publisher-deposited Crossref record. Methods, input data, forecast horizon, results and full text have not been extracted or independently verified. Code availability has not been established for this entry.

[Primary source](https://doi.org/10.3390/bdcc9120324) · [DOI](https://doi.org/10.3390/bdcc9120324) · [Evidence 2](https://api.crossref.org/works/10.3390%2Fbdcc9120324)

Code availability: not verified in this snapshot.

---

<a id="maas2024"></a>
### 2024 · The Tornado Archive: Compiling and Visualizing a Worldwide, Digitized Tornado Database

Malcolm Maas; Timothy Supinie; Andrew Berrington; Samuel Emmerson; Ava Aidala; Michael Gavan · *Bulletin of the American Meteorological Society* · **journal** · `direct` · `annotated`

A reference for reconciling heterogeneous tornado records across the world.

全球龙卷事件汇编与可视化，为事件去重、来源追踪和跨区域数据整理提供参考。

- **Method / input:** Global data curation and visualization / Multi-source tornado reports.
- **Target & horizon:** Worldwide event archive.
- **Reading caution:** Bibliographic/abstract-level seed annotation; full-text methods, splits and performance have not been independently audited.
- **Provenance:** metadata checked 2026-09-29; independently reproduced: false.

[Primary source](https://repository.library.noaa.gov/view/noaa/69259) · [DOI](https://doi.org/10.1175/BAMS-D-23-0123.1)

Code availability: not verified in this snapshot.

---

<a id="weatherbench22024"></a>
### 2024 · WeatherBench 2: A Benchmark for the Next Generation of Data-Driven Global Weather Models

Stephan Rasp; Stephan Hoyer; Alexander Merose; Ian Langmore; Peter Battaglia; Tyler Russell; Alvaro Sanchez‐Gonzalez; Vivian Yang; Rob Carver; Shreya Agrawal; Matthew Chantry; Zied Ben Bouallegue; Peter Dueben; Carla Bromberg; Jared Sisk; Luke Barrington; Aaron Bell; Fei Sha · *Journal of Advances in Modeling Earth Systems* · **journal** · `transfer` · `annotated`

Read for metric design, baselines and reproducible forecast comparison.

学习多指标、强基线与可复现比较，不把全球天气榜单当作龙卷模型榜单。

- **Method / input:** Multi-metric forecast benchmark / Global forecasts and reference fields.
- **Target & horizon:** Medium-range global forecasting evaluation.
- **Reading caution:** Bibliographic/abstract-level seed annotation; full-text methods, splits and performance have not been independently audited.
- **Provenance:** metadata checked 2026-09-29; independently reproduced: false.

[Primary source](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2023MS004019) · [DOI](https://doi.org/10.1029/2023MS004019) · [arXiv](https://arxiv.org/abs/2308.15560) · [Author-linked code](https://github.com/google-research/weatherbench2) · [Evidence 2](https://api.crossref.org/works/10.1029%2F2023ms004019)

Code availability: author-linked release above.

---

<a id="ref-37449ae127d8"></a>
### 2021 · Performance Benchmarking of Parallel Hyperparameter Tuning for Deep Learning Based Tornado Predictions

Jonathan N. Basalyga; Carlos A. Barajas; Matthias K. Gobbert; Jianwu Wang · *Big Data Research* · **journal** · `direct` · `bibliographic`

书目与主题已核对；方法、输入、时间窗及结果待阅读原文。Bibliographic record; detailed study annotation pending.

Bibliographic identity and topical relevance reviewed from the cited publisher-deposited Crossref record. Methods, input data, forecast horizon, results and full text have not been extracted or independently verified. Code availability has not been established for this entry.

[Primary source](https://doi.org/10.1016/j.bdr.2021.100212) · [DOI](https://doi.org/10.1016/j.bdr.2021.100212) · [Evidence 2](https://api.crossref.org/works/10.1016%2Fj.bdr.2021.100212)

Code availability: not verified in this snapshot.

---

<a id="weatherbench2020"></a>
### 2020 · WeatherBench: A benchmark data set for data-driven weather forecasting

Stephan Rasp; Peter D. Dueben; Sebastian Scher; Jonathan A. Weyn; Soukayna Mouatadid; Nils Thuerey · *Journal of Advances in Modeling Earth Systems* · **journal** · `transfer` · `annotated`

A benchmark-design reference, not a tornado dataset.

学习公开基准、数据划分与基线设计；它不是龙卷数据集。

- **Method / input:** Benchmark design / Global reanalysis fields.
- **Target & horizon:** Global weather forecasting evaluation.
- **Reading caution:** Bibliographic/abstract-level seed annotation; full-text methods, splits and performance have not been independently audited.
- **Provenance:** metadata checked 2026-09-29; independently reproduced: false.

[Primary source](https://doi.org/10.1029/2020MS002203) · [DOI](https://doi.org/10.1029/2020MS002203) · [arXiv](https://arxiv.org/abs/2002.00469) · [Author-linked code](https://github.com/pangeo-data/WeatherBench) · [Evidence 2](https://arxiv.org/html/2401.16437v1) · [Evidence 3](https://github.com/pangeo-data/WeatherBench)

Code availability: author-linked release above.

---

<a id="vortex2012"></a>
### 2012 · The Second Verification of the Origins of Rotation in Tornadoes Experiment: VORTEX2

Joshua Wurman; David Dowell; Yvette Richardson; Paul Markowski; Erik Rasmussen; Donald Burgess; Louis Wicker; Howard B. Bluestein · *Bulletin of the American Meteorological Society* · **journal** · `direct` · `annotated`

Documents the VORTEX2 campaign design and its coordinated observations of tornadoes, parent storms and near-storm environments.

介绍VORTEX2多平台外场试验及其对龙卷、母体风暴和环境的协同观测，补充基准数据背后的观测来源。

- **Method / input:** Multi-platform field-campaign overview / Mobile radars, mesonets, soundings, photography and damage surveys.
- **Target & horizon:** Observation of tornado formation, maintenance and decay.
- **Reading caution:** A field-campaign overview is not a single harmonized machine-learning dataset. Metadata/abstract-level review; experiments not independently reproduced.
- **Provenance:** metadata checked 2026-09-29; independently reproduced: false.

[Primary source](https://doi.org/10.1175/bams-d-11-00010.1) · [DOI](https://doi.org/10.1175/bams-d-11-00010.1) · [Evidence 2](https://api.crossref.org/works/10.1175%2Fbams-d-11-00010.1)

Code availability: not verified in this snapshot.

---

<a id="ref-79ea4a2ad277"></a>
### 2006 · Evolution of the U.S. Tornado Database: 1954–2003

Stephanie M. Verbout; Harold E. Brooks; Lance M. Leslie; David M. Schultz · *Weather and Forecasting* · **journal** · `direct` · `bibliographic`

书目与主题已核对；方法、输入、时间窗及结果待阅读原文。Bibliographic record; detailed study annotation pending.

Bibliographic identity and topical relevance reviewed from the cited publisher-deposited Crossref record. Methods, input data, forecast horizon, results and full text have not been extracted or independently verified. Code availability has not been established for this entry.

[Primary source](https://doi.org/10.1175/waf910.1) · [DOI](https://doi.org/10.1175/waf910.1) · [Evidence 2](https://api.crossref.org/works/10.1175%2Fwaf910.1)

Code availability: not verified in this snapshot.

---

<a id="vortex1994"></a>
### 1994 · Verification of the Origins of Rotation in Tornadoes Experiment: VORTEX

Erik N. Rasmussen; Jerry M. Straka; Robert Davies-Jones; Charles A. Doswell III; Frederick H. Carr; Michael D. Eilts; Donald R. MacGorman · *Bulletin of the American Meteorological Society* · **journal** · `direct` · `annotated`

Describes the original VORTEX experiment and the measurements needed to investigate tornado formation.

介绍最初VORTEX试验的研究设计和观测需求，为理解龙卷生成研究的实测证据来源提供入口。

- **Method / input:** Field-experiment design / Coordinated mobile and fixed storm observations.
- **Target & horizon:** Investigation of the origins of rotation in tornadoes.
- **Reading caution:** A campaign-design paper does not imply that every planned scientific question was resolved. Metadata/abstract-level review; experiments not independently reproduced.
- **Provenance:** metadata checked 2026-09-29; independently reproduced: false.

[Primary source](https://doi.org/10.1175/1520-0477%281994%29075%3C0995%3Avotoor%3E2.0.co%3B2) · [DOI](https://doi.org/10.1175/1520-0477%281994%29075%3C0995%3Avotoor%3E2.0.co%3B2) · [Evidence 2](https://api.crossref.org/works/10.1175%2F1520-0477%281994%29075%3C0995%3Avotoor%3E2.0.co%3B2)

Code availability: not verified in this snapshot.
