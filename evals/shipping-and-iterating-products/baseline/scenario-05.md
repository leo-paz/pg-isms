# Raw baseline output

Case ID: scenario-05
Reviewer ID: shipping-baseline-001

Product shipping owns the work now: the problem has moved beyond discovery because firms shared real workflows, used a manual version repeatedly, and committed to paid pilots. Engineering owns how to deliver it safely, but replacing the event bus is not the primary workflow unless the existing bus cannot meet the first release's correctness, timeliness, or observability needs. Growth should support pilot recruitment and messaging, not run a broad acquisition campaign before the product produces repeatable value.

The first release should do one narrow job end to end: receive a time-sensitive invoice exception from the existing approval flow, identify the designated approver, send a reliable notification through one agreed channel, link the approver to the exception, record acknowledgement or resolution, and show a minimal status and audit trail to the requester. Limit integrations, channels, routing rules, and administration to what the two paid pilots require. Use the current event bus with a small adapter if it can provide deduplication, retries, delivery status, and monitoring; fix only the infrastructure gaps that block those properties.

The discovery-to-shipping gate has already passed: repeated manual use and paid pilot commitments establish a problem and a testable buyer. The build-to-pilot gate is an end-to-end tested workflow, correct recipient routing, no duplicate or lost notifications in defined failure tests, useful logging and alerts, a manual recovery path, and agreement with each pilot on success measures. Those measures should include notification delivery, acknowledgement time, exceptions resolved before deadline, false or noisy alerts, and continued use across multiple cycles.

The pilot-to-broader-release gate requires both firms to complete real approval cycles reliably, evidence that the workflow improves timely exception handling, acceptable support cost, and no unresolved correctness or security issue. The shipping-to-growth handoff occurs only after the team can onboard another similar firm predictably and can describe the observed value with credible product data. At that point growth can expand to a narrowly defined wholesaler segment; a broad campaign waits until activation and retention are repeatable.
