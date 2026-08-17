# System Architecture

## Architectural View

Aquila-X is organized as a layered cyber-physical system. The air vehicle provides structure, propulsion, power, flight control, sensing, onboard computing, and communications. A ground-control station provides mission planning, monitoring, operator commands, logging, and maintenance workflows.

```text
Mission and operator layer
        |
Ground-control station <---- communications links ----> Air vehicle
        |                                                   |
Mission planning                                      Flight controller
        |                                                   |
Data review and logs                         ESCs -> motors -> airframe
                                                            |
                                               Sensors -> onboard AI
                                                            |
                                                   Power and thermal systems
```

## Core Subsystems

| Subsystem | Function | Primary dependencies |
|---|---|---|
| Airframe | Supports propulsion, payloads, electronics, and landing loads | Structural design, mass budget, vibration analysis |
| Flight system | Stabilizes and commands the aircraft | Flight controller, IMU, barometer, motor-control outputs |
| Perception | Produces observations of position, obstacles, and mission scenes | Cameras, Lidar, optical flow, ultrasonic, IR, GPS |
| Autonomy support | Assists routing, obstacle avoidance, and mission execution | Sensor fusion, onboard compute, operator constraints |
| Power and propulsion | Converts stored energy into controlled lift and thrust | Battery, BMS, ESCs, motors, propellers, cooling |
| Communications | Exchanges telemetry, commands, and authorized payload data | RF, Wi-Fi, cellular, encryption, spectrum compliance |
| Ground control | Provides human supervision and mission management | Tablet, mission software, link management, logs |

## Interface Principles

Interfaces should be documented with message formats, timing expectations, failure responses, authentication requirements, and test procedures. The flight-critical control path should remain deterministic and should not depend on an unvalidated AI decision. AI functions should be bounded by safety rules, operator authority, geofencing, and failsafe logic.

## Safety Boundaries

A mature implementation would require independent review of flight termination and emergency landing behavior, loss-of-link handling, battery protection, thermal limits, sensor disagreement, software update security, and data retention. The current document defines a conceptual decomposition rather than a certified architecture.
