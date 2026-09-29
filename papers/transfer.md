# Transferable weather AI

可迁移的天气 AI 方法 · 5 records · snapshot 2026-09-29

[Back to the catalog](README.md) · [Scope and evaluation](../guides/TASKS.md)

<a id="aurora2025"></a>
### 2025 · A foundation model for the Earth system

Cristian Bodnar; Wessel P. Bruinsma; Ana Lucic; Megan Stanley; Anna Allen; Johannes Brandstetter; Patrick Garvan; Maik Riechert; Jonathan A. Weyn; Haiyu Dong; Jayesh K. Gupta; Kit Thambiratnam; Alexander T. Archibald; Chun-Chieh Wu; Elizabeth Heider; Max Welling; Richard E. Turner; Paris Perdikaris · *Nature* · **journal** · `transfer` · `annotated`

An adaptable foundation-model design to consider for transfer research.

地球系统基础模型的迁移设计参考；不把其通用能力当作龙卷任务实验证据。

- **Method / input:** Earth-system foundation model; Aurora / Diverse Earth-system data.
- **Target & horizon:** Multiple Earth-system forecast tasks.
- **Reading caution:** Bibliographic/abstract-level seed annotation; full-text methods, splits and performance have not been independently audited.
- **Provenance:** metadata checked 2026-09-29; independently reproduced: false.

[Primary source](https://www.nature.com/articles/s41586-025-09005-y) · [DOI](https://doi.org/10.1038/s41586-025-09005-y) · [arXiv](https://arxiv.org/abs/2405.13063) · [Author-linked code](https://github.com/microsoft/aurora) · [Evidence 2](https://api.crossref.org/works/10.1038%2Fs41586-025-09005-y)

Code availability: author-linked release above.

---

<a id="climax2023"></a>
### 2023 · ClimaX: A foundation model for weather and climate

Tung Nguyen; Johannes Brandstetter; Ashish Kapoor; Jayesh K. Gupta; Aditya Grover · *ICML / PMLR* · **conference** · `transfer` · `annotated`

Read for variable-aware pretraining and adaptation across datasets.

变量感知预训练与跨数据集迁移的参考，不宣称能直接解析龙卷尺度。

- **Method / input:** Transformer foundation model / Heterogeneous weather/climate variables.
- **Target & horizon:** General weather and climate transfer.
- **Reading caution:** Bibliographic/abstract-level seed annotation; full-text methods, splits and performance have not been independently audited.
- **Provenance:** metadata checked 2026-09-29; independently reproduced: false.

[Primary source](https://proceedings.mlr.press/v202/nguyen23a.html) · [arXiv](https://arxiv.org/abs/2301.10343) · [Author-linked code](https://github.com/microsoft/ClimaX) · [Evidence 2](https://arxiv.org/abs/2301.10343)

Code availability: author-linked release above.

---

<a id="graphcast2023"></a>
### 2023 · Learning skillful medium-range global weather forecasting

Remi Lam; Alvaro Sanchez-Gonzalez; Matthew Willson; Peter Wirnsberger; Meire Fortunato; Ferran Alet; Suman Ravuri; Timo Ewalds; Zach Eaton-Rosen; Weihua Hu; Alexander Merose; Stephan Hoyer; George Holland; Oriol Vinyals; Jacklynn Stott; Alexander Pritzel; Shakir Mohamed; Peter Battaglia · *Science* · **journal** · `transfer` · `annotated`

A graph-based Earth-system modeling reference, not a resolved tornado model.

图神经网络全球天气预报代表方法，可借鉴结构，但不等于能解析龙卷。

- **Method / input:** Graph neural network; GraphCast / Global reanalysis.
- **Target & horizon:** Medium-range global weather.
- **Reading caution:** Bibliographic/abstract-level seed annotation; full-text methods, splits and performance have not been independently audited. The original author-linked GraphCast repository now redirects to google-deepmind/weathernext; select the GraphCast implementation/version within that evolving project.
- **Provenance:** metadata checked 2026-09-29; independently reproduced: false.

[Primary source](https://www.science.org/doi/10.1126/science.adi2336) · [DOI](https://doi.org/10.1126/science.adi2336) · [arXiv](https://arxiv.org/abs/2212.12794) · [Author-linked code](https://github.com/google-deepmind/graphcast) · [Evidence 2](https://api.crossref.org/works/10.1126%2Fscience.adi2336) · [Evidence 3](https://github.com/google-deepmind/graphcast)

Code availability: author-linked release above.

---

<a id="nowcastnet2023"></a>
### 2023 · Skilful nowcasting of extreme precipitation with NowcastNet

Yuchen Zhang; Mingsheng Long; Kaiyuan Chen; Lanxiang Xing; Ronghua Jin; Michael I. Jordan; Jianmin Wang · *Nature* · **journal** · `transfer` · `annotated`

A transfer-method reference for combining physical constraints with generative prediction.

物理约束与生成模型融合的参考，不将强降水预测包装成龙卷发生预测。

- **Method / input:** Physics-conditioned generative modeling / Radar precipitation fields.
- **Target & horizon:** Extreme-precipitation nowcasting.
- **Reading caution:** Extreme-precipitation nowcasting is a transfer method, not tornado validation. The author-linked code and pretrained weights are a Code Ocean capsule, not an identified official GitHub repository. No independent reproduction was performed. The DOI resolves to Code Ocean capsule 3935105; automated retrieval returned HTTP 403 on 2026-09-29, so capsule execution/download was not verified.
- **Provenance:** metadata checked 2026-09-29; independently reproduced: false.

[Primary source](https://www.nature.com/articles/s41586-023-06184-4) · [DOI](https://doi.org/10.1038/s41586-023-06184-4) · [Author-linked code](https://doi.org/10.24433/CO.0832447.v1) · [Evidence 2](https://api.crossref.org/works/10.1038%2Fs41586-023-06184-4) · [Evidence 3](https://doi.org/10.24433/CO.0832447.v1)

Code availability: author-linked release above.

---

<a id="dgmr2021"></a>
### 2021 · Skilful precipitation nowcasting using deep generative models of radar

Suman Ravuri; Karel Lenc; Matthew Willson; Dmitry Kangin; Remi Lam; Piotr Mirowski; Megan Fitzsimons; Maria Athanassiadou; Sheleem Kashem; Sam Madge; Rachel Prudden; Amol Mandhane; Aidan Clark; Andrew Brock; Karen Simonyan; Raia Hadsell; Niall Robinson; Ellen Clancy; Alberto Arribas; Shakir Mohamed · *Nature* · **journal** · `transfer` · `annotated`

A transferable generative forecasting and human-evaluation reference.

生成式雷达临近预报与人工评价的参考路线；降水技巧不代表龙卷预报技巧。

- **Method / input:** Deep generative radar nowcasting / Weather radar.
- **Target & horizon:** Precipitation nowcasting.
- **Reading caution:** Precipitation-field skill is not tornado-event skill. The linked release supplies pretrained generative models; existence of this repository is not a verification of a complete reproducible training pipeline.
- **Provenance:** metadata checked 2026-09-29; independently reproduced: false.

[Primary source](https://www.nature.com/articles/s41586-021-03854-z) · [DOI](https://doi.org/10.1038/s41586-021-03854-z) · [Author-linked code](https://github.com/deepmind/deepmind-research/tree/master/nowcasting) · [Evidence 2](https://api.crossref.org/works/10.1038%2Fs41586-021-03854-z) · [Evidence 3](https://github.com/deepmind/deepmind-research/tree/master/nowcasting)

Code availability: author-linked release above.
