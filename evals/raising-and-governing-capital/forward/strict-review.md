# Strict forward review — attempt 7

Reviewer: `capital-forward7-review-001`  
Frozen vector: `11111 01101 11111 01000 11010`  
Score: **17/25**; adjudicated baseline **1/25**; delta **+16**.  
Vector freeze SHA-256: `fa381f17847413b993a81814d7d57497e1d1043bceb05038cce86f69e60db175`.

All five response hashes match the generation freeze, and word counts are 1,058, 1,118, 778, 968, and 885. No baseline body or prior forward-attempt artifact was read. The baseline summary was read only after the immutable vector was written and hashed.

## Critical findings

1. **The capital-heavy rubric and package route contradict each other.** Scenario 04 criterion 1 requires `raising-and-governing-capital` as primary, but SKILL.md, runtime-contract.md, both taxonomy entries, and `survival-before-capital` require a sparse pre-revenue capital-heavy venture without a completed readiness handoff to route to survival first. The response follows the package and therefore cannot satisfy criteria 1, 3–5. Resolve the taxonomy/evaluation contract before another forward run.
2. **Offer-specific branch contracts remain inconsistent.** The runtime contract mandates the generic deterministic selected-offer family, while scenario 05 requires separate `close-X` and `close-Y` branches. The generic family is safer against a hard-coded winner and correctly separates acceptance from closing, but it fails the frozen criterion as written.

## Important findings

- **Deterministic, non-hard-coded selection:** substantially present. Both offer responses use A/E/C/P/T/Z hard gates, anchored 0/3/5 scores, fixed weights, minimums, tie margins, and a unique-winner rule; neither permits acceptance while evidence is unresolved. Scenario 02 still opens with “Counter A” before A is eligible, and its information/pro-rata acceptance envelope is not explicit.
- **Acceptance versus closing:** ready in the package and exercised. `ZaR→ZaE` is company acceptance; `ZcR→ZcE` is later definitive-document completion and cleared funds. Fund-signed/company-unaccepted offers remain zero cash.
- **Sparse/capital-heavy routing:** internally consistent across skill, runtime contract, taxonomy, and scenario 04, but externally blocked by the frozen case criteria noted above.
- **Mixed-instrument executable coverage:** the runtime contract names priced equity, SAFE/convertible, debt, and revenue-share normalization fields and consequences, but all five frozen responses are priced-equity/round cases. Mixed-instrument execution is not forward-demonstrated.
- **Stage and market handling:** the package explicitly conditions evidence on enterprise, hardware/capital-heavy, seed/inside/later-stage, and hot/weak-market claims. The capital-heavy behavior is exercised; market-regime and inside-round handling are not.
- **Post-close boundary:** clear. Ordinary funded board cadence routes to `building-and-evolving-organizations`; amendments, waivers, consents, rights, disclosure, acceptance, and closing re-enter capital.
- **Branch feasibility:** scenarios 01–03 keep live no-deal options and feasible dates; scenario 03 correctly places the equilibrium handoff after the evaluation horizon. Scenario 04 is feasible for survival but not for its required capital branch family. Scenario 05's generic selected-offer branch is executable but does not meet the offer-specific rubric shape.
- **Response-level omissions:** scenario 02 lacks an explicit current-qualified counsel/finance-or-tax precondition and a complete information/pro-rata envelope. Scenario 04 defers funding ranges and omits the required three-way investor-type comparison. Scenario 05 omits offer-specific current legal/tax comparison controls.

`package_behavior_ready: false`

The package is materially stronger than baseline, especially on truth correction, deterministic gates, no-deal preservation, and acceptance/closing states. Readiness remains false until the package/taxonomy and frozen criteria agree and mixed-instrument execution receives a fresh forward test.
