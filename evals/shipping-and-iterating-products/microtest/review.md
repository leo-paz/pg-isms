# Shipping and Iterating Products Wording Microtest Review

Scorer ID: shipping-micro-scorer-001

Final rescorer ID: shipping-eval-final-review

Skill SHA-256: `a627063ae70644a5c9d3d3c1c4b224d13b7f5573ce81293b28fac8fc8e2b0ffe`

Rubric SHA-256: `fb7b45b76da13dc9a4072a746fa8482b380668012da1e08dfd07e99e9d257a27`

Rubric frozen before scoring: **true**.

I independently read and scored all ten frozen responses. The artifact contains exactly five control and five guided response/manifest pairs with filename and manifest repetitions 1–5. All ten manifests have the same exact nine keys, correct variant and repetition, a unique nonempty canonical task, model identity `GPT-5`, a valid UTC timestamp, the exact rubric prompt, the correct control-null or current-guided skill hash, and a declared response hash matching the response bytes. The ten tasks and ten response hashes are unique. Control response byte counts are `[7384, 6908, 6459, 6830, 6607]`; guided byte counts are `[9142, 9579, 9255, 8623, 9222]`. All artifact JSON parses, and every response starts with content, ends in exactly one line feed, and has no trailing horizontal whitespace.

Integrity gate: **Pass**. All ten manifests now declare numeric `"schema_version": 1` and share the required exact nine-key schema. The guided repetition 4 generator correction changed only that manifest field; its declared response hash still matches the unchanged response bytes. The rubric and skill hashes remain frozen at the values above.

Scoring required every clause of a criterion to be operational, rather than inferred from general rollout competence. All controls make shipping primary, defer the rewrite and campaign, and provide a representative staged migration with fallback, support, and stop controls. None records a complete falsifiable release rivalry or returns only a newly exposed need uncertainty to learning. Controls 1–4 also fail to measure interruption recovery across experience groups; control 5 measures assisted recovery and passes that criterion. Control scores are `[2, 2, 2, 2, 3]`.

Guided repetition 4 operationalizes all five criteria: it gives growth targeted activation and retention for the already paid segment while keeping broad scaling behind released-workflow evidence. Repetitions 1 and 2 delay that ownership transfer until released-workflow gates pass. Repetition 5 permits bounded pilot activation earlier but contradicts itself by making final ownership conditional on a released cohort passing. Repetition 3 also omits the branch returning contradictory behavior or a newly exposed need uncertainty to learning. Strict guided scores are `[4, 4, 4, 5, 4]`.

Verdict: **Ready Yes.** Normalized mean rises from `0.44` to `0.84` (`+0.40`). Control and guided population score variance are both `0.16`; guided all-criteria pass rate is `0.20` versus control `0.00`. The project acceptance contract requires a verified normalized improvement of at least `0.10`, not a `1.00` guided all-criteria pass rate. The integrity gate passes, the measured improvement is stable and materially exceeds that threshold, and all four strict criterion-5 misses remain disclosed as regression targets.
