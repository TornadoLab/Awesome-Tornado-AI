# A task compass for tornado research / 任务与评测指南

This is an editorial evaluation checklist, not a claim that every seed paper satisfies it. Follow primary sources for the exact definitions used in each study.

## 1. Name the target before choosing the model

| Task | What is predicted? | What must be specified? | Representative source |
|---|---|---|---|
| Current detection | Tornado presence, tornadic circulation or radar signature at/near observation time | Whether the target is a report, vortex, debris or storm object; space/time tolerance | [NSSL TDA](https://doi.org/10.1175/1520-0434(1998)013%3C0352:TNSSLT%3E2.0.CO;2), [TPA](https://repository.library.noaa.gov/view/noaa/48189) |
| Future occurrence | Tornado occurrence after forecast issuance | Causal issue time; event onset; lead interval; object/grid/region; all input availability | [Lagerquist et al.](https://repository.library.noaa.gov/view/noaa/60124) |
| Intensity / rating | Damage-based EF/F class, wind estimate or another severity target | These are different targets; identify survey conventions, missing/unrated events and exposure bias | [Edwards et al.](https://journals.ametsoc.org/view/journals/bams/94/5/bams-d-11-00006.1.xml) |
| Probabilistic guidance | Calibrated risk over a specified space/time window | Event radius; forecast horizon; threshold choice; operational latency | [ProbSevere v3](https://repository.library.noaa.gov/view/noaa/67694) |
| Regional reasoning | Risk polygons or meteorological judgments from environmental/forecast context | Available maps, soundings, dates, evidence and spatial verification | [AgentCaster](https://arxiv.org/abs/2510.03349) |
| Radar nowcasting | Future radar fields or their quality | Field target versus tornado-event target; whether cases already contain a tornado | [Erickson et al.](https://arxiv.org/html/2609.35675v1), [RadarQA](https://arxiv.org/abs/2508.12291) |
| Post-event impact | Damage recognition, track recovery, losses or societal effects | Time after event; imagery source; class definitions; distinguish damage severity from EF survey | [Architectural Insights](https://arxiv.org/abs/2602.14523) |

**中文要点：** “图上有旋转”“当前存在龙卷”“未来将发生龙卷”“未来回波会怎样”“灾后建筑损坏几级”“预报员是否因此决策更好”，是六类不同问题。论文题目里出现 prediction，不足以确定它们属于同一任务。

## 2. Separate variables, sensors and modalities

TorNet contains multiple polarimetric radar variables. Multiple channels from one radar instrument are not automatically independent sensor modalities. For each experiment, enumerate actual variables (for example reflectivity, radial velocity, correlation coefficient), elevations, spatial coordinates, missing-data encodings and input times. Preserve folded/missing flags rather than silently presenting them as valid measurements. Consult the [TorNet paper and official implementation](https://github.com/mit-ll/tornet).

For a genuinely multi-source method, list radar, satellite, lightning, soundings, NWP, ground imagery and text separately. A text caption derived from a radar image is not a new independent observation. An EF label or a post-event damage report must not enter a real-time model as a feature unless the task explicitly occurs after that information becomes available.

## 3. Audit causality and leakage

A recommended evidence table for any future benchmark:

| Field | Required entry |
|---|---|
| Forecast issue time | Timestamp including timezone and latency convention |
| Input validity and availability | Both observation time and when it could actually be accessed |
| Label window | Exact start/end and event-matching rule |
| Spatial unit | Pixel, storm object, radar cutout, tornado event, county or risk polygon |
| Train / validation / test units | Storm/event/day/outbreak grouping; station/region/year where relevant |
| Duplicate control | Overlapping scans, repeated storm tracks, near-identical imagery and preprint/journal records |
| Threshold tuning | Done on validation data, not optimized on the final test set |
| Missing data | Masks, sensor outages, station changes and selection/exclusion rules |

Random frame splitting is not evidence of out-of-event generalization when adjacent frames describe the same storm. Report event-grouped and, where feasible, temporal/geographic held-out evaluation. This is a recommended protocol, not a claim of universal agreement on one ideal split. Atmospheric benchmark design context: [Dueben et al.](https://doi.org/10.1175/AIES-D-21-0002.1); severe-weather ML context: [McGovern et al.](https://repository.library.noaa.gov/view/noaa/52401).

## 4. Match metrics to the question

For binary contingency counts, define TP, FP, FN and TN at the same evaluation unit:

```text
POD / recall            = TP / (TP + FN)
precision               = TP / (TP + FP)
false alarm ratio (FAR) = FP / (TP + FP) = 1 - precision
false positive rate    = FP / (FP + TN)   [different denominator from FAR]
CSI                     = TP / (TP + FP + FN)
F1                      = 2TP / (2TP + FP + FN)
accuracy                = (TP + TN) / (TP + FP + FN + TN)
Brier score             = mean((forecast_probability - binary_outcome)^2)
```

These equations are definitions, not measured performance from the seed catalog. Handle zero denominators explicitly; do not silently return perfect scores. For rare events, show the base rate, counts, precision–recall curve, its integration convention, recall at operationally relevant false-alarm levels, and probability calibration. ROC-AUC alone does not describe the alarm burden. A PR-AUC value is uninterpretable without its target definition and prevalence.

For EF/F ordinal classes, include the confusion matrix, support per class, per-class recall and macro-averaged metrics. State how unrated events, EF0–1 groups and cumulative thresholds such as EF2+ are handled. Do not compare two papers with different grouping rules as if their F1 scores were commensurate.

For nowcast fields, use field-appropriate spatial/probabilistic scores; add a separately defined tornado-event evaluation before claiming tornado prediction. For polygons, define the matching radius and space/time area tradeoff. For uncertain outputs, report calibration/reliability and resolution along with discrimination. For operational systems, add latency, lead time conditional on successful detection, warning burden and human-use evaluation. The [HWT forecaster evaluation](https://repository.library.noaa.gov/view/noaa/54565) is a useful separate reading from an algorithm-only paper.

Uncertainty intervals should respect correlated storms or days; independent-frame resampling can give overly optimistic precision. Publish split manifests, configuration, software versions, inference costs and enough provenance to repeat the evaluation.

## 5. Do not turn method families into claims

A CNN, transformer, foundation model or VLM is an architecture/training family. None is intrinsically “more intelligent” for a specified tornado task without evidence. Distinguish pretrained-backbone transfer, supervised fine-tuning, in-context prompting, retrieval, tool-using agents and reinforcement fine-tuning.

Reinforcement fine-tuning of a reasoning model—such as the meteorological work in [Weather-R1](https://arxiv.org/abs/2601.14044)—is not the same problem as learning an observation policy that chooses radar scans or sensor actions. The latter needs a state/observation/action/cost definition and a closed-loop evaluation. This seed does **not** claim to have established the best tornado-observation RL literature.

## 6. Rating caveat and corrections

EF/F rating is damage-based and depends on the information available from an event. Do not equate a radar-derived wind estimate with a survey label. [Wurman et al. (2021)](https://www.pnas.org/doi/10.1073/pnas.2021535118) has a [2025 correction](https://pmc.ncbi.nlm.nih.gov/articles/PMC12519134/); consult both when using its quantitative calculations. The catalog deliberately does not recycle headline strength claims as universal model targets.
