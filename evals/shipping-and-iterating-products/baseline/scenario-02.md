# Raw baseline output

Case ID: scenario-02
Reviewer ID: shipping-baseline-001

Do not silently enable the feature for all 6,000 customers. The two replay failures are rare but demonstrate a known path to moving the wrong amount, and reversal does not undo missed payroll, fees, or penalties. Friday's all-customer launch should be stopped until amended payroll runs are handled correctly or excluded safely.

First, reproduce both failures, define the correct reserve calculation for amendments, fix the logic, and rerun the full historical set plus targeted amendment, duplicate-run, late-change, insufficient-funds, and retry cases. The release gate should require zero wrong-amount transfers in those tests, idempotent processing, a complete audit trail, reconciliation against payroll records, monitoring that detects a mismatch before settlement when possible, and a tested kill switch and correction procedure.

Then run in shadow mode: calculate proposed transfers for live accounts without moving money and compare every result with the amount that should have been reserved. After a sustained clean window, invite a small, informed pilot cohort whose payroll patterns are understood. Start with low transfer limits and manual approval for amendments or anomalous amounts. Give customers a clear preview, timing, amount, explanation, and ability to decline or pause. Have operations review every pilot transfer and reconcile it promptly.

Expand in stages only after each cohort completes multiple payroll cycles with no incorrect transfers, reconciliation and alerts operate as designed, support load is acceptable, and incident drills succeed. Increase limits and automate exceptional cases separately. Broad default enablement requires demonstrated live reliability, explicit legal and compliance approval, customer communication, and a compensation policy for harms caused by the system. Any wrong transfer, unexplained discrepancy, or failed safeguard pauses the rollout and returns affected paths to manual approval.
