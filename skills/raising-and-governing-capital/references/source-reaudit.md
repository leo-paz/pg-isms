# Raising and governing capital source re-audit

This file records the independent source-review lineage behind the public
42-essay evidence inventory. It does not reproduce source passages.

## Disjoint audit coverage

| Reviewer | Assigned essays | Retrieval and full-read proof |
|---|---:|---|
| `capital-source-a` | 17 | Essays `033,039,040,046,048,049,050,052,053,061,067,069,073,076,078,084,085`; 34 BM25 queries, 37 semantic queries, and 17 complete line-numbered local reads. |
| `capital-source-b` | 16 | Essays `088,089,092,098,102,105,109,116,123,127,129,131,133,136,137,145`; 16 BM25 queries, 16 semantic queries, and 16 complete line-numbered local reads. |
| `capital-source-c` | 16 | Essays `149,150,152,154,155,156,159,165,169,174,176,182,196,198,199,201`; 16 BM25 queries, 16 semantic queries, and 16 complete line-numbered local reads. |

The three ID sets are pairwise disjoint and their union exactly equals the 49
essays initially assigned to this skill. Every reviewer used
`PATH=/Users/leopaz/.nvm/versions/node/v22.23.0/bin:$PATH qmd --index graham-essays`
with both `search` and `vsearch`, then based each decision on the complete local
corpus file rather than retrieval snippets.

The independent `capital-source-union` reviewer reran BM25, semantic retrieval,
and a complete local read for all 40 changed or disputed essays:
`033,039,048,052,053,061,067,069,073,076,084,085,089,092,098,102,105,109,116,123,129,131,133,136,137,149,152,154,155,156,159,165,169,174,176,182,196,198,199,201`.
The nine unchanged essays remained covered by their independent batch full reads.

## Reconciled source set

Retained 42 essays:
`033,039,040,046,049,050,052,053,061,067,069,076,078,084,085,088,092,098,102,105,109,116,123,127,129,131,133,136,137,145,149,150,152,154,155,156,165,174,176,182,196,201`.

Removed seven false or boundary triggers:

| Essay | Specific reason and route |
|---|---|
| `048` | Career ownership and liquidity optionality are not startup financing terms or investor governance; route to founder preparation and calibrated decisions. |
| `073` | Personal commitment and independence are founder-readiness evidence, not financing control; route to founder preparation, opportunity choice, and founder partnership. |
| `089` | Maker autonomy inside an organization is not control created by a financing round; route to founder preparation, organization building, and calibrated decisions. |
| `159` | A fatal pinch is a survival-first non-trigger; route to `managing-runway-and-survival` before considering rescue financing. |
| `169` | Default-dead diagnosis and its contingency belong to survival planning, not raise execution; route to runway survival and state-conditioned organization work. |
| `198` | Historical investor dependence is memoir evidence rather than a reusable round procedure; route operating lessons to runway/organization, accelerator history to ecosystem/advising, and deal details to historical context. |
| `199` | Restricted nonprofit donations are too remote an analogy and would falsely trigger startup-capital guidance; route operator-trust reasoning to advising and calibrated decisions. |

The retained inventory contains exactly 146 essay-theme pairs across the ten
owned canonical themes:

| Theme | Essays |
|---|---:|
| `deal-mechanics-and-terms` | 12 |
| `financing-terms-equity-and-control` | 16 |
| `founder-autonomy-and-control` | 14 |
| `funding-market-conditions` | 13 |
| `funding-stage-fit` | 15 |
| `fundraising-readiness-and-investor-communication` | 10 |
| `fundraising-strategy-and-process` | 20 |
| `investor-incentives-and-selection` | 21 |
| `investor-truth-trust-and-reputation` | 14 |
| `valuation` | 11 |

## Canonical application and citation verification

The union plan used 68 article-scoped occurrence actions: 63 additions and five
replacements, with no global raw-theme mapping change. Its simulation reported
zero collisions, zero unrelated-theme collateral, zero non-scope article changes,
and no existing implemented-skill membership change. The applied canonical state
reproduces the exact 42 essays and 146 owned pairs. The normalization-revision,
theme-projection, and taxonomy check modes all pass, and all 13 previously
implemented package provenance checks remain byte-current.

Every source URL, corpus path, and corpus SHA-256 in the inventory was checked against
the local corpus snapshot. All 49 files match; all 342 cited ranges are in bounds;
and all 303 retained theme-evidence ranges are contained within committed audit
intervals. Crossing ranges were split or narrowed rather than expanding canonical
audit evidence. Article `069`'s auxiliary singleton citation at line 230 was omitted
from the public inventory because it lies outside the committed audit intervals and the
same valuation, term, board, and control claim is directly supported at `152-164`.

## Conditions, boundaries, and copyright controls

- Preserve stage, venture, and market predicates. Capital-light software, long-build
  or capital-heavy ventures, seed and later rounds, hot and weak markets, and
  survival financing do not share one invariant playbook.
- Route default-dead, payroll-threatening, or fatal-pinch states to
  `managing-runway-and-survival` first. Route whether outside capital fits the
  venture to `designing-business-models`; employee equity to organization building;
  cofounder ownership to founder partnership; and acquisition choices to exits.
- Treat instruments, securities, tax, fiduciary duties, signed documents, and
  governance implementation as current-data and qualified-counsel questions.
- Revalidate every dated dollar amount, percentage, instrument, named investor,
  fund structure, valuation, board norm, market forecast, accelerator practice,
  location claim, and evidence expectation before application.
- Keep only concise paraphrases, source URLs, essay IDs, hashes, and exact ranges.
  A direct 20-, 30-, and 40-word overlap scan across 477 public prose segments found
  zero corpus matches at every window size.
