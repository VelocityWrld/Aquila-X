# Aquila-X Sensing and Perception

## Status and purpose

**Status: Proposed sensor and payload architecture.** The source describes sensing for vehicle state, obstacle awareness, navigation assistance, and authorized observation. It does not establish that the complete sensor set has been assembled, calibrated, or validated.

## Source-described sensing set

The source lists GPS, IMU, barometer, a basic Lidar unit, temperature sensors, optical flow, ultrasonic sensing, and infrared sensing. It also describes HD 1080p imaging, a gimbal with pan-tilt-zoom, and a dual HD/thermal PTZ camera system. These descriptions occur in different configuration sections; the source does not establish that every item is installed at the same time.

| Source element | Proposed role in the concept | Status limitation |
| --- | --- | --- |
| GPS | Position reference and navigation input. | Proposed; accuracy, availability, and failure behavior are unspecified. |
| IMU | Motion and attitude-related measurement for flight and sensor fusion. | Proposed; calibration, drift, and mounting requirements are unspecified. |
| Barometer | Pressure-based altitude input and part of the proposed sensor-fusion set. | Proposed; environmental sensitivity and fusion weighting are unspecified. |
| Lidar | Obstacle avoidance, terrain mapping, and range information. | Proposed; the source only calls one prototype item a basic unit and gives no range or test result. |
| Optical flow | Motion or position support and sensor fusion. | Proposed; lighting and surface constraints are unspecified. |
| Ultrasonic and IR | Additional short-range or environmental sensing inputs. | Proposed; exact role and integration are unspecified. |
| Temperature sensors | Health and thermal monitoring. | Proposed; sensor locations and limits are unspecified. |
| HD camera | Live video, tracking, and observation. | Proposed; 1080p is source-stated for a prototype camera discussion. |
| Thermal camera | Night or thermal imaging in the dual-camera concept. | Proposed; thermal performance is unspecified. |
| PTZ gimbal | Pan, tilt, zoom, and 360-degree observation concept. | Proposed; range of motion, stabilization, and control interface are unspecified. |

## Why sensing is coupled to structure and vibration

The source does not treat perception as a software-only function. It recommends dampeners, silicone grommets, foam mounting, and shock-absorbing mounts to reduce vibration transmitted from motors and propellers to cameras, sensors, and the AI core. The stated reasoning is that vibration can reduce video stability and create sensor error, which in turn can affect flight precision and recognition or streaming quality.

This creates a design tradeoff. Isolation may improve measurement quality but adds mass and may require precise placement. Excessive flexibility or an unsuitable mount could create another mechanical problem. The source does not specify the mount design, so the benefit remains a proposed outcome requiring test evidence.

## Onboard processing and analytics

The source proposes a Jetson Orin Nano with a custom Aquila AI Core for facial recognition and autonomous routing. It also proposes on-device video processing. These are not established software implementations. The source does not define the model, processing pipeline, latency, storage, update path, or how an automated result is presented to an operator.

Facial recognition is a particularly sensitive proposed capability. The repository preserves it as source content but does not treat it as a default or validated requirement. Any future study would require explicit authorization, lawful purpose, privacy controls, secure handling, human review, and evidence before a recognition result could be relied upon.

## Sensor fusion inputs

The source explicitly names a fusion combination of Lidar, optical flow, ultrasonic, infrared, and barometer data, while other sections also mention GPS and IMU fusion. The documentation retains both statements. It does not invent a fusion algorithm, weighting scheme, filter, confidence model, or failure policy.

The relationship to navigation is described in [sensor fusion](sensor-fusion.md) and [navigation and autonomy](navigation-and-autonomy.md). The source does not establish whether all sensor data is fused centrally, whether some sensors are fallback-only, or which measurements are authoritative during disagreement.

## Data handling and communications

The source proposes AES-256 encrypted transmission and on-device video processing. It also mentions RF interception and signal monitoring, fail-safe memory dump or self-wipe, and encrypted or fallback communications. These capabilities are proposed and require legal, privacy, security, and technical review. No implementation or authorization is established.

The design question is not only whether data can be processed onboard. It is also what data is stored, what is transmitted, how long it remains available, who can access it, how deletion is verified, and what happens when communications fail. The source raises these concerns but does not resolve them.

## Validation needs retained from the source

The source’s prototype-validation stages propose checking live HD feed, camera tracking, facial recognition, GPS or airspace precision, heat management, and sensor placement during controlled testing. No test results are supplied. Sensor performance therefore remains **requires validation** across lighting, weather, terrain, vibration, temperature, and communications conditions.

## Open questions

The source leaves unresolved the final sensor subset, exact camera and gimbal configuration, sensor mounting locations, calibration process, fusion authority, handling of disagreement, onboard-processing software, data retention, recognition thresholds, and the legal basis for sensitive sensing functions. These gaps remain visible rather than being completed with general UAV assumptions.
