# Raw held-out output
Case ID: warehouse-robot-production-control-foundation
Generator ID: engineering-heldout-generator-001

# Technical foundation decision memo

**Decision date:** July 14, 2026  
**Decision owner:** VP Engineering, with sign-off from the safety and manufacturing leads  
**Applies to:** the first 200 production robots

## Decision

Freeze a split control foundation for the first production run:

- Keep Ubuntu and ROS 2 for navigation, perception, fleet communication, and diagnostics on a stocked, pin-compatible commercial compute module.
- Move actuator-level motion control and its 20 ms schedule to an industrial microcontroller.
- Retain the independent certified safety controller and keep its emergency-stop path electrically and logically independent of both Linux and the motion microcontroller.

Do not put the first 200 robots on the custom ARM board and niche RTOS. The proposed deterministic scheduler is attractive, but the whole-stack replacement does not fit the six-week hardware-freeze decision: the first board arrives in five months, Lattice has no shipped operational experience with the stack, and several safety-relevant sensor drivers would be new. Its $420 per-unit projection is not a net lifecycle advantage yet. Compared with the split option's $90 saving, the known hardware delta is $66,000 across 200 robots; that does not compensate for custom-board bring-up, driver work, vendor dependence, field-debugging risk, or a schedule that cannot produce fabricated-unit evidence before freeze.

This decision is a conditional production approval, not approval to ship immediately. Failure of a gate below means stop or stage the affected deliveries; it does not mean silently moving motion control back onto Linux.

## Decision context and assumptions

Facts: Lattice has paid use at two warehouses, a contracted deployment, 1,600 robot-hours in benign environments, and a five-person team proficient with the existing x86/Ubuntu/ROS 2 stack. The present co-located system missed a 20 ms deadline in 0.4% of stressed cycles, and a safety controller intervened after a near collision. The incumbent compute module cannot supply the run, production environments are harsher, field service is constrained, hardware freezes in six weeks, and a failure can injure a person or stop a customer aisle.

Assumptions to resolve during qualification: a stocked pin-compatible module can be contracted in production quantities with an acceptable lifecycle; the industrial microcontroller and toolchain are procurable for the run; motion-control semantics can be isolated without moving navigation or perception; and the existing safety controller's certification remains valid after the architectural change. Procurement, safety, security, privacy, and applicable legal/regulatory owners must confirm those assumptions. Lattice should not treat an undeployed bench spike as field evidence.

The binding constraint is a safe, supportable control foundation that can be physically frozen in six weeks and delivered over nine months. The evidence interval is therefore hardware-realistic—fabricated units and weeks of environmental and field testing—not a weekly software preference. The physical freeze is costly to reverse; application software and MCU firmware remain comparatively reversible behind versioned interfaces.

## Why the split is the smallest credible change

The familiar Linux/ROS 2 baseline preserves proven navigation, perception, fleet, diagnostic, deployment, and observability paths. The microcontroller removes its demonstrated predecessor limitation: a safety-relevant periodic loop competing with CPU and network workloads on a general-purpose host. It adds one explicit processor boundary, but avoids replacing every onboard subsystem at once.

The expected leverage is falsifiable: zero motion-loop deadline misses in the bounded qualification workload; bounded safe-stop behavior despite Linux, network, or power faults; fewer safety-critical concepts and new drivers than the RTOS rewrite; delivery before the contract window; and field replacement by customer maintenance staff. The costs to count are MCU integration and tooling, interface debugging, spares, dual-firmware deployment, observability across the boundary, security maintenance, supplier lifecycle, hiring and training, and incident ownership—not merely processor price.

## Boundary and invariants

The motion microcontroller owns the actuator state machine, the 20 ms loop, actuator limits, command freshness checks, and a local controlled-stop transition. Linux may request bounded motion but may not write actuator outputs directly. Commands are versioned, sequence-numbered, time-bounded, range-checked, and safe to retry. Stale, malformed, unauthorized, out-of-order, or missing commands; a lost heartbeat; an MCU watchdog event; or an MCU/Linux reboot must cause the hazard-analysis-defined controlled stop. Intermittent wireless service must never be required to maintain local safe motion.

The independent safety controller retains final emergency-stop authority and must be able to remove motion regardless of Linux or MCU state. The MCU/Linux protocol is a trust boundary with least-privilege access: only the motion service can issue commands, firmware is signed and version-pinned, debug interfaces are disabled or physically controlled in production, and command/state transitions are recorded in a tamper-evident incident log. Logs need synchronized timestamps and sufficient sensor, requested-motion, applied-motion, watchdog, safety-controller, and software-version data for deterministic replay.

After interruption, the robot starts in a non-moving state. It must reconcile Linux's requested route with the MCU's actual actuator state before accepting a new command; it must never infer that an earlier command completed. A fleet or navigation restart cannot resume motion without a fresh, authorized command. The interface has a conformance suite and invariant tests maintained by the controls owner. The robotics lead owns end-to-end behavior; the firmware lead owns the MCU and protocol; the safety lead owns the hazard analysis and independent safety case; the field-operations lead owns recovery procedures. During an incident, the robotics lead is the single technical incident owner.

