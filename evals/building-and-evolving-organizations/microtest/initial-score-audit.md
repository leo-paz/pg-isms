# Frozen paired microtest blind-score audit

Date: 2026-07-15  
Scorer: `/root/org_micro_scorer`  
Microtest: `building-and-evolving-organizations-microtest-001`

## Verdict

**PASS.** Control scored **2/25 = 0.08**. Guided scored **16/25 = 0.64**. The guided-minus-control effect is **+14/25 = +0.56**, which clears the predeclared **`>= 0.20`** gate by **+0.36**.

Each criterion was graded as an independent all-conjunct bit. I gave no partial credit and did not infer omitted owners, limits, dates, caveats, actions, or semantic roles.

## Blind-read boundary

I opened only the four authorized manifest files and the ten response paths listed in the attestation. I did not open `SKILL.md`, `runtime-contract.md`, `prompt.txt` as a separate file, source evidence, prior evaluations, prior agent messages, or other repository files. Prompt and criteria metadata were independently derived from `rubric.json`. The frozen skill/runtime hashes below are reproduced from `skill-freeze.json`; their targets were deliberately not opened.

## Integrity reproduction

Integrity status: **PASS; no blockers.**

- Actual samples: 10; control: 5; guided: 5.
- Unique canonical tasks: 10; sample IDs: 10; paths: 10; actual response hashes: 10.
- Indices are exactly 1–10 and plan/attestation task-arm-path mappings match.
- Every actual response hash, byte count, and `wc -w` count matches its attestation entry.
- All ten responses are below the 1,500-word cap; maximum is 1,450 words.
- Generation-plan hash matches the attestation; rubric hash/bytes match the plan.
- Criteria hash/bytes/count and prompt hash/bytes/words reproduce exactly from `rubric.json`.
- Plan state is `frozen-before-response-generation`; `response_generation_started` is false.
- The plan declares fresh context, criteria/prior/opposite-arm hiding, first-completion freezing, no quality resampling, manual semantic grading, and a 0.20 gate.
- The attestation declares no post-generation revision and repeats the passing count/uniqueness/word-cap invariants.
- The skill-freeze path matches the plan. The design-review verdict/hash are reproduced as declarations only; the separate review artifact was outside the allowed read set.

### Frozen and manifest metadata

| Role | SHA-256 | Bytes | Extra / verification |
|---|---|---:|---|
| `rubric.json` | `637702d2cc20c2c1a20cd1c190b9a1f7fac43e020732e6682873a7f43fd6aa75` | 4,824 | recomputed |
| `generation-plan.json` | `7eb719689e1cc8e48bc016ac9f8d44e1b7b9ac2bd4f18faae0ea9fca0aac2aa8` | 4,450 | recomputed; matches attestation |
| `generation-attestation.json` | `7ccc01f23977e98d25ea418c733e85d34da0e884d7d0a796b17a744449444370` | 3,711 | recomputed |
| `skill-freeze.json` | `3279de5df5e64258374bf513e6eab62ff9931ffd8a2482d661b89aa2bc28149e` | 583 | recomputed |
| Prompt | `375c5d6d4c905177150b206e7c65fb960cde374c99cb22f7ac4abd49662fa4be` | 2,317 | 365 words; reproduced from rubric prompt + LF |
| Criteria | `5a12e2133053c6b53f2d0bd1a3771ddaf2b21e8d1f24ed886647154634d4ce19` | 2,356 | 5 criteria; `jq -c .criteria` + LF |
| Frozen skill | `2a1e0a27562aa3cfac61ce280a833bd538e4ad633267e238d8cf7bed695e572a` | 3,718 | declared by freeze; target not opened |
| Frozen runtime contract | `6fc8f66eb3b3aea79b1bab9b67602887e0bbb17a00e302e6982fb48378e7bd5b` | 12,033 | declared by freeze; target not opened |

### Task, arm, path, and response metadata

