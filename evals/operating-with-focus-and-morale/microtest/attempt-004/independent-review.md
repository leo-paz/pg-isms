# Independent review — operating-with-focus-and-morale microtest attempt 004

## Result

All 50 binary judgments were independently rejudged under the conjunctive rubric. No bit changes are warranted.

- Control: `0/25 = 0.00`
- Guided: `8/25 = 0.32`
- Guided minus control: `0.32`
- Acceptance threshold: `>= 0.20`
- Decision: **accept**

Both arms contain exactly five attested, uniquely hashed responses from five distinct task identities.

## Independent vectors

Criteria order: `C1 C2 C3 C4 C5`.

| Slot | Independent vector | Total | Blind vector | Correction |
|---|---:|---:|---:|---|
| `slot-01` | `0 1 0 0 0` | 1 | `0 1 0 0 0` | none |
| `slot-02` | `0 0 0 0 0` | 0 | `0 0 0 0 0` | none |
| `slot-03` | `0 1 1 0 0` | 2 | `0 1 1 0 0` | none |
| `slot-04` | `0 1 0 0 1` | 2 | `0 1 0 0 1` | none |
| `slot-05` | `0 0 0 0 0` | 0 | `0 0 0 0 0` | none |
| `slot-06` | `0 1 0 0 0` | 1 | `0 1 0 0 0` | none |
| `slot-07` | `0 0 0 0 0` | 0 | `0 0 0 0 0` | none |
| `slot-08` | `0 0 0 0 0` | 0 | `0 0 0 0 0` | none |
| `slot-09` | `1 1 0 0 0` | 2 | `1 1 0 0 0` | none |
| `slot-10` | `0 0 0 0 0` | 0 | `0 0 0 0 0` | none |

Criterion totals remain `C1=1, C2=5, C3=1, C4=0, C5=1`; overall `8/50`.

## Strict audit notes

- `C1`: Only `slot-09` satisfies every route, claim-integrity, unknown-contract, and fact-integrity clause. The other structured guided responses each retain at least one claim-classification or independently contracted-unknown defect; the control responses omit the required route/exclusion and persistence-switch treatment.
- `C2`: `slot-01`, `slot-03`, `slot-04`, `slot-06`, and `slot-09` each provide one current-member outcome, one tactic/evidence loop, a complete priority row, all initiative dispositions, and all protected essentials. The other slots lack at least one complete priority-row or disposition requirement.
- `C3`: Only `slot-03` gives accountable owner Ellis both recurring protected analysis and recurring direct at-risk-member contact, bounds coordination/availability, supplies the required coverage contract, and meets recovery and morale-diagnosis clauses. Every other slot fails at least the same-owner pair or complete coverage contract.
- `C4`: Every slot misses at least one conjunctive requirement. Most notably, none requires checkpoints to record observed result, confounders, safeguard status, and the precommitted branch together.
- `C5`: Only `slot-04` has a complete and semantically valid four-branch contract while staying within 1,200 words and including the lineage line. Slots `01`, `03`, `06`, and `09` exceed the word limit; the remaining slots lack the required four-row matrix and/or lineage.

## Hash and mapping verification

The recomputed SHA-256 values for `prompt.txt`, `rubric.json`, and all ten blind responses exactly match `blind-score.json`. Every blind slot also matches the SHA-256 attested for its mapped arm/rep:

| Slot | Mapping | SHA-256 match |
|---|---|---|
| `slot-01` | `guided/rep-5.md` | yes |
| `slot-02` | `control/rep-1.md` | yes |
| `slot-03` | `guided/rep-1.md` | yes |
| `slot-04` | `guided/rep-4.md` | yes |
| `slot-05` | `control/rep-4.md` | yes |
| `slot-06` | `guided/rep-2.md` | yes |
| `slot-07` | `control/rep-5.md` | yes |
| `slot-08` | `control/rep-3.md` | yes |
| `slot-09` | `guided/rep-3.md` | yes |
| `slot-10` | `control/rep-2.md` | yes |

All ten response hashes are unique. Recomputed word counts also match the generation attestation.

## Arm calculation

| Arm | Mapped slots | Raw | Possible | Normalized |
|---|---|---:|---:|---:|
| Control | `02, 10, 08, 05, 07` | 0 | 25 | 0.00 |
| Guided | `03, 06, 09, 04, 01` | 8 | 25 | 0.32 |

`0.32 - 0.00 = 0.32`, so the paired microtest clears the `0.20` minimum effect by `0.12`.
