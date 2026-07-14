# Raw held-out output

Case ID: case-001
Generator ID: shipping-heldout-generator-001

# Release decision memo

**To:** TerraFlow leadership

**From:** Product release owner

**Subject:** Pre-expo release of adaptive irrigation approval flow

## Decision

Do not enable the redesign fleet-wide before the expo, and do not combine it with a mandatory, one-step fleet firmware cutover. Before the expo, TerraFlow should make only a bounded, explicitly consented release to the two volunteer customers. Start in shadow mode, and permit the flow to control real watering only after the firmware, offline-reconciliation, fallback, and response-readiness gates below have passed. If those gates cannot pass by a precommitted go/no-go date at least two weeks before the expo, keep the trial non-executing.

At the expo, describe the product as a controlled pilot and show the workflow. Growth may collect qualified interest, but it should not run the drafted all-controller campaign or work the 500-account upsell list as if the product were proven. The three renewals can be offered pilot access later under the same gate; they should not be promised general availability.

The old weather API deadline is a separate continuity problem. Validate and migrate the replacement data source independently, using old/new shadow comparisons and failure handling, without using that deadline to justify adaptive-control exposure. If firmware 7 is needed for service continuity, its rollout must still be staged and must preserve the fixed-schedule mode. A temporary feature flag and fallback are migration controls, not a commitment to support two permanent products.

## Why this is the right release

This is a redesign of an installed, safety-relevant workflow, not a greenfield interface test. The current job is reliably watering zones under intermittent connectivity. Its real artifact includes tuned schedules, physical dials, paper records, seasonal-crew habits, and years of workarounds—not just the web console.

Replay and six agronomists provide useful recommendation-quality evidence: 86% of 180 historical zone-day recommendations were judged acceptable. They do not establish that managers will understand and use the flow, that an approved command will execute correctly, or that vines and allocations will remain safe in live conditions. No vineyard has used it to control water. Watering errors can be irreversible, while the most important harm signals arrive after the expo. Convenience for engineering and an expo date are therefore not release gates.

The smallest complete release is one recommendation for one zone, its explanation, explicit approval by an authorized manager, correct execution, observable confirmation, and safe return to the current schedule or physical control. Automatic execution, broad enablement, removal of existing controls, and a fleet-wide marketing launch are deferred.

## Gates before any live command

The CTO owns the technical gates; the chief agronomist owns agronomic bounds and has independent pause authority; the product lead owns the release record and cohort; the customer-success director owns onboarding and field support; and the COO owns incident coordination, customer notification, and restitution. Before the first live watering, they must record named individuals and obtain a current legal/operational check for local allocation constraints.

Live execution requires all of the following:

- On representative controller hardware, engineering demonstrates recovery from power loss at each relevant point in a firmware 7 update, with configuration and current schedules intact.
- The disconnected queue has a deterministic, tested precedence rule for physical-dial changes. Reconnection cannot create a stale, duplicate, missed, or wrong-zone command, and the manager can see what won and why.
- Loss or staleness of probe, forecast, power, or connectivity data prevents an unsafe recommendation from executing. The controller continues the preserved schedule or makes the defined safe handoff to physical control.
- Existing schedules and physical controls remain available throughout the pilot. There is a tested, fast rollback or safe-disable procedure that does not depend on the failing connection.
- Agronomists set hard per-zone watering bounds and exclusion conditions. Every command requires confirmation by a trained, authorized manager; there is no autonomous mode.
- End-to-end telemetry distinguishes recommendation shown, explanation viewed, approval or rejection, command queued, command applied, physical override, actual water applied, connectivity state, allocation status, missed watering, and stress alerts.
- Both customers give informed consent to the bounded trial and understand the fallback. TerraFlow trains both experienced managers and representative seasonal operators, supplies a simple field procedure, and provides named on-call support during watering windows.

