# System Specification

## Status

This is a preliminary, non-certified system specification derived from the Aquila-X concept material. Values are design targets or discussion estimates until verified by engineering analysis and testing.

## Mission and Operating Concept

Aquila-X is intended as a modular VTOL unmanned aircraft for authorized observation, mapping, inspection, environmental measurement, and related remote-sensing tasks. The operating concept assumes a trained human operator, approved mission plan, defined recovery behavior, and compliance with applicable aviation and privacy requirements.

## Preliminary Requirements

| ID | Requirement area | Preliminary statement | Verification |
|---|---|---|---|
| SYS-001 | Air vehicle | Support VTOL operation and controlled recovery | Flight test and inspection |
| SYS-002 | Navigation | Provide position, attitude, altitude, and health estimates with validity state | Hardware-in-loop and flight test |
| SYS-003 | Perception | Support modular imaging and obstacle-awareness sensors | Bench and environmental test |
| SYS-004 | Control | Provide operator-supervised manual, assisted, mission, and recovery modes | Functional and flight test |
| SYS-005 | Power | Monitor battery, propulsion, thermal, and reserve-energy state | Bench and endurance test |
| SYS-006 | Communications | Authenticate command and telemetry links and define loss-of-link behavior | Security and link test |
| SYS-007 | Ground control | Provide mission planning, monitoring, logs, and intervention | Usability and integration test |
| SYS-008 | Safety | Prevent unsafe autonomy actions through bounded control and failsafe logic | Safety analysis and fault injection |

## Performance Estimates

The source material mentions a possible 120–200 minute flight-time range, solar augmentation of approximately 10–20 minutes, and smart charging to approximately 60% in 20–30 minutes. These are unverified estimates and must not be presented as achieved performance.
