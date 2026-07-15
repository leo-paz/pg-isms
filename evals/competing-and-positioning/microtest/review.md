# Strict scoring review — attempt 13

Integrity passed. All 13 authorized inputs match their recorded SHA-256 hashes and byte counts. The ten response tasks, sessions, hashes, and bodies are unique; planned and attested tasks match; chronology is valid; arm boundaries and frozen-state assertions are consistent between the plan and attestation. Every response has the correct arm/replication headers, no trailing whitespace, and exactly one final LF. Frozen inputs were not modified.

Scoring used five strict conjunctive booleans per response. A criterion received `1` only when every clause was satisfied; partial coverage received `0`.

## Results

- Control vectors: `[0,0,0,0,0]`, `[0,0,0,0,0]`, `[0,0,0,0,0]`, `[0,0,0,0,0]`, `[0,0,0,0,0]`
- Guided vectors: `[1,1,1,1,1]`, `[1,1,1,1,1]`, `[1,1,1,1,1]`, `[1,1,1,1,1]`, `[1,0,1,1,1]`
- Control mean: `0.00`
- Guided mean: `0.96`
- Guided-minus-control effect: `+0.96`
- Materiality threshold: `0.20`
- Verdict: material positive guided effect

## Exact miss review

Every control response fails C1 because it has no `competing-and-positioning` primary owner, ordered named-skill handoffs, or specialist owner map. Every control fails C2 because it omits the material manual/status-quo alternative and does not explicitly separate observed facts from inferences. Every control fails C3 because it lacks the complete causal advantage chain plus the full incumbent ability, incentive, legacy-constraint, likely-response, and durability test. Every control fails C4 because it lacks the complete dependency record and a bounded voluntary builder-user loop with exposure limits and executed rollback proof. Every control fails C5 because it does not select all required branches or precommit all outcomes with observable dated conditions, guardrails, disconfirmation, preserved options, and next owners.

Guided reps 1–4 satisfy all five criteria. Guided rep 5 fails only C2: it handles the enterprise job, native summary, open model, integrated workflow, and fact/unknown separation, but never maps the material manual/status-quo alternative. Under conjunctive scoring, that single missing clause makes C2 false.
