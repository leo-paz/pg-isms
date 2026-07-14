# Canonical microtest review: attempt 2

Scorer: `business-model-micro-scorer-002`
Final rescorer: none

## Strict method

I scored each frozen response independently against the five frozen criteria. A criterion passed only when every clause was explicit in the response; adjacent good practice or a reasonable inference did not fill a missing clause. Each criterion was binary, so each response had a possible score of 0–5.

For criterion 2, a per-site ledger counted as separate economic records when the response explicitly tagged each site by volume and renewal status and supplied the required actor, evidence, cost, retention, and confounder fields. For criterion 4, generic monitoring or portability did not count as supplier-versus-architecture failure evidence; the response had to attribute failures between the supplier and the startup's own interface, routing, inputs, or workflow. For criterion 5, aspirations to monitor retention or effects did not count as gates unless the branch was conditioned on those results.

## Pre-generation isolation proof

- Rubric SHA-256: `726da76b63ebc82b6d60e0c045dde065a1b1f3b449c04a562233a9024d9d881a`
- Generation-plan SHA-256: `1db521138c8dd59a0cabfc6e654c64828e14d91f55ccdf6b61ddd50d5228f939`
- Prompt projection SHA-256: `6d25e19d71639221af82c759db4632b4a8228269b9739436c5fdd515eaa68868`
- Criteria projection SHA-256: `c7a8aa272e0bbd62c9776353fe0b728c550c9fcd440fc03ad4606857d8becdb9`
- Guided skill SHA-256: `fe50d245ee40ee68ee7e722089d83797f76ce62e3fd0a0e9a26608b933397ad0`

The plan was created at `2026-07-14T21:16:03Z`, before every response `generated_at` and `frozen_at`. All response generation occurred with `criteria_visible_during_generation: false`, `criteria_hidden_during_generation: true`, and `prior_outputs_visible_during_generation: false`. Control manifests use a null skill hash; guided manifests use the current skill hash. All responses were frozen before the generation attestation completed at `2026-07-14T21:44:49Z` and before scoring began.

## Integrity result

All integrity checks passed:

- exactly five control and five guided responses;
- exactly ten manifests, each with the same exact 15 keys;
- exact prompt text and prompt hash identity across the rubric, plan, attestation, and every manifest;
- exact plan, rubric, criteria, and skill hashes;
- exact planned/completed task equality, including order, with the same task set in manifests;
- unique canonical tasks and unique response hashes;
- valid `plan created < generated <= frozen < attestation completed` ordering for all ten responses;
- exact response-byte hashes matching every manifest and the attestation hash map; and
- internally consistent plan, attestation, and per-manifest isolation flags.

Generation artifacts were not edited.

## Scores and exact misses

| Variant | Rep | Score | Missed criteria |
|---|---:|---:|---|
| control | 1 | 2/5 | 1, 2, 4 |
| control | 2 | 1/5 | 1, 2, 3, 5 |
| control | 3 | 0/5 | 1, 2, 3, 4, 5 |
| control | 4 | 1/5 | 1, 2, 3, 5 |
| control | 5 | 0/5 | 1, 2, 3, 4, 5 |
| guided | 1 | 5/5 | none |
| guided | 2 | 5/5 | none |
| guided | 3 | 5/5 | none |
| guided | 4 | 5/5 | none |
| guided | 5 | 5/5 | none |

The control misses were specific and repeated. All five omitted the primary `designing-business-models` owner and ordered artifact/result handoffs. All five stopped short of a complete four-way economic record across volume and renewal status. Four lacked a fully precommitted pricing interpretation for acceptance, rejection, discounting, and churn. Three did not explicitly distinguish supplier failure from startup architecture failure. Four lacked the complete combination of pricing/boundary branches, retention and accountable-effects gates, reversible option, and named next owner for every material result. The individual scorecards state the exact missing clauses and response evidence.

## Arithmetic

Control scores were `[2, 1, 0, 1, 0]`:

- mean: `4 / 5 = 0.8`
- population variance: `((2-0.8)^2 + (1-0.8)^2 + (0-0.8)^2 + (1-0.8)^2 + (0-0.8)^2) / 5 = 0.56`
- normalized score: `0.8 / 5 = 0.16`
- all-criteria pass rate: `0 / 5 = 0.0`
- criterion pass rates: `[0.0, 0.0, 0.2, 0.4, 0.2]`

Guided scores were `[5, 5, 5, 5, 5]`:

- mean: `25 / 5 = 5.0`
- population variance: `0.0`
- normalized score: `5.0 / 5 = 1.0`
- all-criteria pass rate: `5 / 5 = 1.0`
- criterion pass rates: `[1.0, 1.0, 1.0, 1.0, 1.0]`

Guided-minus-control deltas were `+4.2` mean points, `+0.84` normalized score, `+1.0` all-criteria pass rate, and criterion-rate deltas of `[+1.0, +1.0, +0.8, +0.6, +0.8]`.

## Material-improvement judgment

The guided condition is a material improvement. It moves every repetition to 5/5 and eliminates every criterion-level miss, while the control condition never produces an all-criteria pass. The improvement is also behaviorally specific: guided responses consistently add the primary owner and ordered handoffs, per-site economic records that can be sliced by volume and renewal, bounded price tests with predeclared interpretations, supplier-versus-architecture repair branches, and named post-gate owners. This is not a marginal wording change or a result driven by one repetition.