## Pre-freeze and pre-exposure gates

By August 18, 2026, one week before the assumed August 25 physical freeze, the decision owner must review evidence from the actual candidate compute module, MCU, safety controller, sensors, power system, and production-intent interfaces. At minimum:

1. **Supply and integration:** signed availability for at least 200 modules, MCUs, and service spares; documented lifecycle and alternates; all required camera, lidar, network, and diagnostic paths operating on the pin-compatible module; and a reviewed PCB, thermal, electrical, EMC, and connector design. Any pin incompatibility or unqualified driver blocks the freeze.
2. **Determinism and fault behavior:** no missed 20 ms MCU deadlines in at least 10 million consecutive cycles for each representative production configuration while Linux is under bounded worst-case CPU, memory, storage, and network load. Inject packet loss, delay, duplication, reordering, corruption, process crashes, watchdog resets, brownouts, and power interruption. Every run must preserve the command, authorization, ordering, idempotency, audit, safe-stop, and restart-reconciliation invariants; any unsafe actuator output is a redesign result, not an averageable failure.
3. **Representative hardware:** repeat simulation and hardware-in-the-loop scenarios on fabricated units across the specified cold, dust, vibration, thermal, voltage-sag, sensor-degradation, and intermittent-wireless envelopes. Stop distance, speed, load, aisle-clearance, and recovery thresholds must be predeclared by the qualified safety owner from the hazard analysis. All safety-critical thresholds must pass with margin; this memo does not invent substitutes for that analysis.
4. **Operability and recovery:** a maintenance technician using the production runbook and field tools can identify the failed replaceable unit, replace it, restore a signed known-good image, run self-test, and return the robot to a safe service-ready state within 30 minutes, in 100% of five observed trials per replaceable unit. Rollback to the last qualified Linux and MCU firmware must preserve log and configuration compatibility.
5. **Independent assurance:** the safety lead confirms that the changed control path does not invalidate the certified safety controller's use; current security, privacy, and legal/compliance reviews close all high-severity findings; manufacturing signs the assembly and end-of-line tests; and support signs monitoring, escalation, spares, and customer recovery procedures.

Before any customer exposure, run production-intent robots in a sandbox or cordoned warehouse under the hostile fault matrix. Then stage delivery: a small first cohort, observed shifts in each environmental class, and only then larger batches. Shipping leadership—not this architecture decision—owns cohort size, customer exposure, live monitoring, stop-ship and rollback gates, incident response, communications, and restitution after credible harm. A worker-safety event, collision, unexplained commanded-versus-applied-motion discrepancy, failed safety invariant, or unrecoverable aisle blockage triggers immediate safe stop and stop-ship pending review.

## Alternatives and preserved options

Keeping the entire loop on Linux is rejected for production because the observed stressed miss rate and near collision show that the current co-location is not a capable baseline. The remaining incumbent modules may support controlled engineering work and spares, but not an unqualified production fallback.

The full ARM/RTOS foundation is rejected for this run, not forever. Preserve the option without coupling production to it: keep the MCU command/state protocol hardware-neutral; separate ROS 2 adapters from transport; store deterministic replay fixtures; require exportable logs and configuration; avoid proprietary application semantics in the RTOS; and negotiate source, tooling, license, security-update, data-export, and vendor-exit terms before a trial. Do not build parallel production implementations before evidence justifies them.

The split architecture should itself be reconsidered if the added boundary raises coordination, call-site, incident, recovery, or conceptual cost without delivering the measured control benefit. Retreat means simplifying the protocol or consolidating only onto a foundation that has independently passed the same safety and operability gates; it never means bypassing the safety boundary to meet a schedule.

## Review and switch conditions

Review the decision on January 15, 2027, or after 50 production robots have accumulated 10,000 aggregate hours across at least one cold, one dusty, and one voltage-unstable site, whichever is later. Review motion-loop misses, safety-controller interventions, commanded-versus-applied discrepancies, field incidents, mean recovery time, failed swaps, deployment lead time, cross-team handoffs, interface defects, supplier outlook, and total engineering plus unit cost.

Authorize a time-boxed ARM/RTOS production-intent prototype only if the split foundation has passed its release gates and one of these predeclared conditions is true: the stocked module cannot be secured through the planned service life; measured thermal, reliability, or performance limits cannot be corrected behind the module seam; boundary-related failures or maintenance burden exceed the safety lead's release limits in two consecutive reviews; or audited lifecycle savings, including board and driver engineering, validation, tooling, hiring, support, security updates, migration, and exit costs, repay the switch within the remaining product volume.

Switch a later production revision only after fabricated ARM boards complete the same representative environmental, adversarial, safety, recovery, and field-service gates; all required drivers and observability are production-ready; Lattice has named code and incident owners proficient in the stack; staged field exposure supplies evidence rather than projections; and a behavior-preserving migration and rollback has been demonstrated. Otherwise keep the split foundation, qualify another compatible Linux compute module if necessary, and review again at the next hardware revision.
