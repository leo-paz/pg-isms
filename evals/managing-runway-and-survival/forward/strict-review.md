# Strict forward review: managing-runway-and-survival

Reviewer: `runway-forward-scorer-001`
Model: `Codex (GPT-5)`
Method: conjunctive binary scoring; a criterion earns 1 only when every clause is explicit in the frozen response.

## Result

- Forward: **18/25 = 0.72 (72%)**
- Baseline: **5/25 = 0.20 (20%)**
- Delta: **+13 criteria, +0.52 normalized**
- Minimum required improvement: **+0.10**
- `forward_valid`: **true**

The forward run is valid because every response hash, byte count, and word count matches the frozen attestation, all responses are within the 1,200-word limit, and the normalized improvement is +0.52.

## Exact vectors

| Case | Vector | Score |
|---|---:|---:|
| scenario-01 | `[1, 1, 0, 1, 1]` | 4/5 |
| scenario-02 | `[1, 0, 0, 0, 1]` | 2/5 |
| scenario-03 | `[1, 1, 0, 0, 1]` | 3/5 |
| scenario-04 | `[1, 1, 0, 1, 1]` | 4/5 |
| scenario-05 | `[1, 1, 1, 1, 1]` | 5/5 |
| **Total** | `[1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1]` | **18/25** |

## Integrity verification

| Case | SHA-256 | Words | Bytes | Result |
|---|---|---:|---:|---|
| scenario-01 | `0231611615ad003b30e8d0b88e29ac0a07c3b607f77bf9c3d6ef3c78245c98a4` | 1090 | 7319 | match; within limit |
| scenario-02 | `3fae01f710fff29348698a56d90bd94b0528b2ad2df59ee880db4df1cc40c97c` | 1132 | 7454 | match; within limit |
| scenario-03 | `33a1d1fafd81a19b5607c6b70892cebfa8b069b222d8d1b4346439b5a6eb616b` | 1148 | 7337 | match; within limit |
| scenario-04 | `f495601b26aa247e6d0b34e6e0529a6a03c0504e866ca1a08d8bc6618453b115` | 1149 | 7701 | match; within limit |
| scenario-05 | `1b60e6836fc407cb4d9e8302313d658ea80f2b8aae8746b8e8a1be3520fcd0d8` | 1142 | 7803 | match; within limit |

The cases hash is `45f0b96edcfed3562ee2d6338db0bc1270d7c8a5a5dcdb8dc48e2f8a764739cd`, the generation-plan hash is `f7ab0bd079a0b9e8316e7fcf7c1cf2eaf958f635087f2e4f08c381acc4c97bd8`, and the generation-attestation hash is `e212fbf86533c238e1f80706193b3107d51c802c63364e0b943ae3e2f48fa5c9`.

## Strict misses

- **scenario-01 criterion 3:** The scenarios and unknown-control fields are complete, but the equilibrium/default-alive test has no date.
- **scenario-02 criterion 2:** Sales capacity lacks a complete unknown-control row; cohort comparability also lacks the full owner/artifact/date/threshold/effect structure.
- **scenario-02 criterion 3:** The 90-day experiment omits an affected lead/customer segment and an explicit rival causal explanation.
- **scenario-02 criterion 4:** Adapt and hold do not state exact spend levels; they use “inside $36k” and “current committed level.”
- **scenario-03 criterion 3:** No staged technical-readiness milestone is defined separately from the clinical/regulatory cost-and-schedule gate.
- **scenario-03 criterion 4:** The hire gate lacks an explicit milestone-capacity predicate, and no partner option is compared.
- **scenario-04 criterion 3:** Channel saturation has no owner, artifact, due date, threshold, or decision effect.

All other criteria satisfy every required clause explicitly. Detailed evidence is in `forward/scorecards/` and the machine-readable record is `forward/strict-score.json`.
