# Deep tornado detection & prediction

深度学习检测与发生预测 · 16 records · snapshot 2026-09-29

[Back to the catalog](README.md) · [Scope and evaluation](../guides/TASKS.md)

<a id="snaiki2026"></a>
### 2026 · A hybrid physics-informed graph neural network for tornado wind-field modeling

Reda Snaiki; Seyedeh Fatemeh Mirfakhar · *Advances in Wind Engineering* · **journal** · `direct` · `annotated`

Combines an analytical tornado representation with a physics-informed graph model to represent wind-field structure.

将解析龙卷模型与物理约束图神经网络结合，用于描述龙卷风场结构，扩展智能方法在风工程中的应用范围。

- **Method / input:** Physics-informed graph neural network / Analytical vortex representation and high-fidelity wind-field information.
- **Target & horizon:** Tornado wind-field modeling.
- **Reading caution:** Wind-field reconstruction or emulation is distinct from predicting tornado onset. Metadata/abstract-level review; experiments not independently reproduced.
- **Provenance:** metadata checked 2026-09-29; independently reproduced: false.

[Primary source](https://doi.org/10.1016/j.awe.2026.100101) · [DOI](https://doi.org/10.1016/j.awe.2026.100101) · [Evidence 2](https://api.crossref.org/works/10.1016%2Fj.awe.2026.100101)

Code availability: not verified in this snapshot.

---

<a id="xie2026enhanced"></a>
### 2026 · Dual-polarization radar-based enhanced tornado detection network with explainability analysis

Jinyang Xie; Kanghui Zhou; Lei Han; Yongguang Zheng · *Expert Systems with Applications* · **journal** · `direct` · `annotated`

Combines a dual-polarization tornado detection network with analysis of the evidence used by the model.

将双偏振雷达龙卷检测网络与模型解释分析结合，补充较新的专用识别方法。

- **Method / input:** Enhanced dual-polarization detection with explainability / Dual-polarization radar observations.
- **Target & horizon:** Radar-based tornado detection.
- **Reading caution:** Attribution analysis does not prove the model learned a physically causal mechanism. Metadata/abstract-level review; experiments not independently reproduced.
- **Provenance:** metadata checked 2026-09-29; independently reproduced: false.

[Primary source](https://doi.org/10.1016/j.eswa.2026.132803) · [DOI](https://doi.org/10.1016/j.eswa.2026.132803) · [Evidence 2](https://api.crossref.org/works/10.1016%2Fj.eswa.2026.132803)

Code availability: not verified in this snapshot.

---

<a id="ref-0891baad4eb7"></a>
### 2026 · Physics-Enhanced Multistage Tornado Prediction Network Using Doppler Radar Data

Jinyang Xie; Kanghui Zhou; Lei Han; Xuming Zhang; Yongguang Zheng · *IEEE Transactions on Geoscience and Remote Sensing* · **journal** · `direct` · `bibliographic`

书目与主题已核对；方法、输入、时间窗及结果待阅读原文。Bibliographic record; detailed study annotation pending.

Bibliographic identity and topical relevance reviewed from the cited publisher-deposited Crossref record. Methods, input data, forecast horizon, results and full text have not been extracted or independently verified. Code availability has not been established for this entry.

[Primary source](https://doi.org/10.1109/tgrs.2026.3705532) · [DOI](https://doi.org/10.1109/tgrs.2026.3705532) · [Evidence 2](https://api.crossref.org/works/10.1109%2Ftgrs.2026.3705532)

Code availability: not verified in this snapshot.

---

<a id="darknet2026"></a>
### 2026 · TDA-DARKNet: A Deep Learning Model Based on Dual-Polarization Radar Data for Tornado Detection

Guoxiu Zhang; Qiangyu Zeng; Fugui Zhang; Hao Wang; Tiantian Yu · *Remote Sensing* · **journal** · `direct` · `annotated`

A recent radar-deep-learning entry with attention and KAN components.

覆盖最新双偏振深度网络路线；个例提前量不代表所有事件的稳定预警能力。

- **Method / input:** Dense/residual CNN; attention; KAN / Dual-polarization radar.
- **Target & horizon:** Tornado detection; case-specific lead analyses.
- **Reading caution:** Bibliographic/abstract-level seed annotation; full-text methods, splits and performance have not been independently audited.
- **Provenance:** metadata checked 2026-09-29; independently reproduced: false.

[Primary source](https://www.mdpi.com/2072-4292/18/8/1124) · [DOI](https://doi.org/10.3390/rs18081124)

Code availability: not verified in this snapshot.

---

<a id="tordet2025"></a>
### 2026 · TorDet: A Refined Two-Stage Deep Learning Approach for Radar-Based Tornado Detection

Maoyu Wang; Kanghui Zhou; Haonan Chen; Lei Han; Yongguang Zheng · *IEEE Transactions on Geoscience and Remote Sensing* · **journal** · `direct` · `annotated`

A recent two-stage detector with a released inference interface.

两阶段雷达龙卷检测；作者仓库提供 CINRAD S 波段推理接口与示例。

- **Method / input:** Two-stage deep learning / CINRAD S-band radar.
- **Target & horizon:** Radar-based tornado detection.
- **Reading caution:** IEEE publisher metadata assigns this article to the 2026 journal volume; its DOI contains 2025. The legacy record ID is retained for stable links. A released inference interface does not by itself establish a complete reproducible training pipeline.
- **Provenance:** metadata checked 2026-09-29; independently reproduced: false.

[Primary source](https://ieeexplore.ieee.org/document/11313536/) · [DOI](https://doi.org/10.1109/TGRS.2025.3647545) · [Author-linked code](https://github.com/Tornado-AI/TorDet) · [Evidence 2](https://github.com/Tornado-AI/TorDet) · [Evidence 3](https://api.crossref.org/works/10.1109%2Ftgrs.2025.3647545)

Code availability: author-linked release above.

---

<a id="ref-85ea1b95b91a"></a>
### 2026 · TorViNet: A spatiotemporal deep learning network for tornado detection in user-captured social media videos

Hongjin Chen; Kanghui Zhou; Zhonghua Zheng; Lei Han; Yongguang Zheng · *Expert Systems with Applications* · **journal** · `direct` · `annotated`

Uses a spatiotemporal network to recognize tornado footage in the TorVideo collection, extending the atlas beyond radar-image detection.

面向用户拍摄的社交媒体视频识别龙卷，将研究输入从雷达扩展到地面实景视频；任务是识别已出现的龙卷画面。

- **Method / input:** Spatiotemporal deep learning for video recognition / User-captured social-media video clips.
- **Target & horizon:** Recognition of tornado scenes already visible in video; no pre-onset forecast horizon.
- **Reading caution:** Visible-scene recognition is distinct from radar detection and pre-onset prediction. Publisher links model/training/evaluation code, but reports that raw TorVideo cannot be redistributed because of platform copyright and privacy constraints. No reproduction was performed.
- **Provenance:** metadata checked 2026-09-29; independently reproduced: false.

[Primary source](https://doi.org/10.1016/j.eswa.2026.131093) · [DOI](https://doi.org/10.1016/j.eswa.2026.131093) · [Author-linked code](https://github.com/Tornado-AI/TorViNet) · [Evidence 2](https://api.crossref.org/works/10.1016%2Fj.eswa.2026.131093) · [Evidence 3](https://www.sciencedirect.com/science/article/abs/pii/S0957417426000072) · [Evidence 4](https://github.com/Tornado-AI/TorViNet)

Code availability: author-linked release above.

---

<a id="xie2025ts"></a>
### 2025 · Enhancing multi-task learning-based Tornado identification using spatial and temporal information from weather radar images

Jinyang Xie; Kanghui Zhou; Lei Han; Liang Guan; Maoyu Wang; Yongguang Zheng; Hongjin Chen; Jiaqi Mao · *Applied Soft Computing* · **journal** · `direct` · `annotated`

Extends multi-task tornado identification by incorporating temporal evolution alongside spatial radar information.

在多任务龙卷识别中加入雷达图像的时间演变信息，连接单时刻空间识别与连续观测建模。

- **Method / input:** TS-MTINet spatiotemporal multi-task learning / Time sequences of weather-radar images.
- **Target & horizon:** Tornado identification and number estimation.
- **Reading caution:** Temporal inputs do not by themselves establish a causal forecast horizon. Metadata/abstract-level review; experiments not independently reproduced.
- **Provenance:** metadata checked 2026-09-29; independently reproduced: false.

[Primary source](https://doi.org/10.1016/j.asoc.2025.113834) · [DOI](https://doi.org/10.1016/j.asoc.2025.113834) · [Evidence 2](https://api.crossref.org/works/10.1016%2Fj.asoc.2025.113834)

Code availability: not verified in this snapshot.

---

<a id="ref-60eafd800706"></a>
### 2025 · Shape-Aware Refinement of Deep Learning Detections from UAS Imagery for Tornado-Induced Treefall Mapping

Mitra Nasimi; Richard L. Wood · *Remote Sensing* · **journal** · `direct` · `bibliographic`

书目与主题已核对；方法、输入、时间窗及结果待阅读原文。Bibliographic record; detailed study annotation pending.

Bibliographic identity and topical relevance reviewed from the cited publisher-deposited Crossref record. Methods, input data, forecast horizon, results and full text have not been extracted or independently verified. Code availability has not been established for this entry.

[Primary source](https://doi.org/10.3390/rs18010141) · [DOI](https://doi.org/10.3390/rs18010141) · [Evidence 2](https://api.crossref.org/works/10.3390%2Frs18010141)

Code availability: not verified in this snapshot.

---

<a id="ref-a85747089237"></a>
### 2025 · Using Neural Network Models and Synoptic Circulation Patterns to Project Future Changes in US Tornado Activity

Cameron C. Lee; Omon A. Obarein; Erik Tyler Smith · *Journal of Geophysical Research: Machine Learning and Computation* · **journal** · `direct` · `bibliographic`

书目与主题已核对；方法、输入、时间窗及结果待阅读原文。Bibliographic record; detailed study annotation pending.

Bibliographic identity and topical relevance reviewed from the cited publisher-deposited Crossref record. Methods, input data, forecast horizon, results and full text have not been extracted or independently verified. Code availability has not been established for this entry.

[Primary source](https://doi.org/10.1029/2025jh000629) · [DOI](https://doi.org/10.1029/2025jh000629) · [Evidence 2](https://api.crossref.org/works/10.1029%2F2025jh000629)

Code availability: not verified in this snapshot.

---

<a id="zhou2024"></a>
### 2024 · A Novel Hybrid Approach for Tornado Prediction in the United States: Kalman-Convolutional BiLSTM with Multi-Head Attention

Jiawei Zhou · *arXiv* · **preprint** · `direct` · `annotated`

A hybrid sequence-model entry whose temporal protocol deserves careful reading.

覆盖卷积、双向时序网络与注意力组合；阅读时重点核对因果输入、划分与提前量。

- **Method / input:** Kalman; CNN; BiLSTM; attention / MRMS radar-derived inputs.
- **Target & horizon:** Tornado prediction; inspect causal horizon.
- **Reading caution:** Bibliographic/abstract-level seed annotation; full-text methods, splits and performance have not been independently audited.
- **Provenance:** metadata checked 2026-09-29; independently reproduced: false.

[Primary source](https://arxiv.org/abs/2408.02751) · [arXiv](https://arxiv.org/abs/2408.02751)

Code availability: not verified in this snapshot.

---

<a id="ref-cfd5ab87f798"></a>
### 2024 · An LSTM deep learning framework for history-based tornado prediction using meteorological data and damage assessment using NDVI anomalies

Omid Memarian Sorkhabi · *Results in Earth Sciences* · **journal** · `direct` · `bibliographic`

书目与主题已核对；方法、输入、时间窗及结果待阅读原文。Bibliographic record; detailed study annotation pending.

Bibliographic identity and topical relevance reviewed from the cited publisher-deposited Crossref record. Methods, input data, forecast horizon, results and full text have not been extracted or independently verified. Code availability has not been established for this entry.

[Primary source](https://doi.org/10.1016/j.rines.2024.100040) · [DOI](https://doi.org/10.1016/j.rines.2024.100040) · [Evidence 2](https://api.crossref.org/works/10.1016%2Fj.rines.2024.100040)

Code availability: not verified in this snapshot.

---

<a id="xie2024"></a>
### 2024 · Multi‐Task Learning for Tornado Identification Using Doppler Radar Data

Jinyang Xie; Kanghui Zhou; Haonan Chen; Lei Han; Liang Guan; Maoyu Wang; Yongguang Zheng; Hongjin Chen; Jiaqi Mao · *Geophysical Research Letters* · **journal** · `direct` · `annotated`

Jointly learns tornado identification and count estimation with attention-based spatial and variable interactions.

通过空间与通道注意力联合学习龙卷识别和数量估计，补入中国雷达深度学习研究中的MTI-Net方法。

- **Method / input:** Multi-task identification network (MTI-Net) / Doppler weather-radar data.
- **Target & horizon:** Tornado detection and count estimation.
- **Reading caution:** Detection, count estimation and forecast lead time are distinct tasks. Metadata/abstract-level review; experiments not independently reproduced.
- **Provenance:** metadata checked 2026-09-29; independently reproduced: false.

[Primary source](https://doi.org/10.1029/2024gl108809) · [DOI](https://doi.org/10.1029/2024gl108809) · [Evidence 2](https://api.crossref.org/works/10.1029%2F2024gl108809)

Code availability: not verified in this snapshot.

---

<a id="ref-6ba8eba76cda"></a>
### 2024 · Using Deep Learning and Advanced Image Processing for the Automated Estimation of Tornado-Induced Treefall

Mitra Nasimi; Richard L. Wood · *Remote Sensing* · **journal** · `direct` · `bibliographic`

书目与主题已核对；方法、输入、时间窗及结果待阅读原文。Bibliographic record; detailed study annotation pending.

Bibliographic identity and topical relevance reviewed from the cited publisher-deposited Crossref record. Methods, input data, forecast horizon, results and full text have not been extracted or independently verified. Code availability has not been established for this entry.

[Primary source](https://doi.org/10.3390/rs16071130) · [DOI](https://doi.org/10.3390/rs16071130) · [Evidence 2](https://api.crossref.org/works/10.3390%2Frs16071130)

Code availability: not verified in this snapshot.

---

<a id="ref-85c1d71a8353"></a>
### 2022 · Development of Tornado Detection Technique with Doppler Radar using Deep Learning

Kenichi KUSUNOKI; Naoki ISHITSU; Toru ADACHI; Osamu SUZUKI; Ken-ichiro ARAI; Chusei FUJIWARA; Hiroto SUZUKI · *Wind Engineers, JAWE* · **journal** · `direct` · `bibliographic`

书目与主题已核对；方法、输入、时间窗及结果待阅读原文。Bibliographic record; detailed study annotation pending.

Bibliographic identity and topical relevance reviewed from the cited publisher-deposited Crossref record. Methods, input data, forecast horizon, results and full text have not been extracted or independently verified. Code availability has not been established for this entry.

[Primary source](https://doi.org/10.5359/jawe.47.218) · [DOI](https://doi.org/10.5359/jawe.47.218) · [Evidence 2](https://api.crossref.org/works/10.5359%2Fjawe.47.218)

Code availability: not verified in this snapshot.

---

<a id="lagerquist2020"></a>
### 2020 · Deep Learning on Three-Dimensional Multiscale Data for Next-Hour Tornado Prediction

Ryan Lagerquist; Amy McGovern; Cameron R. Homeyer; David John Gagne II; Travis Smith · *Monthly Weather Review* · **journal** · `direct` · `annotated`

A key multiscale deep-learning reference combining storm structure and environment.

结合三维风暴结构和环境信息，研究下一小时龙卷预测，是从检测走向预报的重要文献。

- **Method / input:** Convolutional neural networks / 3D radar and environmental soundings.
- **Target & horizon:** Next-hour tornado prediction.
- **Reading caution:** Bibliographic/abstract-level seed annotation; full-text methods, splits and performance have not been independently audited.
- **Provenance:** metadata checked 2026-09-29; independently reproduced: false.

[Primary source](https://repository.library.noaa.gov/view/noaa/60124) · [DOI](https://doi.org/10.1175/MWR-D-19-0372.1)

Code availability: not verified in this snapshot.

---

<a id="ref-3c8575044fee"></a>
### 2016 · A Study of Tornado Prediction Using Deep Belief Network

Susumu SHIRAYAMA; Ryo SHIBATA · *The Proceedings of The Computational Mechanics Conference* · **journal** · `direct` · `bibliographic`

书目与主题已核对；方法、输入、时间窗及结果待阅读原文。Bibliographic record; detailed study annotation pending.

Bibliographic identity and topical relevance reviewed from the cited publisher-deposited Crossref record. Methods, input data, forecast horizon, results and full text have not been extracted or independently verified. Code availability has not been established for this entry.

[Primary source](https://doi.org/10.1299/jsmecmd.2016.29.4_213) · [DOI](https://doi.org/10.1299/jsmecmd.2016.29.4_213) · [Evidence 2](https://api.crossref.org/works/10.1299%2Fjsmecmd.2016.29.4_213)

Code availability: not verified in this snapshot.
