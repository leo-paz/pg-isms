# Independent review: building-and-evolving-organizations microtest

Date: 2026-07-15  
Review protocol: strict two-stage independent scoring, followed by canonical comparison

## Final verdict

**PASS after one canonical scoring correction.** The corrected control score is **2/25 = 0.08** and the corrected guided score is **15/25 = 0.60**. The corrected effect is **+0.52**, exceeding the predeclared **`>= 0.20`** threshold by **+0.32**.

The canonical artifacts initially over-credited guided rep 4 C5. That bit, its sample total, the guided aggregate, effect, margin, scorer report, and scorecard were corrected during this review and independently reverified. This reviewer did not edit canonical files.

## Stage A freeze

Stage A was written before any canonical summary, scorer report, or scorecard was opened.

- Artifact: `.superpowers/sdd/org-micro-independent-stage-a.json`
- SHA-256: `e453fe3c5bfc5030ccd1cb8e62dbe57e87169e34261c7debd41a900ce9574f4d`
- Size: 17,311 bytes
- Control vectors: `10000`, `10000`, `10000`, `10010`, `10010` = **7/25 = 0.28**
- Guided vectors: `11110`, `11110`, `11110`, `11111`, `11111` = **22/25 = 0.88**
- Stage-A effect: **+0.60**, gate **PASS**

The frozen Stage-A file remains unchanged. It contains all 50 independent bit decisions and rationales plus the reproduced integrity ledger.

## Exact vector and total comparison

| Sample | Stage A | Canonical at first open | Corrected final | Stage A → final differences |
|---|---:|---:|---:|---|
| `org_micro_control_1` | `10000` (1) | `00000` (0) | `00000` (0) | C1 |
| `org_micro_control_2` | `10000` (1) | `00000` (0) | `00000` (0) | C1 |
| `org_micro_control_3` | `10000` (1) | `00000` (0) | `00000` (0) | C1 |
| `org_micro_control_4` | `10010` (2) | `00010` (1) | `00010` (1) | C1 |
| `org_micro_control_5` | `10010` (2) | `00010` (1) | `00010` (1) | C1 |
| `org_micro_guided_1` | `11110` (4) | `10110` (3) | `10110` (3) | C2 |
| `org_micro_guided_2` | `11110` (4) | `01110` (3) | `01110` (3) | C1 |
| `org_micro_guided_3` | `11110` (4) | `01110` (3) | `01110` (3) | C1 |
| `org_micro_guided_4` | `11111` (5) | `01111` (4) | `01110` (3) | C1, C5 |
| `org_micro_guided_5` | `11111` (5) | `01110` (3) | `01110` (3) | C1, C5 |

Stage A and the canonical scorer initially agreed on 39 of 50 bits and disagreed on 11. The guided-rep-4 C5 re-adjudication exposed one shared error, so Stage A and the corrected canonical result agree on 38 bits and differ on 12. The JSON companion records the bit and rationale comparison for every criterion in every sample.

## Adjudication of disagreements

### Stage-A corrections accepted

- **Nine C1 bits:** control reps 1–5 and guided reps 2–5 reject broad delegation, a COO, a council, another layer, or several enumerated structural changes, but do not explicitly reject or defer **broad reorganization** as its own option. Under the all-conjunct rule, all nine C1 bits are 0.
- **Guided rep 1 C2:** the memo has a strong observed/claimed/unknown ledger, but it does not explicitly categorize proposed-boundary quality and future pilot effects as unknown. C2 is 0.
- **Guided rep 5 C5:** its capacity rule does not explicitly require interface causes to have been addressed, and Keep, Revise, and Capacity do not each name a next owner. C5 is 0.

### Canonical correction required and applied

- **Guided rep 4 C5:** the Keep result states what happens but does not name its next owner. Global text such as “leadership applies” or the header’s accountable owners cannot be imported into each result under the scorer’s own no-inference rule. Because every required result must name its next owner and action, C5 is **0**, not 1.

This changes guided rep 4 from `01111`/4 to `01110`/3, guided total from 16 to 15, guided score from 0.64 to 0.60, effect from +0.56 to +0.52, and margin from +0.36 to +0.32. The PASS gate is unchanged.

## Corrected final scoring

| Arm | C1 | C2 | C3 | C4 | C5 | Total | Normalized |
|---|---:|---:|---:|---:|---:|---:|---:|
| Control | 0 | 0 | 0 | 2 | 0 | 2/25 | 0.08 |
| Guided | 1 | 4 | 5 | 5 | 0 | 15/25 | 0.60 |

`(15 - 2) / 25 = 13 / 25 = 0.52`

`0.52 >= 0.20` → **PASS**

## Integrity and artifact review

All reproducible canonical integrity claims passed:

- 10 samples, split 5/5, with unique tasks, sample IDs, paths, and response hashes; indices are 1–10.
- All response hashes, byte counts, and word counts match the attestation; the maximum is 1,450 words and all are below 1,500.
- Plan/attestation mappings align. The generation-plan, rubric, prompt-derived, criteria-derived, attestation, and skill-freeze hashes and sizes all reproduce.
- Frozen skill and runtime targets were checked **only by SHA-256 and size**, never opened. Both match `skill-freeze.json`.
- The scorer’s ignored-audit JSON and Markdown hashes and sizes reproduce without opening their contents.
- The plan/attestation declarations are internally consistent: frozen-before-generation, response generation not started in the plan, and no post-generation revision in the attestation.
- The corrected summary, report, and all scorecards now agree on every vector, rationale, total, effect, margin, and PASS verdict.

Fresh context, hidden inputs, first-completion freezing, forbidden quality resampling, and the scorer’s blind-read history are process attestations, not independently reconstructible facts. They are explicitly presented as declarations, are internally consistent, and have no contradictory frozen artifact.

## Corrected canonical artifact hashes

- `summary.json`: `0e00f619aad1819e544e8ed4b4a30811ee7c504abe0fb6539e5c11d2cd8bf897`
- `scorer-report.md`: `f6c566dca7987383b1bd00b9f7ece16260c04dd917ed6a3c3932a3ba9acbe7cc`
- `scorecards/org_micro_guided_4.md`: `23364c17213f5698df6ebec8fe4fa322af52c635ce7ffb1700f98b0a6541a2e0`

All other scorecard hashes are recorded in the JSON companion.
