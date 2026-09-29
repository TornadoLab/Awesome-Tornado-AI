# Contribute a signal

We welcome foundational, traditional, modern-AI and critical/negative-result work. Quality means a clear task and traceable evidence—not fashionable architecture names or high headline scores. Contributions may be written in English or Chinese; keep both short annotation fields useful.

## Add or correct a paper

Edit only the canonical record in `data/papers.json`; use `data/paper.schema.json` as a field reference. Supply the exact title, year, author list, venue, publication status and primary source. DOI/arXiv/code fields may be `null` when not verified. Do not fabricate them. A final journal article and its preprint should normally share one record.

`scope` must be `direct`, `context` or `transfer`. Choose a primary category by the scientific question, and put secondary methods in `method`. Describe actual inputs and targets in `inputs` and `target_and_horizon`; do not invent a numeric horizon when the source does not establish it. Cite a maximum-case lead time as such, not as average operational warning benefit.

Set `record_type` to `annotated` only when an original task/method annotation is supplied from the source. Use `bibliographic` for title/author/venue/identity screening with detailed reading still pending, and explicitly leave method/input/horizon fields unextracted. Both types must have a primary-source link. Do not paste abstracts or publisher figures. State a real limitation or unresolved metadata question in `caveat`. Keep `sources` for primary provenance and corrections; use author- or institution-linked repositories for code, and disclose when only inference or a partial release is available. A code archive such as Code Ocean is acceptable; do not relabel it GitHub.

New contributions should supply full author lists where available. Records with `authors_complete: false` are explicit metadata debt; they are not examples of manuscript-ready citations. The broader bibliography follows publisher-deposited lists, which may still contain errors or abbreviated names. Raise `verification.level` only with supporting evidence as defined in [the search protocol](guides/SEARCH_PROTOCOL.md).

Run:

```bash
python tools/validate.py
python tools/build.py
python tools/build.py --check
python -m unittest discover -s tests -v
node --check docs/app.js
```

Include the generated diffs in the PR. Explain why the paper belongs, which primary source was checked, what changed, and whether the update affects a reading route. The add-paper and correction issue forms are available when you are not editing JSON directly.

## Scientific interpretation

Do not label every weather-AI paper “tornado forecasting.” Keep detection, onset prediction, severity, reflectivity nowcasting, damage recognition and forecaster decision support distinct. Do not add a leaderboard row without a matched dataset/split/target/metric protocol. Do not call a preprint peer-reviewed without a verified publication record.

## Automation and security

The arXiv scout returns unreviewed candidates; a maintainer decides admission. CI only checks metadata/code integrity, not scientific correctness. No contributor PR should require credentials, execute downloaded papers, add trackers or enable automatic publication of unreviewed results. External network tests are not part of default PR CI.

Original prose contributions are offered under CC BY 4.0; original code, website and artwork under MIT. Authors retain rights in the works being indexed. See [LICENSE](LICENSE). Please follow the [code of conduct](CODE_OF_CONDUCT.md).
