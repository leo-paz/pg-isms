# Frozen Baseline Review

Generator ID: organization-baseline-generator-001

Fresh scorer ID: org-baseline-rescore

Independent evaluation-contract reviewer: /root/org_eval_contract_review

## Blindness and chronology

The five responses were generated in one ephemeral Codex session rooted at `/tmp`
with a read-only sandbox. The generator received only case IDs and prompts plus the
no-skill instruction in `manifest.json`; criteria were not projected. No target
skill package existed. All responses were frozen and hashed before scoring.

An initial independent review accepted the original rubric and provisional `8/25`
score. After the organization package exposed underspecified conjuncts, an
evaluation-contract review replaced 18 criteria and byte-preserved seven. This was
a criteria-only remediation after generation: case IDs, types, prompts, case order,
prompt projection, and every response byte remained unchanged. The committed
original rubric and score preserve the chronology.

A fresh fork-none scorer then read only the remediated cases, baseline manifest, and
five frozen responses. It did not inspect the target skill, runtime contract,
research, sources, existing scorecards, summary, review, git history or diffs, prior
review artifacts, or intended answers. It required every criterion conjunct and
explicit subcheck to be present and inferred nothing from directionally correct
advice.

## Integrity

- remediated cases: `afae81309f8a6eaf1b0a41ae15df850ac1479a5ad1d7c857918e957d00f6b7e9`
- original cases: `30d0d4a6aee6e1b9aa86275ed7438eecfbcc02adb63133b0191664a74f35d6d3`
- unchanged prompt projection: `e7b1a613d6ac218b52097ecd88b02da6bc1e1f914a0c79e62297f10ebcdc68f9`
- scenario-01: `1ecd19711e48765536645e8f6a19896a0fdbaed80946ea169aca10a3b7bc8385`
- scenario-02: `2bb834d9f7791d306cc1fed74b6ec91f0050d80349fcd14125dbcd1385f327b5`
- scenario-03: `8b3ba95809741ab98d825061e445ed08e060e7abeb85d09468e0cd98ce84fb88`
- scenario-04: `4f12899747d2d20a7ed23115c05bf8de366b628c11d906953a65c6abbcf5d795`
- scenario-05: `eead35ad710e35ed0756ce7675501526e6a2cda7658b01e6f1f766dc1ce22c9c`

The fresh scorer reproduced every hash and confirmed the hidden-criteria/no-skill
generation state and frozen-before-scoring record.

## Result

Score vector: `[0, 0, 0, 1, 0]`

Total: `1/25`

Normalized score: `0.04`

Exact criterion vectors:

- scenario-01: `[0, 0, 0, 0, 0]`
- scenario-02: `[0, 0, 0, 0, 0]`
- scenario-03: `[0, 0, 0, 0, 0]`
- scenario-04: `[0, 1, 0, 0, 0]`
- scenario-05: `[0, 0, 0, 0, 0]`

The 24 exact misses cover precise route and branch selection, complete
observed/claimed/unknown ledgers, bounded-test mechanics, decision predicates,
role charters, interfaces and succession, current HR/legal ownership, exact
cross-skill handoffs, and filled dated decision records. Only scenario-04's use of
the stated survival facts without rescue assumptions passed every conjunct.

## Verdict

RED — valid failing baseline. Integrity, chronology, and scorer blindness pass;
every case has at least one exact miss, and the responses predate the skill package.
