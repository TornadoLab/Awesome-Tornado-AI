# Coverage and remaining work / 覆盖与待办

The 2026-09-29 collection spans 15 directions, including early observations, physics, traditional radar detection, rating, forecasting, ML, multimodal methods, engineering and social consequences. A large entry count does not establish exhaustive or balanced coverage. The following gaps concern this collection, not an absence of research in these fields.

| Priority | Remaining work | Completion evidence |
|---|---|---|
| P0 | Read and annotate the 767 bibliography-only entries | Source-backed method/input/target/limitations notes; upgrade `record_type` only when completed. |
| P0 | Expand beyond capped retrieval | Rerun failed queries with rate-aware backoff, paginate relevant result sets and retain dated decisions. Crossref title matches alone are insufficient. |
| P0 | Chinese-language and other national literature | Search original journals plus CNKI/Wanfang and institutional collections where accessible; retain original titles and resolve English/Chinese duplicate versions. |
| P0 | Books, theses, conference proceedings and reports | Search publication types not covered by the broad journal-article filter; establish author/year/edition identities. |
| P0 | Resolve 86 held candidates and uncertain versions | Inspect original genre, author and content evidence; record include/exclude/merge decisions rather than adding all hits. |
| P0 | Continue code discovery | Check each relevant paper's code/data statement and authors' project pages; distinguish complete training releases, inference tools and third-party implementations. |
| P1 | Audit early authorship and duplicate versions | Resolve the 1884 Science author initial and similarly titled historical items; inspect the related 2014/2015 fire-vortex presentations. |
| P1 | Balance storm families and countries | Track supercell, QLCS, landspout, waterspout and tropical-cyclone cases by region; do not infer generalization from category membership. |
| P1 | Extract engineering and rating conventions | Distinguish EF/F/other scales, measured wind, damage indicators, structural vulnerability and uncertainty. |
| P1 | Harmonize forecasting/evaluation descriptions | Record issue time, observation availability, event radius, lead-time distribution, validation unit, split and calibration. |
| P1 | Check correction/retraction and live-link status | Recheck authoritative sources; retain rate/access failures distinctly from missing records. |
| P2 | Grounded multimodal reasoning | Extract localization, hallucination, abstention, expert truth and leakage controls; captions are not physical evidence by themselves. |
| P2 | Adaptive sensing and reinforcement learning | Find actual observation-policy work with state/action/cost and closed-loop evaluation; do not substitute generic LLM reinforcement fine-tuning. |
| P2 | Scientific reproduction | Add reproducible data/version/split/code/environment artifacts before changing evidence level. No current entry claims this. |

## What fuller coverage requires

The [collection log](COLLECTION_LOG.md) reports what was actually searched and screened. Continued expansion should preserve a shared identity/provenance schema, add topic maintainers, and publish source/date/version coverage at each milestone. DOI/title checks should be followed by author/version review for suspicious near-duplicates.

Structured facets for storm type, geography, sensor, exact horizon and dataset license become useful once enough records have been read to populate them honestly. Current descriptions are not a harmonized benchmark. A performance leaderboard would require matched datasets, event definitions, splits, metrics and operational latency; no such equivalence is claimed here.
