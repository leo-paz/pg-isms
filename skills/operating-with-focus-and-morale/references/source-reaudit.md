# Focus source re-audit

Reviewer: `skill12-pair-reaudit-gpt5-20260715`

The final package review identified two canonical article/theme pairs whose review
lineage had been assigned to a reviewer that did not inspect those exact pairs. A
fresh reviewer used both BM25 and semantic QMD retrieval, then read each full essay.

## Article 126: `resourcefulness-and-agency`

Disposition: **removed**.

Lines `18-26` support fake-work alarms and concrete-output checks, but not the
canonical theme's purposeful autonomy or obstacle-navigation mechanism. The prior
claim also inferred a repeated behavior-change loop that the source does not state.
Article 126 remains incorporated under `attention-and-priority-control`.

Retrieval used `qmd --index graham-essays search 'fake work alarm produced result'`,
the refined BM25 query `search 'self-indulgent work alarm'`, and semantic query
`vsearch 'When respectable-looking activity repeatedly produces no concrete result,
install an explicit alarm and change how you act instead of trusting the appearance
of work.'`; the complete `126_how-to-lose-time-and-money.md` (`1-30`) was read.

## Article 147: `attention-and-priority-control`

Disposition: **retained**.

Lines `16-22` directly support changing defaults where possible and turning
consequential omissions into short commands at the actual planning surface. This is
an attention/default-control mechanism, not a general method for ranking company
initiatives.

Retrieval used BM25 query `search 'todo list errors omission default'` and semantic
query `vsearch 'Keep consequential priorities from disappearing through default
omission by turning them into short visible commands on the task list you actually
revisit.'`; the complete `147_the-top-of-my-todo-list.md` (`1-26`) was read.

Every QMD command used the required Node PATH and `--index graham-essays` invocation.
