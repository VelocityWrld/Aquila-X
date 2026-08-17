# Aquila-X System Architecture

## Architecture status

**Status: Proposed architecture.** The source describes a VTOL airframe with a flight-control layer, propulsion and power systems, onboard AI computation, perception sensors, communications, payloads, and a ground-control tablet. The relationships below are documentation of the source concept, not a confirmed implemented architecture.

## Major subsystems

| Subsystem | Source-described role | Status and limitation |
| --- | --- | --- |
| Airframe and mechanical structure | Provide the VTOL structure, component mounting, environmental protection, and thermal-management surfaces. | Proposed. The source discusses lightweight CFRP, aerospace-grade CFRP, titanium-aluminum alloy, 3D-printed ABS parts, vents, cooling fins, and IP65-plus weather resistance in different configurations. |
| Propulsion and ESC layer | Convert battery power into controlled motor thrust and support braking, acceleration, telemetry, and low-noise behavior. | Proposed. Motor count, motor KV, ESC count, and final operating point remain configuration-dependent. |
| Power subsystem | Supply propulsion, avionics, payload, computing, and communications, with BMS and possible solar augmentation. | Proposed. Battery capacities, solar contribution, charging time, and endurance are source estimates requiring validation. |
| Flight controller | Receive pilot or autonomy commands and control motor outputs for VTOL flight. | Candidate hardware is Pixhawk 6C or Cube Orange; implementation is not established. |
| Onboard compute | Run the proposed Aquila AI Core functions, including perception-related processing and autonomous routing concepts. | Jetson Orin Nano is source-described; custom software implementation is not established. |
| Perception and payloads | Provide HD, thermal, PTZ, GPS, IMU, barometric, Lidar, optical-flow, ultrasonic, infrared, and temperature data in various configurations. | The source does not establish that all sensors are present simultaneously or that any one sensor suite is final. |
| Communications | Provide long-range RF, Wi-Fi, cellular, encrypted links, and possible fallback or monitoring functions. | Proposed and subject to legal, spectrum, privacy, and security review. |
| Ground control | Provide mission planning, operator access, monitoring, and a human control path through a rugged tablet. | Proposed. The source does not define a complete interface or protocol. |
| Failsafe and data handling | Support emergency landing, redundancy, encrypted transmission, on-device processing, and possible memory handling. | Proposed or conceptual. No implementation or validation evidence is provided. |

## Layering and control boundaries

The source separately names a flight controller and an onboard Jetson Orin Nano-class computer. The documentation therefore preserves a layered interpretation: low-level flight control is associated with the flight controller, while higher-level AI processing and autonomous routing are associated with the onboard computer. This is a **documentation inference** from the component separation; the source does not specify the complete software boundary, message protocol, timing model, or failure behavior between the two layers.

This separation is relevant because the source simultaneously discusses stable VTOL control and computationally demanding functions such as terrain mapping, camera processing, facial recognition, sensor fusion, and autonomous routing. The source suggests an assistance model rather than an established replacement of flight control by AI. The ground-control tablet remains part of the proposed system, so operator access and human oversight are also architectural concerns.

## Payload and sensor relationships

The source lists a dual HD/thermal PTZ camera system and separately lists GPS, IMU, barometer, Lidar, optical flow, ultrasonic, infrared, and temperature sensors. It also describes sensor fusion as Lidar plus optical flow, ultrasonic, infrared, and barometric data. These are candidate data sources for perception and state estimation, not a completed fusion implementation.

The camera and sensor mounting decisions are linked to vibration control. The source recommends rubber dampeners, silicone grommets, foam mounting, and shock-absorbing landing gear because vibration can reduce video stability and introduce sensor error. This creates a mechanical-to-perception dependency: the sensing design cannot be evaluated independently from the airframe, motor, propeller, and mounting design.

## Power, thermal, and mechanical coupling

The architecture couples stored energy, propulsion, thermal management, and payload operation. A larger battery may support longer operation but increases mass. Solar sheets may augment energy but are described as low-wattage, and the source warns that their contribution may be limited unless the design is upgraded. Vents and cooling fins are proposed for heat management, but the source provides no thermal model or test result.

Noise reduction adds another cross-subsystem dependency. Low-noise propellers, low-KV motors, sinusoidal or field-oriented ESC behavior, soft start/stop algorithms, acoustic materials, motor mounts, and adaptive RPM control affect propulsion, power draw, vibration, software behavior, and payload stability at the same time.

## Interfaces that remain unspecified

The source does not define exact electrical or software interfaces between the flight controller, ESCs, onboard computer, camera system, sensors, communications equipment, and ground-control tablet. It also does not define how autonomous commands are authorized, how conflicting sensor inputs are resolved, how the system behaves after a compute failure, or how emergency landing logic is separated from ordinary autonomy.

These are **unresolved questions**, not missing details to be filled by convention. The current documentation records the subsystem relationships and leaves the implementation boundary open for later owner clarification or engineering work.

## System-level tradeoffs

The architecture repeatedly trades capability against mass, power, vibration, noise, complexity, and regulatory exposure. Solar augmentation may add endurance but may provide only a limited boost. Ducted fans may improve safety and noise shielding but are described as costing some efficiency. Dampeners may reduce vibration but add weight and require careful placement. A richer sensor and payload set may improve perception but increases integration and processing requirements.

The source also proposes stealth-oriented features such as dampened motors, quiet propellers, adaptive RPM control, and a software-defined “Stealth Mode.” These are acoustic design proposals, not evidence of undetectable or validated low-signature flight.

## Architectural questions for later work

The source leaves the following questions open: which airframe material and propulsion configuration is current; which sensor subset is actually intended; where the authority boundary lies between operator, flight controller, and onboard AI; how sensor disagreement is handled; what communications and fallback functions are authorized; how data is retained or erased; and which proposed features are removed when they cannot be validated or legally operated.
