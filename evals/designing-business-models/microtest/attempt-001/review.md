# Designing-business-models microtest review

Scorer: `business-model-micro-scorer-001`
Final rescorer: none

## Frozen inputs and integrity

- Rubric SHA-256: `726da76b63ebc82b6d60e0c045dde065a1b1f3b449c04a562233a9024d9d881a`
- Skill SHA-256: `fe50d245ee40ee68ee7e722089d83797f76ce62e3fd0a0e9a26608b933397ad0`
- The rubric hash was verified before response scoring.
- There are exactly five control and five guided repetitions, numbered 1 through 5.
- Every manifest has exactly the nine required keys and schema version 1.
- All ten manifest prompts exactly equal the rubric prompt.
- All control skill hashes are null; all guided skill hashes equal the current skill hash.
- All timestamps are valid UTC `Z` timestamps.
- All ten canonical task identifiers and all ten response hashes are unique.
- Every declared response SHA-256 matches the exact response bytes.
- The scorer did not edit the rubric, responses, or manifests.

## Strict scoring method

Each response was scored independently against all five frozen criteria. A criterion passed only when every material clause was explicit in that response. Aggregate evidence was not treated as a separate cohort record, a planned interview was not treated as a completed economic field, a dashboard metric was not treated as a decision threshold, and no owner, branch, effect, interpretation, comparison, or handoff was inferred.

## Scores

| Variant | Rep 1 | Rep 2 | Rep 3 | Rep 4 | Rep 5 | Mean | Population variance | Normalized |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Control | 0/5 | 0/5 | 0/5 | 0/5 | 0/5 | 0.0 | 0.0 | 0.00 |
| Guided | 4/5 | 4/5 | 4/5 | 3/5 | 4/5 | 3.8 | 0.16 | 0.76 |

The guided-minus-control normalized delta is **+0.76**. Neither variant produced a 5/5 repetition, so both all-criteria pass rates are 0.0.

Guided criterion pass rates were: criterion 1, 1.0; criterion 2, 0.0; criterion 3, 0.8; criterion 4, 1.0; criterion 5, 1.0. All control criterion pass rates were 0.0.

## Recurring misses

All control responses missed criterion 1 because they did not begin with the named primary skill and ordered routed handoffs. They also consistently omitted complete four-cohort economic records, fully specified commercial-test interpretations, supplier-versus-architecture failure attribution, and complete branch/effects/next-owner ledgers.

All five guided responses missed criterion 2. Each separated small/standard from high-volume/scale pharmacies, and several added an existing-renewed row, but none created a separate complete economic record for the non-renewed cohort. Cause coding or planned interviews did not explicitly fill user, buyer, payer, beneficiary, value event, willingness-to-pay evidence, sales/support effort, cost to serve, retention, and confounders for that cohort.

Guided rep 4 also missed criterion 3. It explicitly defined paid acceptance, list-price rejection, discount handling, cohorts, owner, dates, and numeric gates, but it did not predeclare how churn would be interpreted; “collect churn reason” and an aggregate retention gate did not distinguish price, effect, deployment, support, or other churn causes.

## Judgment

The guided variant is a material improvement: it raises the normalized score from 0.00 to 0.76 and passes ownership/routing, boundary analysis, and branch/effects/next-owner criteria in every repetition. The improvement is not complete. The skill still fails to bind agents to separate renewed and non-renewed economic records with the full field set, and one repetition shows that churn interpretation can still be omitted from an otherwise well-bounded commercial test.
