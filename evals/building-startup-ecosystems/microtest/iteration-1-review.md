# Microtest iteration 1

Scorer: `ecosystems-micro-scorer-001`

Skill SHA-256: `4e5ed49156cebcb986d8cae7189c091057d71b0da6982b65a3593eec27160fc1`

Five independent control repetitions scored `[1, 1, 1, 1, 1]` (normalized mean `0.20`). Five guided repetitions scored `[5, 4, 4, 4, 4]` (normalized mean `0.84`), a `+0.64` improvement.

The recurring guided miss was incomplete pre-allocation feasibility gating in repetitions 2–4; repetition 5 omitted an explicit accountable owner. The skill was revised to require all four named gate results before a recommendation and to forbid an experiment record without a named accountable owner. This is a refinement record; final manifests and scoring replace iteration one.
