# Final evaluation-integrity review

- Reviewer ID: `skill12-eval-integrity-final`
- Status: complete
- Reviewed at: `2026-07-16T03:10:14Z`
- Ready to commit: **No**

## Critical

### Canonical paired microtest is not valid confirmatory evidence

The prompt imposes a hard 1,200-word cap (`microtest/prompt.txt:13`), but four guided outputs are 1,499–1,792 words while all five controls conform (`microtest/generation-attestation.json:6-15`). The summary nevertheless marks the test accepted at a `+0.48` guided-minus-control delta (`microtest/summary.json:17-22`). This creates an arm-specific length confound and conflicts with the repository's treatment of the same cap in earlier microtest, forward, and held-out attempts, which were rejected unscored when responses exceeded it (`microtest/attempt-001/archive-status.json:8`, `forward/attempt-005/archive-status.json:7-16`, `heldout/attempt-004/archive-status.json:7-9`). The canonical microtest must not support acceptance until remediated with a conforming predeclared run.

## Important

### Predeclared blind-scoring protocol was not executed

The design requires two fresh independent blind scorers and blind adjudication before revealing the arm key (`microtest/attempt-005-design.json:113-118`). Only one blind scorer is recorded. The later independent auditor explicitly read `microtest/blind-mapping.json` (`microtest/independent-review.json:20-23`), which reveals every guided and control slot (`microtest/blind-mapping.json:5-16`). Its zero-bit-change result is not the second blind score promised by the frozen protocol.

### Current held-out attempt did not pass

Held-out attempt 005 requires 5/5 (`heldout/attempt-005-design.json:16-22`) but scored 4/5 with `accepted: false` (`heldout/score.json:44-56`; `heldout/summary.json:7-12`). `research/progress.md:1138-1143` accurately discloses the miss, but the milestone heading and `12/21` advancement with no blockers (`research/progress.md:1115`, `research/progress.md:1147-1148`) overstate acceptance while this frozen gate remains failed.

### Held-out execution integrity is not reconstructable

The design requires a fresh criteria-hidden generator, one same-agent length-only draft, canonical freeze, and grading only after freeze (`heldout/attempt-005-design.json:54-81`). The current held-out root contains no generation plan, generation attestation, or response-freeze manifest. Prompt and response hashes reproduce, but freshness, generator/scorer separation, freeze chronology, and the no-repair/no-resampling claim remain assertions rather than independently reconstructable facts.

## Minor

- `forward/manifest.json:35-38` declares a prefix wrapper, but the `Case ID` and `Reviewer ID` metadata are appended to the canonical responses, for example at `forward/scenario-01.md:125-126`. Full-file hashes match; this is metadata drift rather than a scoring-body mutation.
- Baseline independent artifacts label `4d3af3395f316b5303188166821d053340ba0669495ecc4df0edee2b6a96802f` as `manifest_sha256` (`baseline/independent-review.json:20`), but that is the hash of `baseline/generation-freeze-manifest.json`. The current `baseline/manifest.json` hashes to `705ddc687e75e826358f603433308c6b129bb8d2e7e3094cfa55828ca0c157b4`.

## Recomputed evidence

- Current skill SHA-256: `8cb42d33741e49adfb6412bcedb88106491f0041324486115aa4ffdf362245cc`.
- Current runtime SHA-256: `24ec2d982c69da54dc1c6474032e898ee4da22e3f10a8b0bd2a7c4dadeeb2336`.
- Combined skill/runtime SHA-256: `1b2be7ce738d64d623e026c4ced88bd7f415b0d3296196590a7d7a5145b16678`.
- Cases SHA-256: `f77e14ed626c40a49e051aa535feb5dd9dad4597a4761e5118feb1acea63c8c5`.
- Prompt projection SHA-256: `5dcc5d515b9453ae4261017e10afd382ac03013cb7a9ab1061014c502d9d9a72`.
- RED baseline arithmetic reproduces at `14/30 = 0.466667`; every case retains at least one miss.
- Final forward arithmetic reproduces at `23/30 = 0.766667`; delta from baseline is `9/30 = 0.30`, exceeding the declared `0.10` gate. Current response whole-file hashes match the manifest and package hashes are current.
- Microtest score arithmetic reproduces at control `0/25`, guided `12/25`, delta `0.48`; the acceptance interpretation is invalidated by the cap and protocol findings above.
- Held-out prompt and response hashes reproduce; strict score arithmetic is `4/5`, not accepted.
- All JSON artifacts under this evaluation parse successfully.
- Official skill validation passed and `python3 -m unittest discover -s tests -p 'test_*.py'` passed all 120 tests. These mechanical checks do not cover the integrity defects above.

## Disposition

`ready_to_commit: false` pending a conforming canonical paired microtest that follows its frozen scoring protocol, resolution or explicit non-gating treatment of the failed held-out attempt, and execution attestations sufficient to reconstruct held-out freshness, independence, freeze chronology, and no-repair/no-resampling claims.
