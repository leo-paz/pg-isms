# Baseline review

## Read boundary

Scoring used only these frozen evaluation inputs:

- `evals/designing-business-models/cases.json`
- `evals/designing-business-models/baseline/manifest.json`
- `evals/designing-business-models/baseline/scenario-01.md`
- `evals/designing-business-models/baseline/scenario-02.md`
- `evals/designing-business-models/baseline/scenario-03.md`
- `evals/designing-business-models/baseline/scenario-04.md`
- `evals/designing-business-models/baseline/scenario-05.md`

No skill, source/taxonomy material, other evaluation, or prior review was read. The frozen cases, manifest, and responses were not altered.

## Integrity proof

- The SHA-256 of `cases.json` is `88f415e5cc5163580cdf4614b0bf6c57459c31d4ba5055c1a8141c843858f3ce`, matching the manifest.
- Case IDs and response-hash keys are the same ordered set: `scenario-01`, `scenario-02`, `scenario-03`, `scenario-04`, and `scenario-05`.
- Frozen response hashes match the manifest exactly:
  - `scenario-01`: `dd13417e6e38b1099f12abd7782f22d263ba3e7df3c58cffcf0ed6447dcee9df`
  - `scenario-02`: `c959d9373b9bb612a0908430d07e8e57966a136112e1462ab6a200d0348b78a2`
  - `scenario-03`: `335b9fe7d20d87943306ce4562a63ece72f49d7e3e2a61e2389b9ea04a738c4d`
  - `scenario-04`: `0b629ebf2a2951d1e59c29239cd3e494699f43bcc9fe2e8ef8aa4ae8958fbf50`
  - `scenario-05`: `052cdae7afea972572fd61cf763aac9cf009603b5a6716c2fbd802e89ea5c3d6`

## Exact misses

### scenario-01

- Criterion 2: No explicit four-way separation of beneficiary, user, buyer, and payer.
- Criterion 3: No explicit offer price/range or predeclared pass/fail commitment threshold.
- Criterion 4: No dated pay/revise/preserve-free/stop branches and no explicit deferral of fine price tuning until payer validation.
- Criterion 5: No required named workflow ownership or handoffs.

### scenario-02

- Criterion 2: Inventory and internal-build estimate uncertainty are not explicit.
- Criterion 3: Supplier-specific failures are not separated from architectural failures.
- Criterion 4: No precommitted thresholds or complete integrate/dual-source/partner/repair/stop branches.
- Criterion 5: No required named workflow ownership or handoffs.

### scenario-03

- Criterion 2: Per-segment records do not explicitly include willingness-to-pay evidence and gross margin.
- Criterion 3: Acceptance, rejection, discounting, and churn interpretations are not predeclared.
- Criterion 4: No dated keep/change/segment/grandfather/stop branches.
- Criterion 5: No required named workflow ownership or handoffs.

### scenario-04

- Criterion 2: The full remit, including investor incentives, is not explicitly routed to raising-and-governing-capital.
- Criterion 3: Return shape and the rule against reopening payer/price/packaging/sales absent new evidence are not explicit.
- Criterion 4: The conditional runway-first route and signed-offer survival caveat are absent.

### scenario-05

- Criterion 1: Plausible exits are not explicitly compared.
- Criterion 3: Both paths are not modeled across all required explicit assumptions.
- Criterion 4: No dated switch condition or explicit evidence-gated outside-capital acceleration rule.
- Criterion 5: No required named workflow ownership or handoffs.

## Result

The frozen no-skill baseline scores **6/25** (`0.24`). All 25 criteria were scored as binary outcomes with no partial credit. The baseline is ready for comparison.
