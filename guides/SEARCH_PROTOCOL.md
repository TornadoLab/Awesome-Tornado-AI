# Curation and search protocol

**Edition:** 0.2.0. **Snapshot:** 2026-09-29. **Claim:** a broad source-linked research atlas, with explicit bibliographic and annotated stages. This is not a PRISMA review or an exhaustive bibliography.

## Sources and retrieval

Use original publisher/institutional records, author project pages and deposited Crossref metadata. The current edition combines targeted AMS, NOAA, NASA, UCAR, Nature/Science, PNAS, IEEE, Wiley, Springer, MDPI, PMLR, CVF, Chinese journal and arXiv searches with a broader Crossref title/venue pass. Evidence for the dated expansion, including caps and unsuccessful requests, is linked from the [collection log](COLLECTION_LOG.md). Public Awesome lists inform organization, not scientific truth.

Query families include early observations, vortex dynamics, radar signatures, detection/tracking, rating and wind inference, statistical forecasting, ML/deep learning, multimodal reasoning, numerical simulation and assimilation, field campaigns, remote-sensing damage, engineering, climatology, warning verification, social response and regional/non-supercell tornado families. Search both English and original-language terms such as 龙卷、识别、检测、分级、预测、数值模拟、水龙卷、灾损. A single English keyword search cannot establish international completeness.

Record the query, date window, provider, result cap, returned count, retrieval failure and per-candidate decision. Provider result totals are not counts of relevant studies. Capped queries and failed requests remain explicit limitations. Do not bypass rate limits; retain the failure or retry later with appropriate backoff.

## Identity, time and relevance

One final paper and its preprint normally share a record. Compare DOI, normalized title, authors, venue and version history; exact DOI/title checks alone do not catch every duplicate. Use a journal issue year when established and already within the snapshot, otherwise an established available-online year with an explicit caveat. Keep first-preprint year separately. DOI suffixes and upload dates do not by themselves determine publication year. Retain correction/retraction sources when found; their absence is not proof that none exists.

Include direct tornado understanding, identification, detection, rating, prediction, impacts and response as `scope: direct`. Related severe-storm/operational methods and physical analogues are `context`; general weather AI that could transfer is `transfer`. These are relevance labels, not rankings. Engineering/health papers may legitimately study tornado consequences without being meteorological models.

Exclude software frameworks, cryptocurrency mixers, unrelated vortex/optimization names, solar/optical tornadoes and metaphorical uses. Hold incomplete or ambiguous identities for review. Never inflate the accepted count using unresolved search hits. Do not mirror copyrighted abstracts, figures or full papers.

## Entry detail and evidence are different fields

| Field | Meaning |
|---|---|
| `record_type: bibliographic` | Title, authors, venue, identifier and topical relevance screened; detailed method, input, target and result extraction pending. Explicit pending fields are required. |
| `record_type: annotated` | Original task/method/input/target notes supplied from source material. This does not imply a full-text audit. |
| `verification.level: metadata` | Bibliographic identity and, where annotated, abstract/source-level description checked. No full-text or experimental audit claimed. |
| `verification.level: full_text` | Full paper read; methods/splits/limitations recorded with page/section evidence. Still not reproduction. |
| `verification.level: reproduced` | Additionally requires a public reproduction artifact with data version, split manifest, commit and environment. |

All records in this edition remain at `metadata`, with `reproduced: false`. An official GitHub repository does not raise the evidence level. Author lists follow the cited source; set `authors_complete: false` for unresolved identities or partial lists. Even a complete deposited list may require correction before manuscript submission.

## Paper and code links

Every accepted record needs an HTTPS primary-source URL and provenance. Retain a DOI/arXiv link where verified. For `code_url`, require the authors, publisher, project page or responsible institution to establish the paper/repository relationship. Note an inference-only release, partial code or restricted dataset. Code Ocean and other author-linked archives are valid code destinations but should not be called GitHub repositories. Third-party implementations can be listed as such in resources; do not silently treat them as authors' code.

Missing `code_url` means **not verified in this snapshot**. It does not mean unavailable. URL syntax checks are not live availability tests; HTTP 403/429 can be access restrictions. A reachable URL is not evidence that the reported scientific result is correct.

## Updating

1. Resolve the paper's identity and version against existing DOI/arXiv/title/author records.
2. Screen relevance and bibliographic metadata. Use `bibliographic` if deeper reading is unfinished.
3. For `annotated`, inspect the abstract/full text and describe actual method, input, target and horizon in original words; keep unknown values explicit.
4. Add scope, primary links, verified code provenance, limitations and checked date. Keep maximum-case lead time distinct from typical operational performance.
5. Validate, regenerate and review the catalog, exports and site before committing.

The optional arXiv scout generates a review queue only. It neither covers all databases nor silently promotes candidates. Full search logs and pending queues should remain available for the next editorial pass.
