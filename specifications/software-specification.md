# Aquila-X Software Specification

## Status

**Status: Conceptual software architecture.** No flight-ready, validated, or production software is included. The source names a custom Aquila AI Core, AI autopilot, autonomous routing, terrain mapping, obstacle avoidance, camera tracking, facial recognition, on-device processing, encryption, memory dump or self-wipe, and emergency-landing AI. These remain proposed or conceptual functions.

## Proposed software layers

| Layer | Source relationship | Status |
| --- | --- | --- |
| Flight-control layer | Associated by architecture inference with the candidate flight controller, motor outputs, stabilization, and VTOL control. | Proposed boundary; implementation unspecified. |
| Sensor and state layer | Supports GPS/IMU fusion and the broader Lidar, optical-flow, ultrasonic, infrared, and barometric fusion concept. | Proposed; estimator unspecified. |
| Autonomy layer | Supports terrain mapping, autonomous routing, obstacle avoidance, and AI autopilot concepts. | Proposed; authority and algorithm unspecified. |
| Payload layer | Controls HD, thermal, PTZ, tracking, and recognition concepts. | Proposed; data path and models unspecified. |
| Communications layer | Supports encrypted transmission, long-range RF, Wi-Fi, cellular, satellite fallback, and telemetry concepts. | Proposed; protocols and link priority unspecified. |
| Ground-control layer | Supports tablet mission planning, monitoring, operator interaction, and validation logs. | Proposed; interface unspecified. |
| Failsafe and data layer | Includes proposed redundancy, emergency landing, memory dump/self-wipe, and data-protection behavior. | Conceptual; triggers and implementation unspecified. |

## Flight control and autonomy boundary

The source separately identifies a flight controller and a Jetson Orin Nano-class onboard computer. The software record preserves a likely separation between low-level flight control and higher-level AI computation, but labels it as a documentation inference. The source does not define message formats, timing, command arbitration, watchdog behavior, or what remains available after the onboard computer fails.

AI autopilot, autonomous routing, and terrain mapping are not presented as implemented. They require a defined operator authority boundary and a way to reject or limit unsafe commands. The source does not define geofencing, recovery logic, or the exact meaning of supervised operation; these remain unresolved.

## Perception and analytics

The source proposes camera tracking, live HD feed, thermal and night vision, 360-degree PTZ, facial recognition, on-device video processing, and sensor fusion. It does not specify models, data sets, processing latency, storage, update procedure, confidence thresholds, or human-review workflow.

Facial recognition is retained as a high-risk proposed capability. It is not treated as a default system requirement or a validated output. Any future implementation would require explicit legal authorization, privacy controls, secure handling, accuracy evaluation, and human review.

## Noise and propulsion software

The source proposes sinusoidal or field-oriented ESC behavior, soft-start and soft-stop algorithms, adaptive RPM control based on location, AI path planning that avoids noise-reflective environments, and a software-defined “Stealth Mode.” These functions connect software behavior to acoustic output, power draw, route planning, and flight safety.

The source does not define the control algorithm, sensor inputs, thresholds, priority rules, or override behavior. The mode must therefore remain proposed. It cannot be described as validated stealth or allowed to supersede flight, battery, obstacle, airspace, or emergency constraints.

## Security and data handling

The source proposes AES-256 encrypted transmission, on-device video processing, RF monitoring or interception, and fail-safe memory dump/self-wipe. These functions have different technical and legal implications. The source does not define key management, authentication, authorization, retention, deletion verification, or the scope and authority of monitoring.

The public documentation retains the technical privacy and security concerns from the source. No claim is made that encryption, secure deletion, or monitoring has been implemented.

## Ground-control software

The source names mission-planner software on a rugged tablet. The proposed ground-control layer would need to represent mission plans, provide monitoring, support operator commands, and expose health or recovery states. The source does not define the plan format, link protocol, command authorization, or logging schema.

## Verification status

The source proposes controlled flight and systems testing of stability, VTOL performance, autopilot and AI navigation, camera tracking, facial recognition, solar input versus battery draw, RF behavior, flight time, GPS or airspace precision, heat management, and cooling efficiency. No test evidence is present.

The current software status is therefore **requires validation** for all autonomy, recognition, obstacle-avoidance, failsafe, communications, and stealth-mode claims. The source does not authorize adding simulation results, hardware-in-the-loop results, or test conclusions.

## Open software questions

The implementation language, operating environment, model architecture, estimator, control interface, mission-plan schema, update process, security architecture, data-retention rules, failure behavior, and validation dataset remain unspecified. These gaps are preserved.


## Reference compute integration

The provisional software reference pairs the Pixhawk 6C candidate with the Jetson Orin Nano candidate. Holybro publishes the Pixhawk’s STM32H743 flight-management unit, sensor resources, CAN buses, and PWM outputs [1]. NVIDIA publishes the Jetson Orin Nano Super Developer Kit’s 67 INT8 TOPS, 8 GB LPDDR5, and 7–25 W board power range [2]. These facts support an integration study but do not select firmware, operating system, middleware, model, or message protocol.

The proposed boundary is that the Pixhawk retains the flight-critical actuator and stabilization path, while the Jetson performs higher-level perception or routing assistance. The exact interface, data rate, timestamping, watchdog, command arbitration, and behavior after Jetson failure remain unresolved. The Jetson power range must be included in the aircraft power budget using the selected workload rather than the maximum TOPS label.

## Software requirements and verification intent

| ID | Requirement or design question | Status | Evidence required |
| --- | --- | --- | --- |
| SW-001 | Higher-level AI output shall not bypass the defined flight-control safety boundary. | Proposed safety constraint | Architecture review and command-path fault injection. |
| SW-002 | Companion-computer loss or stale output shall be detectable. | Open requirement | Watchdog, timeout, and controlled failure test. |
| SW-003 | Sensor inputs consumed by autonomy shall expose validity and timing state. | Open requirement | Logged interface review and degraded-input test. |
| SW-004 | Mission-plan commands shall require defined operator authorization. | Open requirement | Ground-control authorization and replay test. |
| SW-005 | Video, thermal, and recognition outputs shall have defined storage, access, retention, and human-review behavior. | Proposed for any future sensitive payload use | Security and data-governance review plus controlled system test. |
| SW-006 | Any proposed Stealth Mode shall remain subordinate to flight, obstacle, reserve, and recovery constraints. | Proposed safety constraint | Mode-boundary and override test. |

The current status of autonomy, obstacle avoidance, recognition, encryption, secure deletion, and emergency landing remains **requires validation**. No implementation detail should be inferred from the presence of a Jetson or a Pixhawk in the component list.

## References

[1]: https://docs.holybro.com/autopilot/pixhawk-6c/technical-specification "Holybro Pixhawk 6C Technical Specification"
[2]: https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/nano-super-developer-kit/ "NVIDIA Jetson Orin Nano Super Developer Kit"
