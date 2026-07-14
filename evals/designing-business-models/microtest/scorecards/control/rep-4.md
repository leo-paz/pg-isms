# Control rep 4 scorecard

- Scorer: `business-model-micro-scorer-003`
- Score: **1/5**
- Normalized score: **0.2**
- Response SHA-256: `38fc602aa224e88381125ae1fd9d527c4b480e10d6bdc8df906f02b3f4fd489c`
- Skill SHA-256: `fe50d245ee40ee68ee7e722089d83797f76ce62e3fd0a0e9a26608b933397ad0`
- Rubric SHA-256: `726da76b63ebc82b6d60e0c045dde065a1b1f3b449c04a562233a9024d9d881a`
- Generation plan SHA-256: `1db521138c8dd59a0cabfc6e654c64828e14d91f55ccdf6b61ddd50d5228f939`
- Prompt SHA-256: `6d25e19d71639221af82c759db4632b4a8228269b9739436c5fdd515eaa68868`
- Criteria SHA-256: `c7a8aa272e0bbd62c9776353fe0b728c550c9fcd440fc03ad4606857d8becdb9`
- Generation attestation SHA-256: `5a791a946e8a79d273df2fc8aa989231e3243becbdbccec8c10797c5e4a11ec5`

| Criterion | Pass | Strict rationale |
|---:|:---:|---|
| 1 | No | The response has role assignments but does not name `designing-business-models` as primary or begin with the required ordered handoffs. |
| 2 | No | The all-site dataset in lines 11–22 is useful, but it does not distinguish the full required actor, payer, beneficiary, value-event, willingness-to-pay, effort, retention, and confounder record for each required cohort. |
| 3 | No | Lines 24–45 and 62–66 define unusually strong prices, cohorts, dates, owners, and thresholds. It still fails the strict conjunction because churn is not given a predeclared pricing/sales-test interpretation or retention branch; attribution of partner-related churn in line 78 is a boundary diagnostic instead. |
| 4 | Yes | Lines 47–80 cover channel coordination cost, integration funding, exclusivity, termination, capital, six-month delay, capability, SLA quality, interface portability, alternate switching, and evidence that lost deals, churn, or limitations are actually partner-caused before expansion or build. |
| 5 | No | Pricing and boundary branches and a reversible adapter exist, but the final gate omits a complete retention-plus-accountable-effects threshold and branch-specific next owners. |

Misses: criteria **1, 2, 3, 5**.
