# Managing runway and survival source re-audit

This draft records the independent source-review lineage behind the 28-essay evidence inventory. It does not reproduce source passages.

## Review lineage

| Reviewer | Assigned essays | Method and result |
|---|---:|---|
| `runway-source-a` | 11 | Audited essays `011`–`069` in its explicit non-overlapping batch; read complete relevant passages after BM25 and semantic QMD retrieval. |
| `runway-source-b` | 11 | Audited essays `076`–`116` in its explicit non-overlapping batch; read complete relevant passages after BM25 and semantic QMD retrieval. |
| `runway-source-c` | 10 | Audited essays `117`–`201` in its explicit non-overlapping batch; read complete relevant passages after BM25 and semantic QMD retrieval. |
| `runway-source-union` | 32 assigned; 28 retained | Verified the batches were disjoint and exhaustive, reran both retrieval modes for all 28 changed or disputed essays, read every complete local source, reconciled final ownership, and removed four non-owned essays. |

Every retrieval command used `PATH=/Users/leopaz/.nvm/versions/node/v22.23.0/bin:$PATH qmd --index graham-essays ...`. Decisions were made from complete local sources, not snippets.

## Reconciled ownership

The final source set retains 28 essays and exactly 85 essay-theme pairs across six owned canonical themes. Essays `029`, `048`, `089`, and `117` were removed; `129` was relabeled from runway survival to startup economics and risk.

| Essay | Final owned themes |
|---|---|
| `011` | `capital-efficiency-and-runway`; `revenue-and-profitability`; `runway-survival-and-profitability`; `startup-survival-and-failure` |
| `028` | `startup-economics-and-risk`; `startup-survival-and-failure` |
| `039` | `capital-efficiency-and-runway`; `revenue-and-profitability`; `startup-survival-and-failure`; `state-conditioned-spending-and-hiring` |
| `040` | `capital-efficiency-and-runway`; `startup-economics-and-risk`; `state-conditioned-spending-and-hiring` |
| `049` | `startup-economics-and-risk`; `startup-survival-and-failure` |
| `052` | `capital-efficiency-and-runway`; `state-conditioned-spending-and-hiring` |
| `053` | `capital-efficiency-and-runway`; `runway-survival-and-profitability`; `startup-survival-and-failure`; `state-conditioned-spending-and-hiring` |
| `068` | `capital-efficiency-and-runway`; `startup-survival-and-failure`; `state-conditioned-spending-and-hiring` |
| `069` | `capital-efficiency-and-runway`; `revenue-and-profitability`; `runway-survival-and-profitability`; `startup-survival-and-failure`; `state-conditioned-spending-and-hiring` |
| `076` | `capital-efficiency-and-runway`; `startup-survival-and-failure` |
| `077` | `capital-efficiency-and-runway`; `state-conditioned-spending-and-hiring` |
| `081` | `startup-survival-and-failure` |
| `084` | `capital-efficiency-and-runway`; `startup-economics-and-risk` |
| `097` | `revenue-and-profitability`; `runway-survival-and-profitability` |
| `098` | `capital-efficiency-and-runway`; `revenue-and-profitability`; `runway-survival-and-profitability`; `startup-survival-and-failure`; `state-conditioned-spending-and-hiring` |
| `099` | `capital-efficiency-and-runway`; `startup-economics-and-risk`; `startup-survival-and-failure`; `state-conditioned-spending-and-hiring` |
| `102` | `capital-efficiency-and-runway`; `revenue-and-profitability`; `runway-survival-and-profitability`; `startup-economics-and-risk`; `state-conditioned-spending-and-hiring` |
| `105` | `capital-efficiency-and-runway`; `revenue-and-profitability`; `runway-survival-and-profitability`; `startup-survival-and-failure` |
| `116` | `capital-efficiency-and-runway`; `revenue-and-profitability`; `runway-survival-and-profitability`; `startup-survival-and-failure` |
| `129` | `startup-economics-and-risk` |
| `137` | `capital-efficiency-and-runway` |
| `156` | `capital-efficiency-and-runway`; `revenue-and-profitability`; `runway-survival-and-profitability`; `state-conditioned-spending-and-hiring` |
| `159` | `capital-efficiency-and-runway`; `revenue-and-profitability`; `runway-survival-and-profitability`; `startup-survival-and-failure`; `state-conditioned-spending-and-hiring` |
| `168` | `capital-efficiency-and-runway`; `revenue-and-profitability` |
| `169` | `capital-efficiency-and-runway`; `runway-survival-and-profitability`; `startup-survival-and-failure`; `state-conditioned-spending-and-hiring` |
| `195` | `capital-efficiency-and-runway`; `revenue-and-profitability`; `runway-survival-and-profitability`; `startup-survival-and-failure` |
| `198` | `runway-survival-and-profitability`; `state-conditioned-spending-and-hiring` |
| `201` | `capital-efficiency-and-runway`; `startup-economics-and-risk` |

Theme counts: 22 `capital-efficiency-and-runway`, 12 `revenue-and-profitability`, 13 `runway-survival-and-profitability`, 8 `startup-economics-and-risk`, 16 `startup-survival-and-failure`, and 14 `state-conditioned-spending-and-hiring`.

## Projection collision review

The first executable override plan produced the exact 85 owned pairs but displaced valid themes already used by other skills in essays `011`, `039`, `069`, `116`, and `201`. The final article-scoped placements preserve those prior themes while producing the same runway source set. Every existing package provenance check passes, and the 201 placement preserves its user-acquisition ownership.

## Citation normalization

The union review preserved its complete claim ranges in the ignored review artifact. Where a union range crossed two canonical audit intervals, the public evidence inventory splits it into contained intervals; where only an audited subrange was needed, it cites that narrower exact support. This keeps provenance mechanically reciprocal without expanding claims or weakening validation.

## Boundary and copyright controls

- Route financing process and deal terms to `raising-and-governing-capital`; route normal monetization architecture to `designing-business-models`.
- Route user discovery to `learning-from-users` and ordinary hiring without a cash-state predicate to `building-and-evolving-organizations`.
- Treat dated market amounts, cost curves, and credit-card anecdotes as historical context requiring revalidation, not current prescriptions.
- Keep claims as concise paraphrases and resolve the exact ranges against `/Users/leopaz/dev/opensource/graham-essays/corpus` when deeper context is required.
