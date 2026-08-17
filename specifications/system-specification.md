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
