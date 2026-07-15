# Frozen paired microtest scorer report

Date: 2026-07-15  
Scorer: `/root/org_micro_scorer`  
Plan: `building-and-evolving-organizations-microtest-001`

## Verdict

**PASS.** Control scored **2/25 = 0.08** and guided scored **15/25 = 0.60**. The normalized guided-minus-control effect is **+0.52**, exceeding the predeclared **`>= 0.20`** gate by **+0.32**.

An independent review corrected guided rep 4 C5 from 1 to 0. Its Keep result gives an action but no explicit next owner; the strict every-result owner/action conjunct does not permit that omission to be inferred from global leadership text.

The scorer applied each criterion as an all-conjunct bit. Omitted owners, limits, dates, caveats, actions, and semantic roles were not inferred.

## Integrity

Integrity reproduced with **no blockers**:

- 10 samples: 5 control and 5 guided.
- 10 unique canonical tasks, sample IDs, response paths, and response SHA-256 hashes.
- Plan and attestation task/arm/path mappings match; indices are exactly 1–10.
- Every response hash, byte count, and word count matches the attestation.
- Every response is below the 1,500-word cap; maximum is 1,450 words.
- Generation-plan hash matches the attestation; rubric, prompt-derived, and criteria-derived metadata match the plan.
- Frozen-before-generation state, hidden-input controls, first-completion freezing, no quality resampling, and no post-generation revision are declared consistently.

The scorer remained blind to `SKILL.md`, `runtime-contract.md`, separate source evidence, and prior evaluations. Their hashes are retained only as declarations from `skill-freeze.json`.

## Vectors and totals

Vector order is C1–C5.

| Sample | Arm | Vector | Score |
|---|---|---|---:|
| `org_micro_control_1` | control | `00000` | 0 |
| `org_micro_control_2` | control | `00000` | 0 |
| `org_micro_control_3` | control | `00000` | 0 |
| `org_micro_control_4` | control | `00010` | 1 |
| `org_micro_control_5` | control | `00010` | 1 |
| `org_micro_guided_1` | guided | `10110` | 3 |
| `org_micro_guided_2` | guided | `01110` | 3 |
| `org_micro_guided_3` | guided | `01110` | 3 |
| `org_micro_guided_4` | guided | `01110` | 3 |
| `org_micro_guided_5` | guided | `01110` | 3 |

| Arm | C1 | C2 | C3 | C4 | C5 | Total | Normalized |
|---|---:|---:|---:|---:|---:|---:|---:|
| Control | 0 | 0 | 0 | 2 | 0 | 2/25 | 0.08 |
| Guided | 1 | 4 | 5 | 5 | 0 | 15/25 | 0.60 |

`(15 - 2) / 25 = 13 / 25 = 0.52`

`0.52 >= 0.20` → **PASS**

## Retained misses

- C1: only guided rep 1 explicitly disposed of broad reorganization. Rejecting broad delegation, headcount, titles, committees, or compensation changes did not explicitly dispose of that separate option.
- C2: every control response omitted the complete observations/claims/unknowns ledger. Guided rep 1 did not explicitly classify proposed-boundary quality and future pilot effects as unknown.
- C3: every control response omitted one accountable end-to-end implementation/go-live outcome owner. All guided responses passed.
- C4: control reps 1–3 omitted a named evidence owner and/or complete checkpointing. Control reps 4–5 and all guided responses passed.
- C5: no response explicitly named the next owner and action for every required result. Guided rep 4 included all result branches and thresholds, but its Keep result omitted the next owner.

## Canonical evidence

- Machine-readable integrity, all 50 bit decisions, totals, effect, gate, and retained misses: `summary.json`.
- Per-sample explicit rationales: `scorecards/org_micro_control_1.md` through `scorecards/org_micro_guided_5.md`.
