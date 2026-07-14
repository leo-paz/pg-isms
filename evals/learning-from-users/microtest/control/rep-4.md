# Six-week learning plan

Treat the dashboard requests as a hypothesis, not the current roadmap. The strongest behavioral evidence is that recruiters reach analytics and then fail at imports; nobody has yet shown deployment or payment intent. Pause the $60,000 acquisition spend until the team can reliably activate the traffic it already has.

## Weeks 1–2: establish the bottleneck

- Founder/product owner: interview 8–10 of the 30 directors, but include the recruiters and managers who do the work. Reconstruct the last attempted import, the approval rule, the consequence of failure, and what would have to be true for a pilot or purchase.
- Engineering: instrument import started, failed, retried, approved, completed, and time-to-first-usable-candidate. Reproduce failures by file type and source system using the two volunteered sandbox datasets.
- By the end of week 2, rank failure causes by frequency and activation impact. Clarify whether manager approval is a customer policy, a product permission defect, or both. Do not remove an intended customer control merely to improve a metric.

## Weeks 3–4: run the smallest corrective test

- Fix only the dominant import path and make failures specific, recoverable, and observable. If approvals are legitimately required, test a safe batch or delegated retry flow with customer administrators.
- Give both sandbox partners an instrumented build and a named support contact. Observe each partner attempting imports without the team driving the screen.
- Measure first-pass import success, median time to a usable candidate set, retries per import, manager interventions, completion of the core recruiting workflow, and return use within seven days.
- Show the existing analytics only after a successful import. Ask users to identify a concrete decision they cannot make, rather than asking which dashboard features they want.

## Weeks 5–6: test commitment and decide

- Repeat the corrected workflow with at least four additional companies from the original 30. Seek a concrete commitment: a security review, named deployment owner and date, signed pilot, or payment—not another expression of interest.
- In week 6, review the evidence. Continue reliability work if at least five of six test companies complete imports, both sandbox partners repeat the workflow, and at least two companies make a dated deployment or commercial commitment. Investigate another bottleneck if imports improve but activation does not. Stop the work or narrow the segment if import success remains poor after the dominant cause is addressed.
- Do not fund the ad campaign during this cycle. Growth may prepare messages and tracking, but paid acquisition resumes only after the activation and commitment threshold is met. Then run a small capped channel test before considering the full budget.

## Decision record

Maintain one dated record with:

- decision: prioritize import activation; defer new analytics and paid acquisition;
- observed facts: four sessions reached analytics but abandoned at import/retry; two sandbox offers; zero deployments and zero payments;
- hypotheses: import reliability is the binding constraint; approval friction compounds it; dashboard demand may be stated rather than behaviorally important;
- experiment, cohort, metrics, thresholds, and customer-data constraints;
- result, links to session notes and event data, remaining unknowns, responsible decision-maker, and a week-6 reconsideration date.

Record contrary evidence as well as supporting evidence. A dashboard request becomes roadmap evidence only when tied to a completed workflow and a deployment or purchasing commitment.

## Ownership handoffs

- The founder owns customer access, commitment asks, and the final week-6 decision.
- Product owns the hypothesis log, event definitions, session synthesis, and acceptance criteria; it hands a ranked defect set to engineering after week 2.
- Engineering owns reproduction, instrumentation, the bounded import/retry fix, privacy-safe sandbox handling, and a rollback path; it hands verified builds and telemetry back to product.
- Customer success owns scheduling, sandbox permissions, administrator coordination, and pilot readiness without coaching users through the test.
- Growth owns the paused-spend decision, prepares the later capped test, and receives the activation threshold and approved audience from product before spending.
