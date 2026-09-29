# Collection log / 检索与搜集记录

Snapshot: **2026-09-29**. The collection contains **930 records**, spanning **1872–2026** and **15 directions**: **163 annotated** and **767 bibliographic**. Each entry links to a primary publication or institutional record. **20 entries have verified code links: 19 GitHub links and one Code Ocean archive.** See the generated [code index](../papers/CODE_INDEX.md) and [statistics](../data/stats.json).

“Annotated” means that an original description of the task, method and inputs is present. It does not mean full-text audit or independent reproduction. “Bibliographic” means that identity and topical relevance were screened from the title, venue and deposited metadata; methods and findings remain unextracted. These labels can be filtered in the web explorer and are exported in CSV.

## How this edition was expanded

| Stage | Retrieval and screening | Outcome |
|---|---|---|
| Initial publisher/author searches | AMS, NOAA, NASA, UCAR, journal and institutional pages; classical-to-modern method searches | Original 67 records expanded to 155; 88 additions and 17 completed author lists. |
| 2026 arXiv sweep | Exact title/abstract query for tornado/tornadic, submitted 2026-01-01 through 2026-09-29; limit 200 | API reported 24 results. Five were already indexed; 19 new candidates were screened, with 11 included and eight excluded. These additions are already included in the 155 above. |
| Broad bibliography pass | 36 query families; 33 successful responses, three HTTP 429 failures; 40–200 results requested per query | 1,000 distinct matching titles/DOIs retrieved; 949 new candidates screened. After version review: 770 included records, 92 excluded, 86 pending, one merged duplicate. |
| Primary-source follow-up | Classic vortex dynamics and Chinese journal/institutional pages | Five additional annotated papers; three of the broad-pass records upgraded to annotated. |
| Code/publication follow-up | Author project pages, publisher code sections, CVF and NOAA repositories | 20 total code links; ASTRA and TorDet publication metadata reconciled; Shakya et al. linked to its CVPR 2026 workshop publication; Weather-R1 matched to the official ICASSP program. |

The arithmetic is **155 + 770 + 5 = 930**. The 770 broad-pass additions now comprise three annotated and 767 bibliography-only entries. The 163 annotated entries comprise the first 155, those three upgrades and five follow-up additions. Stage counts must not be added twice.

## Queries and decisions that can be inspected

- [Initial expansion](../data/curation/2026-09-29-expansion.json): individual added identities, source URLs and metadata corrections.
- [arXiv query and decisions](../data/curation/2026-09-29-arxiv.json): exact query URL, date window, requested limit, reported result count and inclusion/exclusion reasons.
- [Broad bibliography audit](../data/curation/2026-09-29-bibliography.json): successful query URLs and caps; every new candidate's DOI, title, topic and decision; failed query names are retained.
- [Primary-source follow-up](../data/curation/2026-09-29-source-followup.json): additional Chinese/classical sources, annotation upgrades, code provenance and the workshop publication update.

The broad pass covered historical/cited/recent work, radar and polarimetry, mesocyclones, intensity, forecasting, statistical ML, deep learning, multimodal work, remote-sensing damage, numerical and laboratory simulations, wind engineering, fragility, debris, waterspouts, nonsupercell/QLCS/tropical-cyclone tornadoes, environments, climatology, warnings, health/social response, regional studies, infrasound/lightning, assimilation, field campaigns and Chinese keywords.

Crossref's relevance search for multiword queries can return unrelated titles. The provider's `total` field is not a count of relevant tornado papers. Candidates were restricted by tornado-related titles and manually screened using title/venue evidence. Software called Tornado, Tornado Cash, solar/optical tornadoes, generic optimization names and metaphorical uses were excluded. Ambiguous genre/identity and insufficient author/venue information remain pending rather than being counted as accepted literature.

The [code availability check](../data/curation/2026-09-29-code-availability.json) confirmed 19 GitHub repositories via the public API. The NowcastNet DOI resolved to Code Ocean, whose automated response was HTTP 403; no capsule download or execution is claimed. This audit also records the official ICASSP 2026 program entry for Weather-R1.

## Version and authorship decisions

- Brotzge, Erickson and Brooks' 2011 false-alarm paper has early-online DOI `10.1175/waf-d-10-05004` and final DOI `10.1175/waf-d-10-05004.1`. It is counted once; both sources are retained.
- ASTRA was available online on 6 August 2026 but assigned to a January 2027 issue. Its record uses the available-online year 2026 and retains arXiv:2602.14523. This is not a second paper.
- TorDet's 2026 journal volume uses a DOI containing 2025. A DOI suffix is not automatically the publication year or a preprint year.
- Shakya et al.'s arXiv paper and CVPR 2026 Workshops (AI4RWC) publication are one record, with both sources retained.
- The 1884 Science item “Tornado Predictions” has only `G.` in the deposited author field. Authorship remains incomplete; it is not assigned to Finley by inference.
- Two fire-tornado simulation presentations in the 2014 and 2015 Tohoku proceedings are retained as distinct bibliographic records with explicit unresolved content-overlap notes. They are not asserted to be independent experiments.

## Limits that remain

This is a substantial expansion, **not an exhaustive search of all tornado literature**. The broad retrieval was capped; historical, ML and East-Asia query attempts returned HTTP 429. Related successful queries still cover some of those topics, but do not prove completeness. Chinese full-text databases, dissertations, monographs, conference archives and non-English national collections have not been searched comprehensively. Most new entries have no method-level annotation yet. All repository links identified here are source-backed, but absence of a code link means “not verified,” not “no code exists.”

No experiments were reproduced, no full-text screening completeness is claimed, and live availability/retraction status was not individually audited for every external URL. A DOI link is a persistent publication identifier, not a guarantee of open full text. See the [search protocol](SEARCH_PROTOCOL.md) and [remaining work](RESEARCH_GAPS.md).
