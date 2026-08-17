# Aquila-X System Specification

## Status and authority

**Status: Preliminary, conceptual, and non-certified.** This document distributes system-level statements from the Aquila-X source notes. It is not a flight requirement baseline, verified performance report, certification basis, or implementation record.

The source contains prototype, advanced-design, and feature-level statements. Where those statements differ, they are retained as separate configuration references. No value is upgraded from proposed or estimated to implemented, tested, or validated.

## System identity

Aquila-X is described as a VTOL unmanned aerial system with onboard AI processing, modular sensing, HD and thermal imaging, sensor fusion, long-range communications, a ground-control tablet, vibration control, acoustic-reduction measures, and battery or solar-assisted power management.

## Preliminary system statements

| ID | Area | Source-faithful statement | Status | Evidence required |
| --- | --- | --- | --- | --- |
| SYS-001 | Air vehicle | Provide VTOL take-off and landing capability. | Proposed | Airframe inspection and controlled flight testing. |
| SYS-002 | Flight control | Use a dedicated flight controller; Pixhawk 6C or Cube Orange is named as a candidate. | Proposed | Component selection, integration test, and flight test. |
| SYS-003 | Propulsion | Use brushless motors and ESCs to produce controlled thrust. | Proposed | Propulsion integration and restrained testing. |
| SYS-004 | Navigation | Support GPS and IMU fusion, terrain mapping, and Lidar-based obstacle avoidance. | Proposed | Controlled navigation and obstacle tests. |
| SYS-005 | Perception | Support HD, thermal, PTZ, Lidar, optical-flow, ultrasonic, infrared, barometric, GPS, IMU, and temperature sensing in proposed configurations. | Proposed | Sensor inventory, calibration, integration, and environmental testing. |
| SYS-006 | Computing | Use a Jetson Orin Nano-class computer with a proposed Aquila AI Core. | Proposed | Hardware installation and software evidence. |
| SYS-007 | Autonomy | Provide AI-assisted routing or autopilot support under a defined human-oversight boundary. | Conceptual / proposed | Architecture definition, safety analysis, and controlled testing. |
| SYS-008 | Power | Use a Li-ion battery system with BMS; 30Ah prototype and 30–60Ah advanced values are both present in the source. | Proposed; unresolved configuration | Electrical design, mass and thermal analysis, and test. |
| SYS-009 | Solar | Use flexible solar sheets or integrated photovoltaic cells as augmentation; 30–60W and 10–20 minutes are source statements. | Proposed; unvalidated | Energy measurement across defined illumination and mission conditions. |
| SYS-010 | Communications | Consider long-range RF, Wi-Fi, 4G, encrypted 5.8GHz, and possible satellite fallback. | Proposed | Radio selection, spectrum review, security review, and link testing. |
| SYS-011 | Data handling | Consider on-device video processing, encrypted transmission, memory dump/self-wipe, and monitoring functions. | Proposed / requires authorization | Software, security, privacy, and legal review. |
| SYS-012 | Noise and vibration | Reduce vibration and acoustic output through dampeners, propeller and motor choices, ESC behavior, materials, and software modes. | Proposed | Airframe-level acoustic, vibration, control, and payload tests. |
| SYS-013 | Validation | Conduct controlled flight, systems, environmental, data-collection, and iterative tests. | Planned | Test records and review evidence. |

## Source-stated estimates and conflicts

The source gives an estimated flight-time range of 120–200 minutes, possible solar augmentation of roughly 10–20 minutes, and smart charging to approximately 60% in 20–30 minutes. These values are **unvalidated estimates**. The source does not provide payload, mass, voltage, current, reserve, weather, or measurement conditions.

The battery descriptions conflict at configuration level: 30Ah prototype, 30–60Ah advanced design, and 30Ah-plus feature wording. The documentation does not select a capacity. Motor descriptions similarly include lower-KV motors for quieter operation and a 3000–5000KV advanced range. These remain unresolved configuration alternatives.

## Operating assumptions

The source assumes controlled testing, trained or skilled operators, a ground-control tablet, regulated operation where applicable, and review of aviation, privacy, spectrum, and data-security requirements. It does not define a complete operating concept, airspace plan, recovery procedure, or acceptance envelope.

## Scope boundary

The source contains additional non-technical planning material that is outside the scope of this public technical specification.

## Open system questions

The final airframe, motor count, flight-controller selection, sensor subset, control interfaces, autonomy authority, communications configuration, data policy, battery configuration, solar value, endurance, thermal design, weather capability, and validation results remain unresolved or unverified.


## Provisional engineering reference configuration

To make the calculations and compatibility discussion concrete, the repository adopts the following **provisional reference configuration for analysis only**. It is not yet an approved build baseline.

