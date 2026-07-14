# Six-week learning plan

The current evidence points to import reliability and approval friction, not missing analytics. Treat the thirty dashboard requests as hypotheses until directors or recruiters demonstrate the underlying job and its priority. Do not spend the $60,000 yet: with no deployment or payment, ads would amplify an unproven funnel and obscure the product failure.

## Weeks 1–2: reproduce and instrument

- The product lead owns four to six observed import attempts across the two sandbox partners, using realistic files. Record file shape, failure point, retry count, approval delay, time to first usable candidate, and whether the user reaches analytics afterward.
- Engineering owns import-stage telemetry, stable error codes, and a reproducible test corpus. Support tags every related issue against those stages.
- The founder interviews the requesting HR directors about the decision they hoped the larger dashboard would enable, then asks them to show their present workaround. Separate buyer requests from recruiter behavior.
- Establish a baseline: successful imports, median time to first usable candidate, retries per import, approval wait, activation to a completed recruiting workflow, and partner willingness to schedule the next session.

At the end of week 2, choose the smallest fix that addresses the dominant observed failure. Likely candidates are better validation and recovery for common files plus removal or batching of redundant retry approvals. Do not build the larger dashboard unless observation shows an important decision is impossible with the existing view.

## Weeks 3–4: run a narrow product test

- Engineering and design ship the smallest reversible import/retry improvement behind a partner flag.
- Each sandbox partner runs at least three new imports without staff taking over the task. Compare the same measures with baseline and capture the exact point of abandonment or completion.
- The founder asks each partner for a concrete next commitment: connect a real workflow, name the deployment owner and date, or decline. A compliment or another feature list does not count.
- The growth lead spends no ad budget, but may prepare message variants based on the observed problem and recruit a small number of additional matched design partners manually.

## Weeks 5–6: test adoption and decide

- Move a partner into a constrained real-workflow pilot only if its data and security requirements permit it. Require a named operator, scheduled imports, and a deployment or paid-pilot decision date.
- Repeat the import-to-workflow measures and verify that improved import success produces downstream usage, not merely successful setup.
- Conduct one final session on the dashboard request after users can reliably reach it. Prototype only if users cannot complete a valuable decision with the current analytics.

Decision rule at week 6: continue investing in imports if both partners can import without assistance, approval-related delay falls materially, and at least one accepts a dated deployment or paid-pilot step. Revise the intervention if imports improve but workflow use does not. Stop this path and investigate the next observed bottleneck if neither partner makes a concrete commitment. Release ad spend only after the product repeatedly activates matched users and the team can state which problem and audience the campaign will test.

# Decision record

Maintain one dated record after each session and a consolidated decision at weeks 2, 4, and 6:

- hypothesis and decision to be made;
- evidence observed, with partner, role, sample size, and telemetry link;
- baseline and post-change measures;
- alternatives considered, including “no change”;
- what would disconfirm the hypothesis;
- decision, confidence, unresolved risks, and next commitment;
- owner, due date, budget authorized, and next review date.

Record requests and observed behavior separately. Label sandbox results as pre-deployment evidence, not customer validation.

# Ownership handoffs

- Founder/product lead: owns the learning question, sessions, partner commitments, and week-6 decision. Hands a ranked, evidence-linked problem statement to engineering; does not hand over a feature order.
- Engineering lead: owns instrumentation, reproducibility, the bounded fix, and reliability measures. Hands verified release notes and metric results back to product.
- Design/research: owns task observation and dashboard-decision prototype only if evidence warrants it. Hands session notes and behavioral patterns to product.
- Partner deployment owner: supplies representative data, runs the workflow, and accepts or rejects a dated next step.
- Growth lead: owns manual recruitment and message preparation during the test. Receives budget authority only after the activation and commitment gates pass; then runs a capped acquisition experiment with its own stop rule.
