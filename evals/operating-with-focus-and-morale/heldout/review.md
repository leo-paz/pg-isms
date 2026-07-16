# Heldout attempt 005 review

Scorer: `focus-heldout-scorer-005`

## Integrity checks

- The prompt embedded in `attempt-005-design.json` is byte-for-byte equal to `prompt.txt` after JSON string extraction: **yes**.
- Prompt SHA-256: `5fc8d0bb86ad026a6624857a0f4828a86ee0e149eab020d9d0ef058c82963970`.
- Response SHA-256: `61851c4c0b4aae971b7a3f0f8678d41241326d8e2a7243755ece0572f1b1d66d`.
- Response word count: **962**, within the hard 900–1,150 band.
- The response was not edited.

## Strict conjunctive scoring

| Criterion | Bit | Rationale |
|---|---:|---|
| `route-and-state-boundary` | 1 | Selects the required primary route; supplies the route record, exclusions, overload-linked wait interpretation, and dated U2 organization-route trigger without inventing adverse state. |
| `evidence-integrity` | 0 | The prompt supplies five claimed propositions, but the ledger gives only four reusable claim IDs. `C2` merges Maya's “longer hours prove seriousness” and “every initiative matters” claims. The criterion requires every proposition to have its own ID, so the whole conjunctive bit fails. |
| `priority-and-competing-work` | 1 | Provides exactly one next-20 planning-call/hold test with the supplied baseline, target, users, owner, mechanism, rival, cadence, falsifier, and final date; protects the named obligations and separately dispositions all six competitors with bounded restart conditions. |
| `execution-morale-and-cadence` | 1 | Preserves all continuity pairs, levels, escalation paths/windows, and artifacts; applies the complete relief envelope and Rosa check; separates the required morale concepts and measures; and records all required future checkpoints as scheduled/not yet observed with the required fields. |
| `branch-and-output-contract` | 1 | Preserves the ordered exhaustive four-branch mapping, all actions/owners/dates/routes and handoff states, decision-now, public-tour option, and all three unknowns; uses filled runtime tables, supplies the lineage boundary, and meets the hard word band. |

Vector: **[1, 0, 1, 1, 1]**  
Total: **4/5**  
Acceptance threshold: **5/5**  
Verdict: **not accepted**.
