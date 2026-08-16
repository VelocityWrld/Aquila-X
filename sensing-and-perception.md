# Sensing and Perception

## Purpose

The perception subsystem provides measurements for navigation support, obstacle awareness, vehicle state estimation, and authorized mission payloads. The preliminary concept includes HD imaging, thermal imaging, GPS, IMU, barometer, Lidar, optical flow, ultrasonic, infrared, temperature sensing, and optional airframe-specific sensors.

## Proposed Sensor Groups

| Group | Candidate elements | Intended role |
|---|---|---|
| Vehicle state | IMU, barometer, temperature sensors | Attitude, acceleration, altitude, and health estimation |
| Position | GNSS/GPS, optical flow | Position reference and motion support |
| Range and obstacles | Lidar, ultrasonic, optical flow | Clearance and obstacle-awareness support |
| Mission payload | HD camera, thermal camera, PTZ gimbal | Authorized observation, inspection, and mapping |
| Health monitoring | Battery, ESC, motor, thermal telemetry | Fault detection and maintenance data |

## Data Handling

Payload data should be processed and retained according to the mission authorization, applicable privacy rules, and an explicit retention policy. On-device processing may reduce unnecessary transmission, but it does not remove the need for access control, audit logs, encryption, and lawful use.

## Recognition and Analytics

The source concept mentions facial-recognition capability. Any such feature is high-risk and should not be treated as a default requirement. If studied, it requires a documented legal basis, strict purpose limitation, bias and accuracy evaluation, human review, secure storage, and a prohibition on consequential action based solely on an automated result.

## Validation

Each sensor should be characterized for range, accuracy, latency, environmental sensitivity, calibration drift, interference, and failure behavior. Perception performance should be evaluated across lighting, weather, terrain, vibration, and representative mission conditions without exposing uninvolved people to unsafe or unauthorized testing.
