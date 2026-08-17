# Aquila-X Navigation and Autonomy

## Status and intended role

**Status: Proposed AI-assisted navigation concept.** The source proposes an AI autopilot with terrain mapping, GPS and IMU fusion, Lidar obstacle avoidance, and mission planning through a tablet. It does not establish an implemented autonomy stack, a validated route planner, or unsupervised operation.

The source also names autonomous routing as a function of the proposed Aquila AI Core. The documentation keeps that function separate from the flight controller because the source separately names both systems. The exact boundary and command path are not defined.

## Navigation inputs

The source discusses GPS, IMU, barometer, Lidar, optical flow, ultrasonic, and infrared sensing. GPS and IMU fusion are specifically named for navigation, while Lidar is specifically named for obstacle avoidance and terrain mapping. The other sensors appear in the broader sensor-fusion concept. The available material does not establish whether all inputs are continuously available or how the system behaves when one becomes unreliable.

The source does not provide an algorithm, state-estimation method, confidence calculation, map representation, coordinate convention, or latency requirement. These are unknown rather than details to be inferred from common practice.

## Terrain mapping and obstacle avoidance

Terrain mapping and Lidar-based obstacle avoidance are proposed capabilities. Their rationale is to support routing and reduce collision risk in environments where the aircraft cannot rely on a clear path. The source does not give Lidar range, field of view, update rate, terrain classification method, false-alarm rate, missed-detection rate, or minimum safe separation.

The source also proposes AI path planning that avoids noise-reflective environments such as narrow urban corridors. This is presented in the noise-reduction discussion, so the route planner would potentially need to consider both navigational safety and acoustic output. The source does not specify how those objectives would be prioritized when they conflict.

## Mission planning and operator control

The source names a rugged ground-control tablet with mission-planner software. The tablet is therefore treated as a proposed interface for defining or reviewing missions and monitoring the aircraft. The source does not define the tablet software, link protocol, plan format, authorization mechanism, or operator interface.

The documentation preserves a supervised interpretation: a mission would require human authorization, the operator would need visibility into vehicle state and communications, and the operator would need an intervention or recovery path. This is consistent with the source’s separate emphasis on mission planning, failsafes, emergency landing, and trained operators, but the exact human-machine boundary remains unresolved.

## Autonomy boundaries

The source uses strong terms such as “AI autopilot,” “autonomous routing,” and “emergency landing AI,” but does not establish whether these are implemented or validated. They must therefore remain **proposed** or **conceptual**. The source does not authorize the autonomy layer to override operator constraints, flight limits, privacy restrictions, airspace requirements, or emergency procedures.

The source’s proposed “Stealth Mode” would reduce power draw, speed, and altitude and avoid fast climbs or descents. It should be treated as a constrained flight-mode idea, not as permission to reduce safety margins. How the mode is enabled, bounded, overridden, or disabled is not defined.

## Degraded navigation and recovery

The source proposes multi-protocol redundancy and emergency landing AI, but does not specify which faults trigger recovery or how recovery is performed. Loss of GPS, disagreement between GPS and IMU, Lidar failure, degraded camera input, link loss, low battery, compute failure, and adverse weather are all relevant failure questions, but no source-defined decision table exists.

The later validation material proposes testing GPS or airspace precision, live navigation, and controlled flights in heat, wind, and dust. These tests would provide evidence only if performed and documented. The current repository contains no results.

## Unresolved questions

The source does not establish the autonomy architecture, route-planning algorithm, map source, sensor confidence method, obstacle-avoidance policy, operator override behavior, recovery trigger, or test acceptance criteria. It also does not establish whether the proposed navigation functions are intended for a particular airframe geometry or payload mass. These remain open design questions.
