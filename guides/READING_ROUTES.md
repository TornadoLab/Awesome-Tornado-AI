# Three routes into the storm

Routes are editorial suggestions, not quality rankings. Read primary papers and inspect data availability before implementing.

### SCOUT / 01 · First contact / 从零进入龙卷研究

Start with the physics. Learn what the sensors see, and what the labels mean. 先理解物理、雷达信号与标签，再看模型。

1. [1953 — Radar Records Illinois Tornadogenesis](../papers/radar.md#stout1953)
2. [1979 — Severe Thunderstorm Evolution and Mesocyclone Structure as Related to Tornadogenesis](../papers/foundations.md#lemon1979)
3. [2015 — A review of supercell and tornado dynamics](../papers/foundations.md#daviesjones2015)
4. [1978 — Tornado Detection by Pulsed Doppler Radar](../papers/radar.md#brown1978)
5. [2005 — Polarimetric Tornado Detection](../papers/radar.md#ryzhkov2005)
6. [1971 — Proposed characterization of tornadoes and hurricanes by area and intensity](../papers/rating.md#fujita1971)
7. [2013 — Tornado Intensity Estimation: Past, Present, and Future](../papers/rating.md#edwards2013)
8. [2025 — A Benchmark Dataset for Tornado Detection and Prediction using Full-Resolution Polarimetric Weather Radar Data](../papers/data.md#tornet2025)

### STORM CHASER / 02 · Build your first baseline / 从传统算法到可复现基线

Follow the path from signature algorithms to neural detection and probabilistic guidance. 从特征算法走到神经检测与概率预报，逐项核对输入和时间窗。

1. [1998 — The National Severe Storms Laboratory Tornado Detection Algorithm](../papers/radar.md#mitchell1998)
2. [1996 — A Neural Network for Tornado Prediction Based on Doppler Radar-Derived Attributes](../papers/ml.md#marzban1996)
3. [2008 — Tornado Detection Using a Neuro–Fuzzy System to Integrate Shear and Spectral Signatures](../papers/ml.md#wang2008)
4. [2009 — Support vector machines for spatiotemporal tornado prediction](../papers/ml.md#adrianto2009)
5. [2020 — Deep Learning on Three-Dimensional Multiscale Data for Next-Hour Tornado Prediction](../papers/dl.md#lagerquist2020)
6. [2023 — The Tornado Probability Algorithm: A Probabilistic Machine Learning Tornadic Circulation Detection Algorithm](../papers/ml.md#sandmael2023)
7. [2025 — A Benchmark Dataset for Tornado Detection and Prediction using Full-Resolution Polarimetric Weather Radar Data](../papers/data.md#tornet2025)
8. [2026 — Analysis of Generalization Performance of Tornado Detection Models: A Cross-Domain Evaluation from U.S. to Chinese Weather Radar Observations](../papers/evaluation.md#jiang2026)
9. [2018 — Long-Term Performance Metrics for National Weather Service Tornado Warnings](../papers/evaluation.md#brooks2018)

### RESEARCHER / 03 · Read the frontier carefully / 走向多模态与智能体

Explore reasoning, regional emulators and new benchmarks—without confusing their tasks. 探索推理、区域天气模拟与新基准，不把任务差异包装成性能进步。

1. [2024 — WeatherQA: Can Multimodal Language Models Reason about Severe Weather?](../papers/agents.md#weatherqa2024)
2. [2025 — AgentCaster: Reasoning-Guided Tornado Forecasting](../papers/agents.md#agentcaster2025)
3. [2026 — TDA-DARKNet: A Deep Learning Model Based on Dual-Polarization Radar Data for Tornado Detection](../papers/dl.md#darknet2026)
4. [2026 — Developing Machine Learning-Based Watch-to-Warning Severe Weather Guidance from the Warn-on-Forecast System](../papers/forecast.md#flora2026)
5. [2026 — Explainable Deep Learning for Probabilistic Nowcasting of Radar Reflectivity in Tornadic Storms](../papers/forecast.md#erickson2026)
6. [2025 — RadarQA: Multi-modal Quality Analysis of Weather Radar Forecasts](../papers/agents.md#radarqa2025)
7. [2026 — ASTRA: Architectural inSights for post-ToRnado damAge recognition](../papers/impacts.md#umeike2026)
8. [2026 — TornadoNet: Real-Time Building Damage Detection with Ordinal Supervision](../papers/impacts.md#tornadonet2026)
9. [2026 — From Pixels to Semantics: A Multi-Stage AI Framework for Structural Damage Detection in Satellite Imagery](../papers/agents.md#shakya2026)

**Do not skip the timestamp audit.** A convincing model can still learn from observations unavailable at its claimed forecast issue time.