| # | Canonical task / sample ID | Arm | Response path | SHA-256 | Bytes | Words |
|---:|---|---|---|---|---:|---:|
| 1 | `/root/org_micro_control_1` / `org_micro_control_1` | control | `evals/building-and-evolving-organizations/microtest/control/rep-1.md` | `70c2466612b88e545868f62d1777409acf758080bc01e9e843b004f056f1287e` | 7,174 | 1,042 |
| 2 | `/root/org_micro_control_2` / `org_micro_control_2` | control | `evals/building-and-evolving-organizations/microtest/control/rep-2.md` | `8d04d6b64af9b71cdc2b7867981dbf500c3a7f43e955de668293ea6f9d765249` | 8,213 | 1,197 |
| 3 | `/root/org_micro_control_3` / `org_micro_control_3` | control | `evals/building-and-evolving-organizations/microtest/control/rep-3.md` | `73a1c60241c70c25daa78d9b8e82061b81af41747658f0378222b458e406bbd7` | 6,994 | 1,014 |
| 4 | `/root/org_micro_control_4` / `org_micro_control_4` | control | `evals/building-and-evolving-organizations/microtest/control/rep-4.md` | `cbe8ca7cd186fb66df4011f483b64ee576a1b1e22e616f0d57f4f558119e1d3b` | 7,579 | 1,120 |
| 5 | `/root/org_micro_control_5` / `org_micro_control_5` | control | `evals/building-and-evolving-organizations/microtest/control/rep-5.md` | `7d49f0a678c97d26cd439689ca7fd59c79669319d83a466d48b7c60e4c11f9a0` | 7,123 | 1,066 |
| 6 | `/root/org_micro_guided_1` / `org_micro_guided_1` | guided | `evals/building-and-evolving-organizations/microtest/guided/rep-1.md` | `d2b94ae8c97f631e43af06a29dbd5459342191914a67d80a98e9f7fae8dcc542` | 9,322 | 1,370 |
| 7 | `/root/org_micro_guided_2` / `org_micro_guided_2` | guided | `evals/building-and-evolving-organizations/microtest/guided/rep-2.md` | `fd23f66dca751d0abc6bc6b00047955e7a2ba8c135cf33279b7d89898813c9ca` | 9,692 | 1,393 |
| 8 | `/root/org_micro_guided_3` / `org_micro_guided_3` | guided | `evals/building-and-evolving-organizations/microtest/guided/rep-3.md` | `10fe768e24b1a98c9f3690df9c34f3c3882ec77414b1182ab8c0bca7a0fd1618` | 9,405 | 1,388 |
| 9 | `/root/org_micro_guided_4` / `org_micro_guided_4` | guided | `evals/building-and-evolving-organizations/microtest/guided/rep-4.md` | `55f6a5234d16aed297192a7191b555bcc63192e2f6443483f5f4a12ccfeaef9e` | 9,952 | 1,450 |
| 10 | `/root/org_micro_guided_5` / `org_micro_guided_5` | guided | `evals/building-and-evolving-organizations/microtest/guided/rep-5.md` | `281d168cd6ce1eb65acdd07f26bcb2aa9b945e6c97d3c9085ce094174888d536` | 9,939 | 1,422 |

## Score matrix

Vector order is C1–C5.

| Sample | Arm | Vector | Bits passed |
|---|---|---|---:|
| `org_micro_control_1` | control | `00000` | 0 |
| `org_micro_control_2` | control | `00000` | 0 |
| `org_micro_control_3` | control | `00000` | 0 |
| `org_micro_control_4` | control | `00010` | 1 |
| `org_micro_control_5` | control | `00010` | 1 |
| `org_micro_guided_1` | guided | `10110` | 3 |
| `org_micro_guided_2` | guided | `01110` | 3 |
| `org_micro_guided_3` | guided | `01110` | 3 |
| `org_micro_guided_4` | guided | `01111` | 4 |
| `org_micro_guided_5` | guided | `01110` | 3 |

## Per-bit rationale

### `org_micro_control_1` — `00000`

- **C1 0:** Correctly makes latency/ambiguity primary and rejects the COO and council, but rejects broad/informal delegation rather than broad reorganization.
- **C2 0:** No explicit observation/claim/unknown separation; boundary quality and future effects are not explicitly unknown.
- **C3 0:** Head is a routine decision owner, not an end-to-end go-live outcome owner; absence backup and a named continuity owner are missing.
- **C4 0:** The six-week test has scope, measures, and safeguards, but no named evidence owner and no explicit dated intermediate checkpoint.
- **C5 0:** No required add-capacity result and no next owner/action for every result.

### `org_micro_control_2` — `00000`

- **C1 0:** Correct primary problem/intervention and COO/council rejection, but no explicit disposition of broad reorganization.
- **C2 0:** Evidence and caveats are discussed without classifying all required observations, claims, and unknown types.
- **C3 0:** Head owns routine exceptions, not an explicitly end-to-end implementation/go-live outcome.
- **C4 0:** The reversible measured trial lacks a named evidence owner.
- **C5 0:** Only three qualitative outcomes appear; the four measured branches and branch owners/actions are absent.

### `org_micro_control_3` — `00000`

- **C1 0:** Correct decision-rights choice and COO/council rejection; broad reorganization is not explicitly rejected/deferred.
- **C2 0:** No explicit ledger or complete classification of stakeholder claims and required unknowns.
- **C3 0:** Decision/communication responsibilities exist, but no single end-to-end go-live outcome owner.
- **C4 0:** No role explicitly owns the pilot evidence record/dashboard.
- **C5 0:** Missing the complete four branches, one-variable-once revision, full-cost capacity gate, and branch owners.

### `org_micro_control_4` — `00010`

- **C1 0:** It rejects undifferentiated broad delegation, not broad reorganization.
- **C2 0:** Caveats do not substitute for an explicit observation/claim/unknown ledger or claim classification.
- **C3 0:** The Head owns decisions/record, not the end-to-end go-live outcome; no actual absence backup is named.
- **C4 1:** Reversible May 4–June 12 test; CEO/Head change ownership; Head record ownership; derivable intermediate reviews; scope, baseline, register, outcome/harm measures, continuity, promise, specialist-review, suspension, and traceability safeguards.
- **C5 0:** No add-capacity result and no branch-specific owner/action assignments.

