# Held-out attempt 003 strict score

## Verdict

- Vector: **C1-C5 = `[1, 1, 1, 1, 1]`**
- Score: **5/5**
- Threshold: **PASS** (requires at least 4/5)
- Transfer: **PASS**
- Integrity: **PASS within the authorized five-file scope**

## Scope and integrity

Only `skill-freeze.json`, `case.json`, `generation-plan.json`, `prompt.txt`, and `response.md` under `evals/building-and-evolving-organizations/heldout/` were inspected. Attempts 001/002, skill/runtime contents, baseline/forward/microtest artifacts, sources/provenance, other skills, author/prompt-review artifacts, existing scores/reviews, git history/diff, and intended answers were not inspected.

| File | SHA-256 | Bytes |
|---|---|---:|
| `skill-freeze.json` | `fe54d93f10fb312605bf9941d1eae332644627cfd20de9add6d6a21d9cd3855f` | 747 |
| `case.json` | `ed27fedc01c45cd216da18e51acc93e605ec6e6bae09fdf0f11be224aebc288d` | 6,213 |
| `generation-plan.json` | `0059317f524b04b0a3eca8b7c3c4b292ae63c5d1ce27a8cfb7a7c12b52a5c04c` | 3,932 |
| `prompt.txt` | `f4c6639c8e83c19eed3bc80fbeca02a474eb48bf4173c05242ec0f39ab62dfaa` | 2,588 |
| `response.md` | `3d00c301836f75e3c0602597778e6f0d77b3cd350fa2a71a82dee9f135c734a3` | 16,979 |

The case prompt is 2,587 bytes, 406 words, and hashes to `fe641bbb3e2fbc1febd8c8f6272fbb86991a08e5dfd2666b74311ec27712dab6`. `prompt.txt` is byte-identical to that prompt plus exactly one final LF. Compact `tojson` serialization of the accessible hidden criteria is 2,655 bytes and hashes to `35ae3f9e0667353edb9b0aff63493be64c6746b81dc8714200dce46e2ccd451b`, matching the plan. Freeze, case, and prompt-projection hashes/bytes match their accessible manifest claims. Skill/runtime hash-and-byte declarations agree across the three authorized JSON files, but their contents and the derived context hash were not recomputed because the scope forbade inspection. The same applies to the case-source and prompt-review artifacts.

The response's first two header lines match exactly, it is a filled dated record, no line has trailing spaces or tabs, and it ends in exactly one LF. The whole-file response hash above was computed after the response existed.

Chronology is ordered: skill freeze `21:09:16Z`; case authorship `21:10:16Z` (+60s); plan freeze `21:16:47Z` (+391s); response birth/mtime `21:25:00Z` (+493s). Thus freeze-before-response passes.

## Strict criteria

| Criterion | Bit | Required conjunct evidence | Missing subchecks |
|---|---:|---|---|
| C1 | 1 | Response lines 6, 10, and 47-54 select `process-or-control` and explicitly reject Head of QA, executive sign-off, a new layer, and headcount as unsupported. | None |
| C2 | 1 | Lines 27-39 separate dated observed facts, both named claims, and future unknowns; lines 34, 37-39, and 68-72 provide owners, methods/artifacts, dates, thresholds, and decision effects for decision-relevant unknowns. | None |
| C3 | 1 | Lines 10, 12, 14, and 58-64 define unit/range validation plus a risk-triggered check, prevented harm, Ravi's control ownership, a 15-minute urgent target, immediate escalation/containment, an auditable record, August 14 review, and Elena's intact end-to-end ownership. | None |
| C4 | 1 | Lines 68-72 specify the reversible four-site July 20-August 14 test, July 22 replay, owners, baselines, and numeric/observable gates. Lines 74-79 contain exactly four final branches: keep, revise one boundary with a final date, expand to the next four sites, and rollback/stop. Lines 78 and 81 exclude hiring as success and defer it to a sustained residual gap after process revision. | None |
| C5 | 1 | Lines 10, 21-23, 62, 70, 76-79, and 85 preserve 24/7 coverage and the 18-site path, retain all listed safeguards and rollback, reject premature broad rollout or safeguard removal, and close each result with owners, the prior path, and observable revisit switches. | None |

## Transfer verdict

**PASS.** The frozen behavior contract preceded a genuinely new case and response under the verified chronology, and the response satisfies all five strict held-out criteria without using any out-of-scope evidence.
