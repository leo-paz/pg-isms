# Strict forward review: raising-and-governing-capital, attempt 2

Scorer: `capital-forward-scorer-001`  
Method: conjunctive binary scoring; a criterion earns 1 only when every clause is explicit in the frozen response.

## Result

- Forward: **20/25 = 0.80 (80%)**
- Frozen baseline: **1/25 = 0.04 (4%)**
- Delta: **+19 criteria, +0.76 normalized**
- Per-case forward scores: **5, 4, 4, 2, 5**
- Per-case deltas: **+5, +4, +4, +2, +4**
- Every case has material behavior improvement: **yes**
- Integrity verdict: **pass**
- `forward_valid`: **true**

## Frozen vector

| Case | Vector | Score |
|---|---:|---:|
| scenario-01 | `[1, 1, 1, 1, 1]` | 5/5 |
| scenario-02 | `[1, 1, 0, 1, 1]` | 4/5 |
| scenario-03 | `[1, 0, 1, 1, 1]` | 4/5 |
| scenario-04 | `[0, 0, 1, 1, 0]` | 2/5 |
| scenario-05 | `[1, 1, 1, 1, 1]` | 5/5 |
| **Total** | `1111111011101110011011111` | **20/25** |

The 25-bit vector was frozen at `2026-07-16T05:47:10Z` in `score-vector-freeze.json` (SHA-256 `0a85f44125451a639a88dea5d5b3bcc1c523932ff288294c5c1bc03a1eef2dd0`). Only afterward, at `2026-07-16T05:47:32Z`, was `baseline/summary.json` opened. No baseline response body, source evidence/provenance, or prior-forward-attempt artifact was opened.

## Integrity proof

- Cases SHA-256: `fc56ebe94279acb5b1091df1fba26e4152f1798f0936e9c58e75d7196d89f372`.
- Generation plan SHA-256: `1a2e2effc4e7f036a7ab19248901a5098dbf4390d9cc7a1a6e4c22932d3d0b08`.
- Package-freeze manifest SHA-256: `a0ae3a83fa406363bf5f60db1d9fca978a43b39071c4a2c8a2396eab475ad586`.
- Generation attestation SHA-256: `f45d01f204f94ca552d67e2860e37c648e255b40beef2705a8a23f3f7e4fd094`.
- Generation-freeze manifest SHA-256: `0716785c8642d19618bdc6b1449387c8cc05d08acd906bacc315ae4c50a0eb1f`.
- All six package hashes recalculated exactly; the package was frozen at `2026-07-16T05:26:10Z`, before every response birth time.
- All five prompt hashes match the plan, and every prompt is an exact id-and-prompt-only projection of `cases.json`.
- The five task IDs are distinct (`capital_forward2_1` through `_5`), the five response hashes are unique, and the attestation records hidden criteria, baseline, prior attempt, and source evidence, one first completion per case, and no quality resampling.
- Every recalculated response SHA-256, byte count, word count, birth time, and modification time matches the attestation/freeze; every response is at most 1,200 words and every birth time equals its modification time.

| Case | SHA-256 | Words | Bytes | Birth = mtime (UTC) |
|---|---|---:|---:|---|
| scenario-01 | `13652bd71a71ecd4a1e7ff32a587b8d3477203ca1f96866546d8bcea09cb57f8` | 1009 | 9501 | `2026-07-16T05:33:58Z` |
| scenario-02 | `7ee6f712471088476985a90a3e8370a9b4928ddd977fd7321e7e1799b7914aa5` | 1045 | 7438 | `2026-07-16T05:31:32Z` |
| scenario-03 | `39e4fa022ab88a0957a6ec053d3bef6be21f1eb242f602970dec1d2cb5ce1453` | 1051 | 7142 | `2026-07-16T05:33:04Z` |
| scenario-04 | `379174bae5b6d91c7362fda0f8524de86e023482be81ee2bd355454539e9b695` | 1077 | 7830 | `2026-07-16T05:41:42Z` |
| scenario-05 | `8da167c6af928de13ece197d82e9eb4c24ca67cca1d79e741d0b65efa60c61b6` | 1050 | 7730 | `2026-07-16T05:41:00Z` |

## Strict misses

- **scenario-02 criterion 3:** no downside/base/upside exit-waterfall comparison of preference economics.
- **scenario-03 criterion 2:** no explicit dated default-alive/equilibrium test; the capital handoff can pass while recurring expense still exceeds recurring collections.
- **scenario-04 criterion 1:** selects `managing-runway-and-survival`, not the required capital workflow, as primary.
- **scenario-04 criterion 2:** omits an explicit working-capital line item/range and a qualified regulatory or safety unknown control.
- **scenario-04 criterion 5:** substitutes survival branches for the required `launch-round`, `stage-or-syndicate`, `delay-and-rework`, and `stop-or-preserve-option` financing branches.

All other criteria explicitly satisfy every clause. Detailed evidence and missing clauses are in `forward/scorecards/`; the machine-readable record is `forward/strict-score.json`.
