# Attempt 003 independent held-out review

Reviewed at: `2026-07-15T21:33:47Z`

Reviewer: `/root/org_heldout3_independent_review`

Final verdict: **PASS**

## Two-stage integrity

Stage A was locked before any score, prompt-review artifact, or prior-attempt review was opened. The lock is `.superpowers/sdd/org-heldout3-independent-stage-a.json`, 7,084 bytes, SHA-256 `df73e58bae3f6af69ced58593c1ca15c479e5b261bb8a1e227164e6859754e4f`.

Its independent conclusions were:

- C1-C5 vector: `[1, 1, 1, 1, 1]`
- Integrity: PASS
- Prompt naturalness/no leakage: PASS
- Transfer: PASS

Stage B found no substantive disagreement with `score.json`, `scorecard.md`, or the prompt-gate artifact.

## Exact comparison

| Surface | Stage A | Stage B | Agreement |
|---|---|---|---|
| Strict vector | `[1,1,1,1,1]` | `[1,1,1,1,1]` | Exact |
| Positive bits / threshold | `5 / 4` | `5 / 4` | Exact |
| Integrity | PASS | PASS | Exact |
| Naturalness/no leakage | PASS | PASS | Exact |
| Transfer | PASS | PASS | Exact |
| Response contract | PASS | PASS | Exact |
| Chronology | PASS | PASS | Exact |

The rationale wording is independently composed rather than text-identical, but every bit and every required conjunct agrees:

- C1: `process-or-control` is primary; Head of QA, universal executive sign-off, a new layer/title, and headcount are rejected now.
- C2: dated facts remain observed, Ravi/CEO theories remain claimed, future control and latency effects remain unknown, and decision-relevant unknowns have owner/method/date/threshold/effect contracts.
- C3: the minimum control is unit/range validation plus risk-triggered independent checking, with Ravi's control ownership, a 15-minute urgent target, immediate exception/escalation, an auditable release record, August 14 review, and Elena's end-to-end ownership intact.
- C4: the four-site July 20-August 14 pilot uses the July 22 replay, named owners and baselines, and exactly four thresholded outcomes: keep, one-boundary revise with an August 28 final review, expand to the next four sites, or rollback/stop. Capacity is not a success branch.
- C5: 24/7 continuity, all listed high-harm safeguards, the 18-site current path, isolation, evidence, and rollback remain; broad rollout waits for evidence; every result has owners, a preserved path, and observable switches.

## Hashes and context

All five whole-file hashes and byte counts shared with the scorer match exactly:

| File | Bytes | SHA-256 |
|---|---:|---|
| `skill-freeze.json` | 747 | `fe54d93f10fb312605bf9941d1eae332644627cfd20de9add6d6a21d9cd3855f` |
| `case.json` | 6,213 | `ed27fedc01c45cd216da18e51acc93e605ec6e6bae09fdf0f11be224aebc288d` |
| `generation-plan.json` | 3,932 | `0059317f524b04b0a3eca8b7c3c4b292ae63c5d1ce27a8cfb7a7c12b52a5c04c` |
| `prompt.txt` | 2,588 | `f4c6639c8e83c19eed3bc80fbeca02a474eb48bf4173c05242ec0f39ab62dfaa` |
| `response.md` | 16,979 | `3d00c301836f75e3c0602597778e6f0d77b3cd350fa2a71a82dee9f135c734a3` |

Scoped recomputation also agrees exactly: case prompt 2,587 bytes / `fe641bbb3e2fbc1febd8c8f6272fbb86991a08e5dfd2666b74311ec27712dab6`; compact criteria JSON 2,655 bytes / `35ae3f9e0667353edb9b0aff63493be64c6746b81dc8714200dce46e2ccd451b`.

Stage A's broader authorized scope additionally verified the skill at 3,718 bytes / `2a1e0a27562aa3cfac61ce280a833bd538e4ad633267e238d8cf7bed695e572a`, runtime contract at 12,033 bytes / `6fc8f66eb3b3aea79b1bab9b67602887e0bbb17a00e302e6982fb48378e7bd5b`, and exact assembled context at 18,386 bytes / `6013d7961ed5cd6a0d26654850588d806fa46e6dfa91681c577d703c94de4379`. These match the generation plan. The prompt-review artifact itself hashes to `3173e3963dc26e16722584ddf56a1b1db2978b0ee3662f0b5658e7e9169ac774`, also exactly matching the plan.

The scorer's narrower five-file integrity scope is not a disagreement; it deliberately did not recompute skill/runtime/context. The prompt reviewer used the draft case path, whose hash is byte-identical to the canonical case.

## Chronology and role separation

Chronology is ordered and agrees exactly: skill/runtime mtime `19:47:32Z`; behavior freeze `21:09:16Z`; case authorship `21:10:16Z`; prompt review `21:13:53Z`; plan freeze `21:16:47Z`; response `21:25:00Z`. Freeze-to-case is 60 seconds, case-to-plan 391 seconds, and plan-to-response 493 seconds.

Attempt 003's five roles are pairwise distinct:

- Author: `/root/org_heldout3_author`
- Prompt reviewer: `/root/org_heldout3_prompt_gate`
- Generator: `/root/org_heldout3_generator`
- Scorer: `/root/org_heldout3_scorer`
- Independent reviewer: `/root/org_heldout3_independent_review`

The prompt gate is PASS with no blockers, and its artifact hash, review time, naturalness/no-leakage result, 4-of-5 threshold, and freeze/case separation all agree with the generation plan and Stage A.

## Prior failures and attempt distinctness

Attempt 001 remains an integrity-clean preserved failure at `[0,0,1,1,1]`, 3/5 below 4/5. Its C1 survival-routing and C2 survival/forecast-unknown misses remain explicit; its recorded response hash remains `9c30c0cc1ccb4d8fc4783381f668aea0244a7d0b4640d451fa52e398d44a2020`.

Attempt 002 remains an integrity-clean preserved failure at `[1,0,0,0,0]`, 1/5 below 4/5. Its role-fit timing, recruiting allocation, recruiting-latency, and bias/proxy safeguard misses remain explicit; its recorded response hash remains `56876ecb2325a221b76d228fe2573caded5e5a4a72e27e915eabc61a86146885`.

Within the authorized Stage B scope, those canonical summaries and reviews attest immutability and integrity; raw prior responses were intentionally not reopened. The summaries/reviews were themselves hashed in the JSON companion to fix their current state.

Attempt 003 is genuinely distinct: new case ID, entirely new author/reviewer/generator/scorer identities, a process-control scenario rather than the prior survival/decision-rights or leader-role-evolution scenarios, and a response hash different from both prior attempts. It does not reinterpret or repair either frozen failure.

## Final gate

- Integrity: **PASS**
- Naturalness/no leakage: **PASS**
- Strict criteria: **PASS, 5/5** (minimum 4/5)
- Transfer: **PASS**
- Role separation: **PASS**
- Prior-failure preservation: **PASS**
- Attempt 003 distinctness: **PASS**

Disagreements or findings: **none**.
