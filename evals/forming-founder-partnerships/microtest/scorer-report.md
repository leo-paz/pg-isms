# Canonical scorer report — founder-partnerships microtest attempt 017

## Verdict

`PASS`

Integrity is `PASS`, the ten response vectors are reproducible, and the corrected guided-minus-control effect is `0.36`, which meets the `>= 0.20` threshold.

## Revision note

The attempt-017 Stage-B challenge identified one overly lenient bit. In `founder_micro_guided_4_017`, the pre-check statement that "Respect and candor appear intact enough to run the reset" infers honesty/truthfulness while the June 27 sources are still unreviewed. That violates C2's explicit no-inference conjunct; the later disclaimer against a broader character conclusion does not retract the narrower candor inference. Guided sample 4 C2 is corrected from `1` to `0`; integrity and the overall `PASS` verdict are unchanged.

## Integrity audit

The audit independently reproduced the frozen rubric, decoded prompt, canonical criteria, skill, runtime contract, shared harness, control assembly, guided assembly, harness/driver/failure/envelope probes, generation plan, skill freeze, and guided-retry hashes and byte counts. The control context is `3623` bytes with SHA-256 `29c3476f4f19d99e19ad5d1c9aa2fefe7a8fcc962c137c0dd8119f6d88a3b500`; the guided context is `18443` bytes with SHA-256 `a87ebb086526d063fab2b46e52c495d2d8602d5d219288f627a11a8a4561edc5`. Both end at the canonical prompt's final period with no terminal LF.

For every response, the eight headers are present in the exact required order; the body begins after one empty separator line; exactly the declared UTF-8 byte length reproduces the declared body SHA-256; and the only remainder is one envelope LF. Each response file hash/size and trace hash/size matches the generation attestation.

All ten canonical-task, sample, context, thread, and response-body identities are unique. Dispatches follow planned order, every completion is no earlier than its dispatch, and every subsequent accepted dispatch follows the prior completion. The five control contexts and five guided contexts match their arm identities exactly.

Each trace has one fresh thread, one completed final `agent_message`, zero forbidden events, exit code 0, and trace gate `PASS`. Event records are limited to `thread.started`, `turn.started`, `item.completed(agent_message)`, and `turn.completed`. Diagnostic records retain ordered hashes, byte counts, and process-only classes; they do not constitute task activity. Nine traces have 21 diagnostics and guided sample 2 has 22; the only classes are state-db fallback warnings plus the recorded shell-snapshot or other process diagnostic where present.

The guided assembly preflight failed at `2026-07-15T17:59:02.430Z` before Codex received a prompt. Its artifact records zero threads, zero JSON events, zero final messages, and no response. The corrected accepted guided dispatch began at `2026-07-15T18:00:07.969Z`; it is not a response resample.

The five criteria are isolated. C1 scores only current route/mode and branch exclusions; C2 only the non-commitment evidence ledger and narrow trust check; C3 only the supplied commitment map, current existing-team outcome, and work-trial decision; C4 only proposed current operating terms and coverage; and C5 only future replacement predicates and breach handling. Their explicit non-scoring clauses prevent any omitted field from being recovered through another criterion.

## Scores

| Arm | Sample | Vector `[C1,C2,C3,C4,C5]` | Score |
|---|---|---:|---:|
| control | founder_micro_control_1_017 | `[1,0,0,0,0]` | 0.2 |
| control | founder_micro_control_2_017 | `[1,0,0,0,0]` | 0.2 |
| control | founder_micro_control_3_017 | `[1,0,0,0,0]` | 0.2 |
| control | founder_micro_control_4_017 | `[1,0,0,0,0]` | 0.2 |
| control | founder_micro_control_5_017 | `[1,0,0,0,0]` | 0.2 |
| guided | founder_micro_guided_1_017 | `[1,1,1,0,0]` | 0.6 |
| guided | founder_micro_guided_2_017 | `[1,1,1,0,0]` | 0.6 |
| guided | founder_micro_guided_3_017 | `[1,1,1,0,0]` | 0.6 |
| guided | founder_micro_guided_4_017 | `[1,0,1,0,0]` | 0.4 |
| guided | founder_micro_guided_5_017 | `[1,1,1,0,0]` | 0.6 |

Control normalized vector: `[0.2,0.2,0.2,0.2,0.2]`; mean `0.2`; population variance `0`.

Guided normalized vector: `[0.6,0.6,0.6,0.4,0.6]`; mean `0.56`; population variance `0.0064`.

Effect: `0.56 - 0.2 = 0.36`. Threshold decision: `0.36 >= 0.20`, therefore `PASS`.

Response-specific rationale for every zero appears in the ten canonical scorecards and is repeated structurally in `summary.json`.
