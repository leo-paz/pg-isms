# Frozen Baseline Review

Reviewer ID: organization-baseline-generator-001

Scorer ID: organization-baseline-scorer-001

Independent reviewer: /root/org_baseline_review

## Blindness and chronology

The five responses were generated in one ephemeral Codex session rooted at `/tmp`
with a read-only sandbox. The generator received only the case IDs and prompts plus
the no-skill instruction recorded in `manifest.json`; criteria were not projected.
No target skill package existed. All five responses were frozen and hashed before
the criteria were supplied to a distinct scorer.

The independent reviewer read only the cases, manifest, and frozen responses before
fixing its own score vector. It did not read source material, taxonomy, intended
skill behavior, prior evaluations, git history, or the external proposed scoring.
After fixing its vector, it compared all 25 bits with the proposed score and found no
disagreement.

## Integrity

Integrity passed after one manifest-only provenance correction. The first manifest
had recorded a digest of the full dispatch text while labeling it as the prompt-only
projection. No case or response changed. The corrected contract explicitly hashes
the compact ordered `{id,prompt}` array with one final LF.

- cases: `30d0d4a6aee6e1b9aa86275ed7438eecfbcc02adb63133b0191664a74f35d6d3`
- prompt-only projection: `e7b1a613d6ac218b52097ecd88b02da6bc1e1f914a0c79e62297f10ebcdc68f9`
- scenario-01: `1ecd19711e48765536645e8f6a19896a0fdbaed80946ea169aca10a3b7bc8385`
- scenario-02: `2bb834d9f7791d306cc1fed74b6ec91f0050d80349fcd14125dbcd1385f327b5`
- scenario-03: `8b3ba95809741ab98d825061e445ed08e060e7abeb85d09468e0cd98ce84fb88`
- scenario-04: `4f12899747d2d20a7ed23115c05bf8de366b628c11d906953a65c6abbcf5d795`
- scenario-05: `eead35ad710e35ed0756ce7675501526e6a2cda7658b01e6f1f766dc1ce22c9c`

The independent rerun reproduced all hashes, the five required case types, five
criteria per case, the hidden-criteria/no-skill state, the external context, and the
frozen-before-scoring record.

## Result

Score vector: `[1, 2, 1, 3, 1]`

Total: `8/25`

Normalized score: `0.32`

Exact criterion vectors:

- scenario-01: `[1, 0, 0, 0, 0]`
- scenario-02: `[1, 0, 1, 0, 0]`
- scenario-03: `[1, 0, 0, 0, 0]`
- scenario-04: `[1, 1, 0, 1, 0]`
- scenario-05: `[1, 0, 0, 0, 0]`

The 17 exact misses concern explicit observed/claimed/unknown separation, bounded
test mechanics, decision thresholds and branches, dated records and accountable
owners, pre-search role design, end-to-end ownership protections, current HR/legal
routing, and a defined escalation boundary. No missing behavior was inferred from
adjacent generic advice.

## Verdict

RED — valid failing baseline. Integrity and blindness pass; every case contains at
least one exact miss, and the target skill package has not been initialized.
