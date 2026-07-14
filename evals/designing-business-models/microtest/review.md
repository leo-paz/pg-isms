# Designing-business-models canonical microtest review

Scorer: `business-model-micro-scorer-003`
Scored at: `2026-07-14T22:07:34Z`

## Result

The guided responses show material improvement under the frozen five-criterion binary rubric.

| Variant | Scores | Mean | Population variance | Normalized score | All-criteria passes |
|---|---|---:|---:|---:|---:|
| Control | `[0, 1, 0, 1, 0]` | 0.4 | 0.24 | 0.08 | 0/5 |
| Guided | `[5, 5, 5, 5, 5]` | 5.0 | 0.0 | 1.00 | 5/5 |

**Guided minus control normalized delta: `+0.92`. Material improvement: yes.**

The result is both large and consistent: the guided condition adds 23 criterion passes across 25 possible response-criterion cells and has zero score variance.

## Criterion-level result

| Criterion | Control passes | Guided passes | Assessment |
|---:|---:|---:|---|
| 1 | 0/5 | 5/5 | Guided responses consistently name the primary skill, begin with ordered handoffs, and route billing/interface/channel artifacts to the required next owners. |
| 2 | 0/5 | 5/5 | Guided responses use per-site records more granular than the required cohorts, keyed by volume and renewal state, while explicitly preserving actors, behavioral payment evidence, acquisition/support effort, cost to serve, retention, and confounders. Controls collect useful economics but omit at least one required distinction or field. |
| 3 | 0/5 | 5/5 | Guided responses consistently predeclare complete acceptance, rejection/change, discount, churn/retention, segment, and stop interpretations. Controls provide useful tests but leave at least one interpretation implicit. |
| 4 | 2/5 | 5/5 | Control reps 2 and 4 pass because they explicitly attribute courier failures against startup/product failure as part of an otherwise complete boundary comparison. The other controls omit that strict conjunct. All guided responses include supplier-versus-architecture attribution. |
| 5 | 0/5 | 5/5 | Guided responses combine pricing and boundary branches with retention, accountable effects, reversible options, and result-specific next ownership. Controls omit at least one of those conjuncts. |

The strict binary method gives no partial credit. For example, a detailed control price test still misses criterion 3 if it merely records discounts or churn without specifying in advance how those observations change the decision. Likewise, a detailed boundary comparison misses criterion 4 if it does not distinguish supplier failure from startup interface or architecture failure.

## Response-level result

- Control reps 1, 3, and 5: `0/5`.
- Control reps 2 and 4: `1/5`, passing criterion 4 only.
- Guided reps 1–5: `5/5` each.

The individual evidence and strict miss explanations are in `scorecards/control/rep-1.md` through `rep-5.md` and `scorecards/guided/rep-1.md` through `rep-5.md`.

## Integrity review

The frozen-input and isolation checks passed:

- Rubric SHA-256: `726da76b63ebc82b6d60e0c045dde065a1b1f3b449c04a562233a9024d9d881a`.
- Generation-plan SHA-256: `1db521138c8dd59a0cabfc6e654c64828e14d91f55ccdf6b61ddd50d5228f939`.
- Generation-attestation SHA-256: `5a791a946e8a79d273df2fc8aa989231e3243becbdbccec8c10797c5e4a11ec5`.
- Skill SHA-256: `fe50d245ee40ee68ee7e722089d83797f76ce62e3fd0a0e9a26608b933397ad0`.
- Prompt SHA-256: `6d25e19d71639221af82c759db4632b4a8228269b9739436c5fdd515eaa68868`; criteria SHA-256: `c7a8aa272e0bbd62c9776353fe0b728c550c9fcd440fc03ad4606857d8becdb9`.
- Every manifest has exactly the same required 15 keys, and task, rep, variant, model, prompt, plan, isolation, response, and skill-hash fields match the frozen plan and attestation.
- All ten response file hashes match their manifests and the attestation.
- Guided rep 5 has SHA-256 `f6e24a2c4b9b26a7019194cb130281cdd5d7b68ae5d3d2d706d3ed75bf665b90` and was frozen at `2026-07-14T22:01:50Z`.
- The plan was created at `2026-07-14T21:16:03Z`; all generations and freezes followed it; the final freeze preceded attestation completion at `2026-07-14T22:03:47Z`; attestation preceded scoring at `2026-07-14T22:07:34Z`.
- All ten canonical responses contain zero trailing horizontal-whitespace matches.
- No generation response, manifest, plan, rubric, attestation, or skill artifact was edited during scoring, and no prior scorecard, summary, review, attempt, baseline, forward, held-out, provenance, research, README, progress, or `.superpowers` content was used.