Shadow use is for checking data, bounds, comprehension, and command simulation. A shadow “approval” must not be counted as proof of willingness to approve a command that actually controls water.

## Cohort, comparison, and rollout

Eligibility is limited to the two volunteered vineyards, their 42 identified zones, and managers already using soil probes. Freeze the inclusion rules before results arrive. Begin with a small sentinel set of matched zones at one vineyard; expand to the second vineyard and the remaining enrolled zones only after a calendar review finds no technical or harm trigger. Keep comparable zones on current schedules so the team can estimate a counterfactual, while recognizing that this small, volunteered sample cannot justify fleet-level claims.

Record soil type, forecast and actual weather, connectivity, prior schedule, crew experience, manual changes, probe health, and unusual agronomic events. Compare against matched current-schedule zones and each zone’s historical baseline, with the analysis specified before live exposure. High-touch support, seasonality, weather, and volunteer-customer selection are explicit confounders.

The primary workflow measure is the share of all eligible weekly irrigation events approved and successfully executed through the flow; the denominator may not exclude ignored or abandoned events. The predeclared product thresholds are:

- at least 60% of eligible events approved and executed through the flow;
- at least a 15% reduction in water-allocation overruns against the defined comparison;
- no increase in missed watering or vine-stress alerts; and
- zero unintended, duplicate, stale, wrong-zone, or unreconciled commands, zero lost physical overrides, and zero allocation breaches attributable to the trial.

Also observe rejection reasons, abandonment, repeated use, support load, execution latency, and differences between experienced and seasonal users. Report sample sizes and uncertainty; do not turn a few good days into a fleet forecast.

Any unintended watering command, lost or ambiguous physical override, unrecoverable update, material divergence between commanded and applied water, allocation breach, or agronomist-defined critical stress signal pauses live execution immediately. Restore the preserved schedules and physical-control path, retain evidence, notify the customers, and start the incident and restitution process. Resumption requires a documented cause, a tested fix, and approval from both the CTO and chief agronomist.

## What to do when the first evidence arrives

Hold a calendar review after the first full week of live eligible events, rather than reviewing only when results look favorable.

- **A safety or integrity trigger fires:** stop and roll back; do not “learn through” further irreversible exposure. Engineering owns the cause and fix, agronomy assesses harm, customer success communicates, and the COO handles remediation and restitution.
- **The flow is safe but approval is below 60%:** do not expand. Observe the real path and distinguish novelty, training, seasonal-crew access, trust in the explanation, offline friction, and denominator or instrumentation errors from lack of need. Make the smallest change that discriminates among those causes and repeat in the same bounded cohort.
- **Approval passes but overrun reduction does not reach 15%:** do not scale. Recommendation performance, the comparison, or the water-use hypothesis has failed even if users like the interface. Return that specific uncertainty to the learning owner and test it without broadening exposure.
- **Water improves but missed watering, stress alerts, reconciliation errors, or support burden increase:** treat the harm or operational limit as a failed gate. Pause or narrow the release; benefit does not offset an unbounded safety failure.
- **All early thresholds pass with no trigger:** continue the bounded trial; do not launch broadly. The early result establishes only short-window workflow and water-use evidence. Maintain the comparison and safeguards through at least the roughly ten-week stress window.

At ten weeks, expand only to another small, opt-in cohort of similar probe-using vineyards if usage and water thresholds still hold, there is no increase in sustained stress, technical integrity remains clean, support is workable, and the legal/incident gates remain current. Preserve schedules, physical control, monitoring, and cohort-level disablement. Do not make the feature mandatory.

Continue the original cohort through harvest. Only after end-of-season evidence shows no credible harvest-quality deterioration should leadership consider a staged commercial rollout and activate broader growth and upsell work. Each rollout cohort keeps the same monitoring and pause rules. If harvest quality worsens or remains too confounded to interpret, do not silently declare success: continue bounded evidence collection, redesign the test, or stop the release.
