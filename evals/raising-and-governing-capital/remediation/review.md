# Remediation review

**Score: 8/9. Remediation ready: false.** Hash integrity, prompt hashes, the 1,200-word ceiling, and skill validation pass. The package resolves all three semantic blockers, but the generated responses resolve only two completely.

|Criterion|Score|Finding|
|---|---:|---|
|capital-heavy-route.1|0|Survival is correctly primary and the response rejects software-seed benchmarks and software-style weekly proof, but it never explicitly refuses ramen-profitability defaults (`capital-heavy-route.md:5,28-32,38`).|
|capital-heavy-route.2|1|U1/U2, G0, dated actions, and first-true branches supply the floor, protected obligations, technical/supplier readiness, staged/no-raise choices, and exact September 8 re-entry handoff without launching or pricing a round (`:17-18,24-32,38-43,53-56`).|
|capital-heavy-route.3|1|Letters are zero cash/demand; discussions are qualification only and zero cash. Qualified finance, independent technical, and counsel gates are explicit, with no invented engineering conclusion (`:11-18,32,39-45`).|
|accept-then-close.1|1|C2/T correct the metric everywhere before acceptance; D0/G0/SEL use gates, anchors, frozen weights/aggregation, minimum, margin, and unique-winner behavior (`accept-then-close.md:12,24-25,35-37,44-53`).|
|accept-then-close.2|1|Both fund-signed offers remain company-unaccepted and zero cash; ZaR, ZaE, ZcR, and ZcE are distinct (`:14-18,25,39-42`).|
|accept-then-close.3|1|The four branches cover acceptance-then-close, counter, continue, and decline/no-deal; ties or unresolved evidence cannot accept (`:53,55-62`).|
|mixed-instruments.1|1|The SAFE, priced equity, and debt are normalized across ownership/conversion, cash service, warrant, covenant, lien, maturity, default, and control with qualified owners (`mixed-instruments.md:5,14-18,24-31,35-44`).|
|mixed-instruments.2|1|Milestone coverage and downside/base/upside cash/ownership effects include existing SAFE/pro-rata interactions and staged/no-deal; debt is called cash-burdened and dilutive (`:13-17,24,27-31,52-55`).|
|mixed-instruments.3|1|Weak-market commentary remains claimed pending dated evidence; G0/SEL enforce gates, anchors, aggregation, unique-winner/tie behavior, acceptance evidence, and later closing evidence (`:18,24-25,37-46,52-55`).|

## Integrity

- Declared cases, skill, runtime, and all three prompt SHA-256 hashes match `generation-plan.json`.
- Response hashes: capital-heavy `abd23a00…0545`; accept/close `2de66f62…a92`; mixed `49f3d6a0…b54a`.
- Word counts are 911, 1,037, and 1,099; all are at or below 1,200.
- `quick_validate.py skills/raising-and-governing-capital` passes.
- Cumulative repository taxonomy validation passes with 223 corpus files, 21 skills, 9 routing rules, and no uncovered relevant essays or orphan skills.

## Earlier semantic blockers

1. **Sparse capital-heavy routing/defaults:** package resolved; response not fully resolved. Taxonomy and both runtime contracts require survival first without a completed handoff, and the capital response follows that route, but it omits the explicit ramen-profitability refusal.
2. **Deterministic selection and acceptance before closing:** resolved in package and response. Hard-gated anchored selection and the ZaR→ZaE then ZcR→ZcE state sequence are explicit.
3. **Mixed-instrument normalization and market evidence:** resolved in package and response. Applicable SAFE/equity/debt consequences, claimed-market treatment, deterministic selection, and later closing evidence are explicit.

The only required remediation is to regenerate `capital-heavy-route.md` with an explicit refusal to apply ramen-profitability defaults, then re-freeze and re-review the response hash.
