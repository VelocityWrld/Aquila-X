# Hardware Specification

## Status

The following hardware list is preliminary and describes candidate classes or source-discussed components. It is not a validated bill of materials.

## Candidate Hardware

| Subsystem | Prototype concept | Later-build concept |
|---|---|---|
| Frame | CFRP with some 3D-printed ABS parts | Aerospace-grade CFRP or titanium-aluminum alloy with thermal and UV protection |
| Motors | Approximately 4–6 brushless VTOL motors | High-thrust brushless motors; exact KV and count require analysis |
| ESCs | 3–4 mid-range ESCs | Four high-performance ESCs with telemetry, subject to final propulsion architecture |
| Battery | 30 Ah Li-ion pack | 30–60 Ah smart battery with BMS and charging protection |
| Flight controller | Pixhawk 6C or Cube Orange class | Final selection pending integration and certification review |
| Onboard compute | Jetson Orin Nano class | Jetson Orin Nano with an Aquila AI Core concept |
| Camera | HD 1080p gimbal camera | Dual HD/thermal PTZ camera concept |
| Sensors | GPS, IMU, barometer, basic Lidar, temperature sensors | Lidar, optical flow, ultrasonic, IR, barometer, and mission-specific sensors |
| Propellers | Carbon-nylon low-noise propellers | Balanced low-noise composite propellers |
| Connectivity | Long-range RF, Wi-Fi, interchangeable 4G dongle | Encrypted and redundant links subject to regulatory review |
| Ground control | Rugged tablet with mission-planner software | Ruggedized operator station with monitoring and audit features |

## Engineering Unknowns

Final mass, center of gravity, thrust-to-weight ratio, motor voltage, current, propeller diameter, thermal limits, structural loads, environmental sealing, electromagnetic compatibility, and component availability remain unresolved. These values must be closed through system engineering before a build is authorized.