### `org_micro_control_5` — `00010`

- **C1 0:** It rejects broad delegation rather than broad reorganization.
- **C2 0:** No explicit evidence taxonomy or complete required classifications.
- **C3 0:** Head is accountable decision maker, but no role explicitly owns the end-to-end go-live outcome.
- **C4 1:** Reversible May 5–June 15 test; named change owners and Implementation evidence owner; derivable checkpoints; baseline/artifacts/measures; continuity, promise, specialist-review, narrowing, and record safeguards.
- **C5 0:** Revision is not exactly one change once; capacity lacks benefit-above-full-cost; branch owners/actions are incomplete.

### `org_micro_guided_1` — `10110`

- **C1 1:** Explicit queue/interface problem, bounded decision rights, COO/council deferral/rejection, flat organization, and domain restoration instead of broad reorganization, based on no demonstrated capacity need.
- **C2 0:** The ledger and causal rival are explicit, but the proposed boundary's quality and future pilot effects are not explicitly categorized as unknown; generic request-mix caveats do not fill those semantic roles.
- **C3 1:** End-to-end Head ownership, domains/limits, specialist consultation, notice, clocks/destinations, interface service, backup, register, continuity, and protected review are all explicit.
- **C4 1:** Reversible dated pilot with change/evidence owners, May 18 and June 1 checkpoints, scope, baseline/artifacts/measures, and all required safeguards.
- **C5 0:** Capacity relief/value is not required to exceed full role cost.

### `org_micro_guided_2` — `01110`

- **C1 0:** It rejects the COO, council, and another layer, but broad reorganization is not explicitly disposed of as a separate option.
- **C2 1:** Complete evidence taxonomy, required classifications, live sustainability/boundary/future/causal uncertainty, and multiple rivals.
- **C3 1:** Complete outcome ownership and operating contract, including service clocks, backups, audit artifact, continuity, and qualified review.
- **C4 1:** Complete reversible, dated, owned, measured, safeguarded pilot.
- **C5 0:** It says to name a revision owner later rather than naming one; not every result names its next owner/action.

### `org_micro_guided_3` — `01110`

- **C1 0:** Correct primary mechanism/intervention and COO/council disposition, but no explicit broad-reorganization disposition.
- **C2 1:** Complete ledger, required classifications and uncertainty, and a stated capacity/judgment rival.
- **C3 1:** Complete outcome owner, boundaries, reviews, notice/clocks, interfaces, backups, log, continuity, and specialist protections.
- **C4 1:** Complete reversible dated pilot with owners, checkpoints, baseline/artifacts/measures, pause, and evidence retention.
- **C5 0:** Capacity benefit need not exceed full role cost, and the revise owner is deferred rather than named.

### `org_micro_guided_4` — `01111`

- **C1 0:** It forbids headcount/title/committee/compensation changes but does not explicitly reject/defer broad reorganization; those listed prohibitions do not exclude a broad reporting-line or responsibility reorganization.
- **C2 1:** Complete evidence taxonomy, required source treatment and unknown types, plus a capacity/complexity rival.
- **C3 1:** Complete end-to-end Head ownership, boundaries, consultation, notice, escalation/service clocks, backups, register, continuity, and protected review.
- **C4 1:** Complete May 5–June 15/16 reversible pilot with evidence ownership, May 25 checkpoint, baseline, measures, and every safeguard.
- **C5 1:** Current decision/unknowns/prior option plus measured Keep, one-variable/one-time Revise, full-cost-gated Add-capacity, and harm Rollback branches; header and branch text supply next owners/actions.

### `org_micro_guided_5` — `01110`

- **C1 0:** Correct primary problem/intervention and COO/council rejection, but no explicit broad-reorganization disposition.
- **C2 1:** Complete evidence taxonomy, required source treatment and unknowns, and hidden complexity/rework rival.
- **C3 1:** Complete end-to-end owner and operating design.
- **C4 1:** Complete reversible, owned, dated, measured, safeguarded pilot.
- **C5 0:** The capacity branch does not explicitly require interface causes to be addressed, and Keep/Revise/Capacity do not each name their next owner.

## Totals and gate

| Arm | Passed bits | Possible | Normalized |
|---|---:|---:|---:|
| Control | 2 | 25 | 0.08 |
| Guided | 16 | 25 | 0.64 |

`guided - control = (16 - 2) / 25 = 14 / 25 = 0.56`

`0.56 >= 0.20` → **PASS**

## Main findings

- Control earned only C4 in reps 4 and 5. Its dominant omissions were the explicit evidence taxonomy, one end-to-end outcome owner, and the complete four-result closure.
- All five guided samples passed C3 and C4.
- Only guided rep 1 explicitly disposed of broad reorganization; the others rejected narrower structural changes without naming that semantic role.
- Only guided rep 4 completed the strict closure, including the full-cost capacity gate and owner/action coverage.
- The effect is +0.56, exceeding the gate by +0.36.

The machine-readable audit, including every per-bit rationale and all integrity metadata, is in `org-micro-score.json`.