| Subsystem | Provisional reference | Evidence/status |
| --- | --- | --- |
| Flight controller | Holybro Pixhawk 6C | Candidate named by the source; manufacturer data verified for controller-level processor, sensor, power, I/O, dimensions, mass, and temperature limits [1]. |
| Companion computer | NVIDIA Jetson Orin Nano Super Developer Kit | Candidate class named by the source; manufacturer page publishes 67 INT8 TOPS, 8 GB LPDDR5, and 7–25 W power range [2]. Airborne suitability remains unresolved. |
| Propulsion study | Four T-Motor U5 KV400 motors with 6S and 14–16 inch propeller context | Source-compatible candidate study; manufacturer publishes 2.85 kg maximum thrust but not a complete aircraft thrust/current table [3]. |
| Battery study | ENEPAQ 6S 30 Ah Li-ion pack | Matches the source’s 30 Ah concept; manufacturer publishes 21.6 V nominal, 648 Wh, and 3.43 kg [4]. |
| ESC study | T-Motor Flame 60A 12S V2.0 as a 6–12S candidate; H110A as a separate 14S alternative | Neither pairing is closed for U5; the Flame page names U12 compatibility, while the H110A page leaves key current fields unexposed in the visible summary [5] [6]. |

The reference configuration exists to prevent the calculations from mixing incompatible source alternatives. It does not establish final motor count, airframe geometry, maximum takeoff mass, payload, flight mode, or endurance.

## Sourced component data and calculation status

The Pixhawk 6C manufacturer page publishes a 6 V maximum input, 84.8 × 44 × 12.4 mm dimensions, 34.6 g plastic-case weight or 59.3 g aluminum-case weight, 16 PWM outputs, two CAN buses, two GPS ports, and an operating range of −40 to 85 °C [1]. These values describe the controller only.

The NVIDIA page publishes 67 INT8 TOPS, an 8 GB 128-bit LPDDR5 memory subsystem, external NVMe and SD-card support, and a 7–25 W power range for the Jetson Orin Nano Super Developer Kit [2]. These values do not establish the power consumed by a selected AI workload or the suitability of the developer kit for vibration, thermal, or airborne operation.

The reference battery’s nominal energy is calculated as:

```text
E_nominal = V_nominal × C_Ah
E_nominal = 21.6 V × 30 Ah = 648 Wh
```

Using an explicitly provisional 0.80 usable-energy fraction and 0.90 combined system-efficiency factor gives:

```text
E_usable = 648 Wh × 0.80 × 0.90 = 466.6 Wh
```

At assumed average aircraft loads of 500 W, 750 W, 1,000 W, and 1,250 W, the corresponding first-order endurance estimates are approximately 56.0, 37.3, 28.0, and 22.4 minutes. The same loads correspond to nominal pack currents of approximately 23.1, 34.7, 46.3, and 57.9 A at 21.6 V. These are sensitivity calculations, not performance claims; the assumptions must be replaced with measured aircraft power, reserve, payload, and environmental data [4].

The four-motor arithmetic maximum-thrust sum, if the U5 published 2.85 kg maximum is multiplied by four, is 11.4 kgf. This is not a hover or continuous thrust value. The actual propulsion budget remains open because the source page does not provide the full propeller, current, voltage, temperature, and operating-point data needed for an aircraft calculation [3].

## Engineering interpretation

The first-order calculation exposes a direct conflict between the source’s 120–200 minute endurance estimate and the currently evidenced 648 Wh battery candidate. That conflict should remain visible in the specification. It may be resolved only by changing the aircraft power requirement, energy store, mass, propulsion arrangement, mission definition, or endurance claim; it must not be hidden by presenting the source estimate as achieved.

## References

[1]: https://docs.holybro.com/autopilot/pixhawk-6c/technical-specification "Holybro Pixhawk 6C Technical Specification"
[2]: https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/nano-super-developer-kit/ "NVIDIA Jetson Orin Nano Super Developer Kit"
[3]: https://store.tmotor.com/product/u-power-u5.html "T-Motor U5 Power U-Type KV400"
[4]: https://enepaq.com/wp-content/uploads/2025/02/Li-ion-30000-mAh-6S10P-21.6v-Battery-Pack-ENEPAQ-Unmanned-Aerial-Vehicle-UAV-Drones-Unmanned-Ground-Vehicles-UGV-Robots-AGV-and-AMR-battery-pack-Datasheet-1.pdf "ENEPAQ 6S 30 Ah Li-ion pack datasheet"
[5]: https://store.tmotor.com/product/flame-60a-12s-V2-esc.html "T-Motor Flame 60A 12S V2.0 ESC"
[6]: https://www.hobbywing.com/en/products/xrotor-pro-h110a-14s-bldc "Hobbywing XRotor Pro H110A 14S ESC"
