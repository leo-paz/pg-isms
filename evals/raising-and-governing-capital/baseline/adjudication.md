# RED baseline adjudication

Adjudicator: `capital-baseline-adjudicator-001`
Scope: only scenario 02 criterion 2 and scenario 03 criterion 1
Rule: a bit is `1` only when every clause is explicit. Missing details are not inferred, and a backticked workflow name is an explicit routing requirement.

## Verdicts

| Dispute | Prior strict | Independent | Adjudicated |
|---|---:|---:|---:|
| Scenario 02, criterion 2 | 0 | 1 | **0** |
| Scenario 03, criterion 1 | 0 | 1 | **0** |

### Scenario 02, criterion 2: fail (`0`)

- Headline ownership arithmetic passes. Response line 9 gives “about 11.11%” for A and “about 11.29%” for B.
- Option-pool placement passes. Line 11 contrasts “funded post-money” with “funded pre-money” and says the headline “does not establish that B is less dilutive.”
- Participation passes. Lines 3 and 19 contrast the higher headline with materially worse economic downside and explain that participation can “reduce what common holders receive.”
- Anti-dilution passes. Lines 21 and 29 explain “substantial additional dilution” from the full ratchet and say the protection matters more than the headline difference.
- Capitalization definitions fail. Lines 11 and 33 request a “fully diluted capitalization table” and capitalization model, but never identify a governing capitalization definition or explain how such a definition changes the ownership denominator or economics. A cap-table request is not the required definition analysis.
- The ultimate conclusion is explicit at lines 3, 11, and 29, but the criterion requires every listed reason to be explicitly connected. The missing capitalization-definition clause forces `0`.

### Scenario 03, criterion 1: fail (`0`)

- Exact primary routing fails. Lines 1–3 select “cash survival and retention,” but never select `managing-runway-and-survival`. The paraphrase cannot satisfy the explicit backticked route.
- Explicit default-dead classification fails. Line 5 gives “only about 4.4 months of runway,” flat revenue, and fragile churn, but never states the default-dead conclusion. Inferring it is disallowed.
- The only-after survival gate fails. Line 3 calls fundraising a “supporting workflow,” and lines 11–13 date a forecast and survival plan for July 22. But line 23 broadly authorizes preparing, meeting, negotiating, and closing without conditioning that work on completion of the survival envelope; line 31 proceeds with late-July capital deliverables. Suggested chronology is not an explicit gate.
- Non-cash treatment passes. Lines 5, 23, and 31 exclude the unapproved lead and soft circles from the base case, prohibit counting soft circles as cash or presenting the venture firm as committed, and retain the soft-circle label until documents are signed and funds arrive.
- Three required clauses fail, so the conjunctive result is `0`.

## Authoritative result

- Vector: `00000 00000 00000 00000 01000`
- Expanded: `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]`
- Score: **1/25 (4%)**
- Per scenario: `0, 0, 0, 0, 1`

This exactly matches `capital-baseline-scorer-001`. It differs from `capital-baseline-auditor-001` only on the two adjudicated bits, reducing that review's 3/25 result by two points.

## Integrity and freeze readiness

Only `cases.json`, the two frozen responses, `strict-score.json`, and `independent-review.json` were inspected. No source essay, taxonomy, skill package, intended source material, or unrelated skill artifact was opened. The current scenario-response SHA-256 values match the values recorded by both reviews; both allowed reviews report passing frozen blind no-skill integrity. No separate generation artifact was needed for the two-bit content decision.

`red_valid: true` — 24 of 25 criteria fail, and every scenario retains a failure.
`ready_to_freeze_red: true` — both disputes are resolved under the stated strict rule, and the 23 agreed bits remain unchanged.
