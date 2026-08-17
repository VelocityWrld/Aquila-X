# Aquila-X Power and Propulsion

## Status

**Status: Proposed configuration set.** The source presents prototype and advanced-design component lists rather than one finalized propulsion and power system. The values below are retained as source statements, estimates, or candidates and are not validated performance specifications.

## Motor configurations

The prototype discussion references approximately four to six brushless DC motors for VTOL, with lower thrust than a later configuration. The advanced configuration references high-thrust brushless motors in a 3000–5000KV range. The source does not establish the final motor count, motor model, thrust requirement, propeller pairing, or airframe geometry.

The source also proposes low-KV brushless motors for quiet operation at lower speeds. This creates a configuration tension with the high-KV range stated for the advanced design. The documentation preserves both statements because the source does not establish whether they describe alternative configurations, a drafting inconsistency, or a final decision.

## ESC role and selection reasoning

An electronic speed controller regulates motor power in response to flight-controller commands. The source identifies braking, smooth acceleration, failsafe behavior, telemetry, low-noise modulation, and soft-start behavior as relevant features. Telemetry may include RPM, temperature, and power draw.

The source lists three to four mid-range ESCs in a prototype configuration and four high-performance ESCs with real-time telemetry in an advanced configuration. It names BLHeli_32 and SimonK as hobbyist examples and T-Motor Alpha and Hobbywing X-Rotor as advanced UAV examples. These are source-mentioned examples, not confirmed selections.

The design rationale is that precise ESC behavior can improve motor control, reduce abrupt energy spikes, and support quieter operation. Sinusoidal or field-oriented control is proposed to reduce switching noise and electromagnetic interference. Soft-start and soft-stop behavior are proposed to prevent sudden audible and electrical transients. Whether these behaviors are available in the selected hardware remains unresolved.

## Battery and battery management

The prototype materials list a 30Ah Li-ion battery pack. The advanced design lists a 30–60Ah smart battery system with a battery-management system and fast-charging circuit. The feature section separately states “30Ah+.” These values are retained as separate source statements; the repository does not select one capacity or claim that the figures are mutually compatible.

The source links battery management to endurance, fast charging, thermal behavior, and power availability for motors, computing, payloads, and communications. It states a possible smart fast-charging result of 60% in 20–30 minutes, but no charger, current, thermal limit, cell arrangement, or test result is provided. The fast-charging figure is therefore an unvalidated source estimate.

The required engineering questions include cell chemistry and configuration, voltage, peak current, discharge limits, BMS behavior, thermal protection, enclosure, mass, charging safety, and reserve policy. The source does not answer these questions.

## Solar augmentation

The source proposes lightweight flexible solar sheets for a prototype and integrated photovoltaic cells with a charge controller in an advanced configuration. It mentions low-wattage sheets, approximately 30–60W support, and a possible endurance contribution of roughly 10–20 minutes.

The source itself qualifies solar contribution as limited unless upgraded. The result depends on available area, illumination, orientation, conversion losses, charge-controller behavior, aircraft attitude, and mission demand. No measurement or energy model is present, so solar augmentation remains a proposed supplement rather than a primary energy source.

## Endurance claims and energy reasoning

The source states an estimated flight time of 120–200 minutes and separately discusses solar augmentation and battery capacity. These are source estimates, not validated endurance. They cannot be treated as a guaranteed operating range because the source does not provide mass, thrust, hover power, payload mass, weather, battery voltage, reserve, or test conditions.

A later validation path proposes comparing flight time with battery use and solar input. Until those measurements exist, the appropriate status is **requires validation**. The source does not establish whether the endurance estimate applies to the prototype, advanced configuration, a particular payload, or a particular flight mode.

## Propellers and acoustic tradeoffs

The source proposes carbon-nylon or composite low-noise propellers, low RPM, large diameter, optimized blade shapes, and a tip speed below 0.7 Mach to reduce high-frequency noise. These choices trade acoustic output against thrust, diameter clearance, mass, motor operating point, efficiency, and airframe packaging. The source does not provide propeller diameter, pitch, blade count, or test data.

Ducted fans are also proposed for safety and noise shielding, with an explicit warning that efficiency may decrease. This remains an alternative rather than a selected architecture.

## Power and propulsion integration questions

The final motor count, motor KV, ESC count, ESC control method, propeller geometry, battery capacity, BMS configuration, charging circuit, solar area, thermal path, and endurance reserve remain unresolved. The power subsystem must eventually be evaluated together with payload operation, Jetson compute load, communications, camera use, and vibration or acoustic controls. No implementation detail should be inferred from common UAV practice.
