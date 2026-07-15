# Skill 12 RED baseline independent review

## Verdict

- Integrity: **PASS**
- Contract fairness / prompt leakage: **PASS / none found**
- Final score: **14/30**
- Normalized score: **0.466667**
- RED-valid: **YES** — every case misses at least one strict conjunctive criterion.

Stage A was written and hash-frozen before either scorer artifact was opened. Its SHA-256 was `c0c5b3dabb5cd9a018cd451c708b53ae0e9925db8f48f0a53ba41b475502844f`.

## Stage A to final comparison

| Case | Stage A | Scorer | Final | Result |
|---|---:|---:|---:|---|
| Scenario 01 | `10000` | `10000` | `10000` | agree |
| Scenario 02 | `11000` | `11011` | `11011` | Stage A C4/C5 corrected to 1 |
| Scenario 03 | `10000` | `10000` | `10000` | agree |
| Scenario 04 | `10101` | `10101` | `10101` | agree |
| Scenario 05 | `10000` | `10000` | `10000` | agree |
| Scenario 06 | `10111` | `10111` | `10111` | agree |

The independent blind pass agreed on 28 of 30 bits. All 28 agreeing rationales were materially consistent with the scorer, though the scorer sometimes named additional missing conjuncts. The two disagreements were re-adjudicated as follows:

- **Scenario 02 criterion 4, `0 → 1`:** Days 6–15 schedule build/test work, unrelated features are frozen, clinic-user contact repeats across Days 1–5, 6–15, and 16–25, and line 48 explicitly restores a normal workweek with no mandatory nights. Stage A had improperly required a more formal recurring calendar.
- **Scenario 02 criterion 5, `0 → 1`:** functional owners, Days 1–5 baseline work, the 22%-to-50% target, twice-weekly/end-week checkpoints, the Days 26–30 decision, and the continue/adjust/pivot conditions in line 44 satisfy the full conjunct. Stage A had improperly demanded more numeric precision than the criterion requires.

No scorer bit or rationale required correction after those two Stage A undercalls were resolved. The final vectors are therefore `10000`, `11011`, `10000`, `10101`, `10000`, and `10111`.

## Integrity reproduction

| Artifact | SHA-256 |
|---|---|
| Canonical cases | `f77e14ed626c40a49e051aa535feb5dd9dad4597a4761e5118feb1acea63c8c5` |
| Generation plan | `f84f0b565b617ea6e99b873edf7fdba8e171f2d178de0c649209f90ce414a8f9` |
| Generation attestation | `107c8cdf8aa0b3d9a09571fb2a70ec22b5063d939a32ae0382a13d4dbcdc5d96` |
| Manifest | `4d3af3395f316b5303188166821d053340ba0669495ecc4df0edee2b6a96802f` |
| Prompt-only aggregate projection | `5dcc5d515b9453ae4261017e10afd382ac03013cb7a9ab1061014c502d9d9a72` |
| Scorer JSON | `854d42b449fa785b22a9d563bbcf612715288cc7cf4965ff71ab72b8f69d221a` |
| Scorer Markdown | `2f0b8a3a87c7c63bb7dfee1543791c402320f5ce4855dac0eab60935ad256b35` |

The `.superpowers` canonical copy and `evals/.../cases.json` are byte-identical. All six prompt files byte-match their canonical prompt projections, all six response hashes match the manifest, the responses are unique and below 1,200 words, and each response birth epoch equals its modification epoch. The plan, attestation, and manifest consistently record six distinct fresh-context tasks, criteria hidden, no skill, first completion frozen, no quality resampling, no regeneration, and response hashes frozen before a distinct scorer was dispatched. The expected skill package was absent at freeze and scoring.

Historical execution properties such as fresh context and first-completion capture cannot be replayed from files alone; the independent check confirms that the frozen records attest them consistently and contain no contradictory evidence.

## Fairness and leakage

The generation prompts are exact canonical prompt projections and contain no rubric terms, criteria, taxonomy workflow names, skill content, or source evidence. The criteria are answerable from the scenario facts and the requested plan. Scoring does not require literal taxonomy names: semantically correct routing received credit in every criterion 1. Role owners and relative day/week dates also received credit, so the contract does not demand unavailable names or dates.

No integrity, leakage, fairness, or scorer-total defect invalidates the RED result.
