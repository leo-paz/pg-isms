# Runtime contract

Use this reference to produce a compact decision record. Do not replace a specialist's execution plan.

## 1. Select one output mode

Start with `mode`, `primary_skill`, and `reason`. Then use exactly one mode:

| Mode | Predicate | Output and stop condition |
|---|---|---|
| `route-away` | One specialist owns the concrete requested deliverable | Return the exact specialist, inherited guards that matter, known facts/unknowns, and handoff gate; do not build generic options or branches. |
| `source-calibration` | The requested deliverable is only to calibrate a source, prediction, or historical claim | Return the claim, context, mechanism, dated parameters, confidence basis, contrary evidence, and current verification needs; do not invent a company action decision. |
| `cross-domain-decision` | The user explicitly requests one synthesis across domains or no specialist owns the whole consequential choice | Complete sections 2 through 6, then hand execution to the named specialists. |

- Keep `making-calibrated-decisions` primary only for source-calibration or cross-domain-decision mode.
- If one domain owns the requested deliverable, name that exact skill as primary. Apply the seven guards below inside it without creating a second generic process.
- If default-dead, acute cash, or a sparse capital-heavy cash floor binds, route survival before financing.
- Let source calibration precede a specialist, but give execution back after the facts, confidence, and verification needs are recorded.

## 2. Decision header — cross-domain mode only

Record:

| Field | Required content |
|---|---|
| decision | One choice stated so alternatives can be compared |
| owner and deadline | One accountable owner and dated commitment point |
| state | Stage, survival state, product state, and binding constraint |
| product type | Capital-light software, enterprise/integration, hardware, biotech/energy, marketplace/community, or high-harm regulated |
| error profile | Reversibility, maximum credible downside, affected users, and protected obligations |
| evidence clock | Earliest trustworthy result and the cost of waiting |

Do not impose daily or weekly software cadence on long-latency enterprise, hardware, scientific, or regulated evidence.

## 3. Evidence ledger — cross-domain mode only

Classify each material proposition exactly once:

- `observed`: independently measured or directly witnessed; an artifact's existence and literal text may be observed, but the proposition it asserts is not thereby observed;
- `claimed`: asserted by a person, forecast, letter, unsigned document, or source, even when the assertion is preserved in an observed artifact;
- `inferred`: a stated conclusion derived from observations and assumptions;
- `unknown`: missing evidence that can change the decision.

For each consequential unknown give `owner`, `artifact/source`, `due`, `threshold`, and `decision_effect`. Add confidence in words or anchored ranges only when the basis is explicit. Keep at least one rival explanation and one disconfirming observation visible.

Do not equate a good result with a good prior decision or a bad result with a bad one. Review both the process using information available at the time and the later outcome.

## 4. Source calibration

In source-calibration mode, this section is the complete output. In cross-domain mode, embed it only when a source claim affects the decision. Record:

1. the exact claim and context;
2. the durable causal mechanism, if supported;
3. dated parameters requiring current verification, including laws, instruments, costs, platforms, markets, locations, and technology;
4. source incentives, domain contact, contrary evidence, and plausible noise;
5. a resolution date and unambiguous outcome only when a fair credibility update is possible.

Prestige and contrarianism never satisfy an evidence gate. A surprising claim from a domain-connected source may justify a discriminating test, not immediate commitment.

## 5. Option table — cross-domain mode only

Compare every viable option without fake precision:

| Dimension | Required question |
|---|---|
| hard gates | Which safety, cash, control, legal, ethical, or feasibility condition must pass? |
| survival | What obligations and cash floor remain under downside? |
| users | Who benefits or bears error, and how is that effect observed? |
| payoff shape | Is the upside bounded, compounding, thresholded, or power-law, and is this actor diversified enough for that model? |
| reversibility | What can be rolled back, and what becomes irreversible? |
| optionality | Which credible alternative survives, until when, and at what carrying cost? |
| evidence value | Which next action best distinguishes the rival hypotheses before the deadline? |
| delay | What is lost by waiting for better evidence? |

Do not apply an investor's diversified power-law logic to a founder's concentrated personal or company exposure.

## 6. Commitment gates and branches — cross-domain mode only

- Weak evidence + cheap reversible action: run a bounded test with owner, sample or exposure, cap, date, metric, guardrail, and falsifier.
- Irreversible or high-harm action: require current qualified review, stronger independent evidence, staged exposure where possible, protected obligations, and a fallback.
- Long-latency evidence: preserve the option until the earliest trustworthy result or state why the cost of delay justifies a staged commitment.

Return four mutually exclusive branches:

| Branch | Required fields |
|---|---|
| `proceed` | passing predicate, action, owner, date, safeguard |
| `adapt` | mixed-result predicate, bounded change, next evidence |
| `defer` | missing-evidence predicate, preserved option, latest review |
| `stop-or-route` | failed gate, stopped commitment, exact specialist handoff |

Every branch must include a switch condition and make clear what evidence would change the decision.
