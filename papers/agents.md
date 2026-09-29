# Multimodal reasoning & agents

多模态推理与智能体 · 5 records · snapshot 2026-09-29

[Back to the catalog](README.md) · [Scope and evaluation](../guides/TASKS.md)

<a id="shakya2026"></a>
### 2026 · From Pixels to Semantics: A Multi-Stage AI Framework for Structural Damage Detection in Satellite Imagery

Bijay Shakya; Catherine Hoier; Khandaker Mamun Ahmed · *CVPR 2026 Workshops (AI4RWC)* · **conference** · `direct` · `annotated`

Combines image enhancement, object detection and a vision-language stage for damage interpretation, with experiments including a tornado-event subset.

将图像增强、目标检测和视觉语言解释结合，用于灾后建筑损伤分析，实验包含龙卷事件子集。

- **Method / input:** Super-resolution, object detection and vision-language interpretation / Pre- and post-disaster satellite imagery.
- **Target & horizon:** Post-event building-damage detection and semantic interpretation.
- **Reading caution:** CVF workshop publication and arXiv:2603.22768 identify the same work, counted once. Mixed-disaster test imagery and generated descriptions do not establish general tornado reasoning or physical localization accuracy. No independent reproduction.
- **Provenance:** metadata checked 2026-09-29; independently reproduced: false.

[Primary source](https://openaccess.thecvf.com/content/CVPR2026W/AI4RWC/html/Shakya_From_Pixels_to_Semantics_A_Multi-Stage_AI_Framework_for_Structural_CVPRW_2026_paper.html) · [arXiv](https://arxiv.org/abs/2603.22768) · [Author-linked code](https://github.com/Mamunahmed33/From-Pixels-to-Semantic) · [Evidence 1](https://arxiv.org/abs/2603.22768) · [Evidence 3](https://github.com/Mamunahmed33/From-Pixels-to-Semantic)

Code availability: author-linked release above.

---

<a id="weatherr12026"></a>
### 2026 · Weather-R1: Logically Consistent Reinforcement Fine-Tuning for Multimodal Reasoning in Meteorology

Kaiyu Wu; Pucheng Han; Hualong Zhang; Naigeng Wu; Keze Wang · *ICASSP 2026* · **conference** · `transfer` · `annotated`

A transferable reasoning-training method, not established tornado-detection evidence.

提供逻辑一致性的强化微调思路，但尚不能当成龙卷检测有效性的证据。

- **Method / input:** Reinforcement fine-tuning; VLM / Meteorological images and questions.
- **Target & horizon:** Meteorological reasoning consistency.
- **Reading caution:** Its WeatherQA is a different benchmark from Ma et al. (2024). Reinforcement fine-tuning is not the same task as adaptive radar scanning or operational tornado-warning control. Conference status checked against the official ICASSP 2026 accepted-paper program (paper 9095); final proceedings DOI not verified.
- **Provenance:** metadata checked 2026-09-29; independently reproduced: false.

[Primary source](https://www.cmsworkshops.com/ICASSP2026/view_paper.php?PaperNum=9095&bare=1) · [arXiv](https://arxiv.org/abs/2601.14044) · [Author-linked code](https://github.com/Marcowky/Weather-R1) · [Evidence 1](https://arxiv.org/abs/2601.14044) · [Evidence 3](https://github.com/Marcowky/Weather-R1)

Code availability: author-linked release above.

---

<a id="agentcaster2025"></a>
### 2025 · AgentCaster: Reasoning-Guided Tornado Forecasting

Michael Chen · *arXiv* · **preprint** · `direct` · `annotated`

Tests reasoning-guided agents on tornado-risk forecasting and explicit hallucination-related evaluation.

直接面向龙卷风险预报的智能体研究，关注风险区域、推理与幻觉评估。

- **Method / input:** Multimodal reasoning agents / Convection-allowing forecast maps and soundings.
- **Target & horizon:** 12–36 h tornado-risk polygon forecasting.
- **Reading caution:** This is forecast-map/sounding-based regional risk forecasting, not raw polarimetric-radar event detection. Peer-reviewed publication status was not established in this seed.
- **Provenance:** metadata checked 2026-09-29; independently reproduced: false.

[Primary source](https://arxiv.org/abs/2510.03349) · [arXiv](https://arxiv.org/abs/2510.03349) · [Author-linked code](https://github.com/agentcaster/agentcaster) · [Evidence 2](https://arxiv.org/html/2510.03349v1) · [Evidence 3](https://huggingface.co/datasets/agentcaster/agentcaster) · [Evidence 4](https://github.com/agentcaster/agentcaster)

Code availability: author-linked release above.

---

<a id="radarqa2025"></a>
### 2025 · RadarQA: Multi-modal Quality Analysis of Weather Radar Forecasts

Xuming He; Zhiyuan You; Junchao Gong; Couhua Liu; Xiaoyu Yue; Peiqin Zhuang; Wenlong Zhang; Lei Bai · *arXiv* · **preprint** · `transfer` · `annotated`

Provides a radar-forecast assessment paradigm and the RQA-70K dataset.

评价雷达预报质量并生成描述性报告；不能当作已验证的龙卷识别模型。

- **Method / input:** Multimodal large language model / Radar forecast frames and sequences.
- **Target & horizon:** Quality analysis and descriptive forecast assessment.
- **Reading caution:** Bibliographic/abstract-level seed annotation; full-text methods, splits and performance have not been independently audited.
- **Provenance:** metadata checked 2026-09-29; independently reproduced: false.

[Primary source](https://arxiv.org/abs/2508.12291) · [arXiv](https://arxiv.org/abs/2508.12291) · [Author-linked code](https://github.com/hexmSeeU/RadarQA)

Code availability: author-linked release above.

---

<a id="weatherqa2024"></a>
### 2024 · WeatherQA: Can Multimodal Language Models Reason about Severe Weather?

Chengqian Ma; Zhanxiang Hua; Alexandra Anderson-Frey; Vikram Iyer; Xin Liu; Lianhui Qin · *arXiv* · **preprint** · `context` · `annotated`

A benchmark for ingredient-based multimodal reasoning, not raw-volume tornado detection.

多张诊断图与专家文本上的强对流推理评测；不是原始体扫龙卷检测。

- **Method / input:** Vision-language evaluation / Diagnostic images and expert forecast text.
- **Target & horizon:** Severe-weather reasoning and QA.
- **Reading caution:** Do not confuse this WeatherQA (Ma et al., 2024) with the identically named benchmark introduced in Weather-R1 (Wu et al., 2026). Later publication status was not independently established.
- **Provenance:** metadata checked 2026-09-29; independently reproduced: false.

[Primary source](https://arxiv.org/abs/2406.11217) · [arXiv](https://arxiv.org/abs/2406.11217) · [Author-linked code](https://github.com/chengqianma/WeatherQA)

Code availability: author-linked release above.
