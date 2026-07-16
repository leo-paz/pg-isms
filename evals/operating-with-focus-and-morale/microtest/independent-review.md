# Independent review — microtest attempt 005

- Reviewer: `focus-micro5-independent-auditor`
- Audited: `2026-07-15T19:52:03-07:00`
- Policy: strict binary conjunctive scoring; no inference or partial credit
- Read scope: only the prompt, rubric, ten blind slots, blind score/review/mapping, and skill freeze named in the audit assignment
- Excluded: skill source, original control/guided files, prior attempts, forward tests, heldout tests, and all other files

## Result

No bit changes were found. The independent vectors reproduce the locked `12/50` total.

After unblinding through the supplied mapping:

| Arm | Slots | Passed bits | Possible bits | Normalized mean | Mean raw total/response |
|---|---|---:|---:|---:|---:|
| Guided | 01, 04, 08, 09, 10 | 12 | 25 | 0.48 | 2.4/5 |
| Control | 02, 03, 05, 06, 07 | 0 | 25 | 0.00 | 0.0/5 |

Audited guided-minus-control delta: **0.48**. Acceptance threshold: `>= 0.20`. Decision: **ACCEPT**.

## Integrity checks

- Fresh SHA-256 values for the prompt, rubric, and ten blind slots match `blind-score.json` and the hash table in `blind-review.md` exactly.
- Slot-level hashes, duplicated vectors, per-slot totals, and the `12/50` aggregate in `blind-score.json` are internally consistent.
- `blind-review.md` reproduces the locked vectors and totals in `blind-score.json`.
- `blind-mapping.json` declares `frozen_before_scoring: true`; `blind-score.json` records `locked_before_unblinding` and `unblinded: false`.
- The mapping is a complete bijection over all ten slots: five guided and five control, with reps 1–5 appearing exactly once in each arm.
- `skill-freeze.json` skill and runtime hashes exactly match the corresponding file-hash fields in `rubric.json`.
- The rubric's combined skill hash was not recomputed because the two skill-source files were explicitly outside this audit's permitted read scope.

Artifact hashes recorded by this audit:

| Artifact | SHA-256 |
|---|---|
| `prompt.txt` | `77d6384adc126690827efe4c5c8771e318ba88ee7c31a205a449e5e88d704638` |
| `rubric.json` | `678993e0559d0f40e18a51ec8a0559514085c8439b99c2f75573f739b4acb961` |
| `slot-01.md` | `d8f36db46ba0a3f85830fec8185562e8186b9bb4b56a5177f1f9f50b0885b154` |
| `slot-02.md` | `05f556fca64d1a45141f111b08dedc207835fb610f35595e620d203563bfd523` |
| `slot-03.md` | `b65f47fd83e35918c7d51708fa6a4d16806ee05b5c28f7003e6e9963404f3fe9` |
| `slot-04.md` | `173e1b29a3b59aace8b0b0e1838adc5d4f50927d714406d79d79a0e3ec824b2e` |
| `slot-05.md` | `c54eab09d4521425ce6949c8576c15a6154cb724aedfe9b21ca3b3d018c21405` |
| `slot-06.md` | `e7f3109f3d87a4f610b4f37a068bd8bb07d2cec860da08eb336062111b5fcb97` |
| `slot-07.md` | `bf655687ce3c241378df938237ccc78e1b1c5026da211f6610f79ac5d30f574b` |
| `slot-08.md` | `9d7b8f43777568bd477635c70cd672de1b745c780bce44de5c72e702fc2d8488` |
| `slot-09.md` | `6a301504b84d1e22e99e08f1942644e201f64df73494c3f9ee82cbecb3304b13` |
| `slot-10.md` | `5c8a32595307efea1deb88b2acfae056152b62ac030c238098d95922a2930adb` |
| `blind-score.json` | `0b21e31362557994ebaa9be4bf03c170f63998cf43d37cd63a366f6e8e47797a` |
| `blind-review.md` | `a72b4567690ea10f21f16fc84fdbcb8f5616c979ae44f8c8ebbdd279de78150a` |
| `blind-mapping.json` | `63428bfeb13e85f358f215466f01b9e13324be5fb31798165504c2960340865a` |
| `skill-freeze.json` | `eb2ae586f8bc1367269fe3dd6190d992009ebc80208c2068ba3494a2f7f9a4a2` |

## Independent vectors

| Slot | C1 | C2 | C3 | C4 | C5 | Total | Independent basis for failing bits |
|---|---:|---:|---:|---:|---:|---:|---|
| slot-01 | 1 | 1 | 0 | 1 | 0 | 3 | C3: exceptional push lacks a calendar end date. C5: stop return is only to be newly dated later. |
| slot-02 | 0 | 0 | 0 | 0 | 0 | 0 | Missing full route/classification/unknown handling, complete outcome and initiative fields, focus/continuity/queue envelope, measures/checkpoints, and branch schema. |
| slot-03 | 0 | 0 | 0 | 0 | 0 | 0 | Missing complete route/unknown handling, dated outcome specification and initiative fields, focus/continuity/queue envelope, measures/checkpoints, and branch schema. |
| slot-04 | 0 | 1 | 1 | 0 | 0 | 2 | C1: event date and proposal attribution are omitted; Expo reopen evidence is incomplete. C4: results are not explicitly pending. C5: stop return date is absent. |
| slot-05 | 0 | 0 | 0 | 0 | 0 | 0 | Missing complete route/unknown handling, initiative and outcome fields, focus/continuity/queue envelope, measures/checkpoints, and branch schema. |
| slot-06 | 0 | 0 | 0 | 0 | 0 | 0 | Missing route/unknown structure, complete initiative/outcome fields, continuity escalation and queue test, measures/checkpoints, and branch schema. |
| slot-07 | 0 | 0 | 0 | 0 | 0 | 0 | Missing route/unknown structure, complete initiative/outcome fields, recurring product/recovery/queue envelope, measures/checkpoints, and branch schema. |
| slot-08 | 0 | 1 | 1 | 1 | 0 | 3 | C1: investor diligence and the facilitator/mix unknown are incomplete. C5: stop return date is deferred. |
| slot-09 | 0 | 1 | 1 | 0 | 0 | 2 | C1: exact Expo date and Priya proposal are omitted. C4: results are not explicitly pending. C5: stop return date is deferred. |
| slot-10 | 0 | 1 | 1 | 0 | 0 | 2 | C1: Expo reopen unknown is incomplete and gate IDs are invalid. C4: results are not explicitly pending. C5: stop return date is deferred. |

## Bit changes

None. All 50 independently judged bits match the locked score.

Full per-bit rationales and machine-readable integrity metadata are in `independent-review.json`.
