# Microtest attempt 005 protocol deviation

Status: **invalid for confirmatory acceptance**

The ten responses and all raw scores remain byte-preserved. The observed arithmetic
was control `0/25`, guided `12/25`, delta `+0.48`, but it is exploratory only.

Two predeclared conditions failed:

- Four guided responses contained 1,499–1,792 words, above the prompt's hard
  1,200-word cap, while all five control responses conformed. This arm-specific
  capacity difference confounds the comparison.
- The design required two independent blind scorers. Only the first scorer was
  blind; the later reviewer read `blind-mapping.json`, so its zero-bit-change result
  is not the promised second blind score.

No output was repaired, truncated, regenerated, or rescored to manufacture a pass.
This attempt does not contribute acceptance evidence for the skill. The required
quality-contract evidence is the separate RED baseline and fresh-context forward
evaluation recorded under `baseline/` and `forward/`.
