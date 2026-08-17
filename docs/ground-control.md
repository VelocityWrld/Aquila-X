# Aquila-X Ground Control

## Status and purpose

**Status: Proposed operator interface.** The source lists a rugged ground-control tablet with mission-planner software. It does not define a completed application, hardware model, data protocol, or tested operator workflow.

The tablet is important because the source combines AI-assisted routing and perception with controlled test flights, trained operators, mission planning, and failsafe behavior. The ground station is therefore documented as the proposed human-facing boundary for authorizing, monitoring, reviewing, and interrupting system behavior.

## Source-described functions

The source explicitly mentions mission planning through a tablet and a rugged ground-control tablet in the component list. From those statements, the following functions are supported at concept level:

- Prepare or review a proposed mission route.
- Monitor vehicle status and the communications link.
- Observe live HD or thermal payload output where authorized.
- Review battery draw, flight time, temperature, and other logged data during validation.
- Provide operator commands or intervention when the system is operating under supervision.
- Support review of camera tracking, navigation, sensor behavior, and recovery events.

The source does not define screen layouts, command names, operator roles, warning thresholds, or whether the tablet can independently command a vehicle after a link interruption.

## Mission planning boundary

The source’s AI autopilot and autonomous-routing concepts are paired with tablet-based mission planning. The documentation preserves that relationship without claiming a particular level of autonomy. A mission plan may need to express route intent, constraints, recovery behavior, and payload authorization, but the source does not define a plan schema or validation process.

The ground-control system should not be presented as a replacement for the flight controller. The source separates the candidate flight controller from the Jetson Orin Nano-class onboard computer and tablet. The exact command authority among these layers remains unresolved.

## Monitoring and human oversight

The operator-facing system is expected to make relevant state visible during controlled operation. Source-relevant observations include flight stability, VTOL take-off and landing, autopilot or AI navigation, camera tracking, solar input versus battery draw, GPS or airspace precision, heat management, cooling efficiency, and communications behavior.

The source also notes that skilled operators or a long training phase may be required. This is a limitation of the proposed system, not evidence that training material or an operating procedure exists. The interface and procedures would need to distinguish normal operation, degraded sensing, communications loss, low battery, thermal concerns, and emergency landing states; the source does not define those states in detail.

## Logging and validation record

The source proposes recording flight time against battery use, GPS or airspace precision, signal-interception range, and heat-management performance. It also proposes continuous noise profiling and iterative refinement. The ground-control record would be the natural place to associate these observations with a vehicle configuration, payload, operator, weather condition, and software state, but the source does not prescribe a logging format.

No test results are present. The repository therefore describes logging as part of the planned validation path rather than claiming that a flight-data archive exists.

## Payload and sensitive data

HD, thermal, PTZ, facial-recognition, and on-device-processing concepts appear in the source. A ground station handling those outputs would require access control, purpose limitation, secure storage, and retention rules. The source does not define these controls, and the repository does not infer an implementation.

The ground station should not make sensitive automated outputs self-executing. Facial recognition is retained as a proposed source capability and requires authorization, human review, privacy controls, and evidence before operational reliance.

## Open questions

The source leaves unresolved the tablet hardware and software, operator roles, mission-plan format, command authorization, alerting behavior, link-loss interface, logging schema, payload-data access, update process, and emergency-intervention workflow. These are documentation gaps, not invitations to add generic ground-control features.


## Engineering operator-interface baseline

The ground station remains a proposed rugged tablet and mission-planner interface. Its minimum engineering boundary is to authorize missions, display vehicle and link state, expose degraded conditions, display payload data where authorized, and provide an operator intervention path. It must not be described as an autonomous authority independent of the flight controller.

The command relationship is provisionally represented as:

```text
Operator/tablet -> communications link -> vehicle command boundary -> flight controller
                                                    \-> companion-compute assistance
```

This is a documentation-level boundary, not an implementation diagram. The command protocol, authorization, timeout behavior, and interface between Pixhawk and Jetson remain unresolved.

## Minimum validation record

For every controlled test, the ground-control record should associate the observed result with the airframe configuration, battery identity, payload configuration, software state, operator, weather, and communications state. At minimum, the source-supported measurements include flight time versus battery use, GPS or navigation precision, thermal behavior, cooling efficiency, communications behavior, camera tracking, and sensor placement.

| Ground-control record | Why it matters | Status |
| --- | --- | --- |
| Vehicle configuration identifier | Prevents mixing results from different motors, batteries, payloads, or software. | Required record field; format unresolved. |
| Battery voltage/current/energy | Supports the endurance and reserve calculations. | Required measurement; telemetry source unresolved. |
| Flight mode and autonomy state | Distinguishes manual, assisted, and proposed AI behavior. | Required record; state taxonomy unresolved. |
| Link state and operator commands | Establishes command continuity and response to degradation. | Required record; protocol unresolved. |
| Sensor validity and warnings | Shows whether navigation/perception claims were made under valid inputs. | Required record; schema unresolved. |
| Payload data access events | Supports authorization and sensitive-data accountability. | Required for future sensitive payload operation; policy unresolved. |

The source proposes trained or skilled operators and controlled testing. That is retained as an operational prerequisite, not as evidence that a training program or standard operating procedure exists.
