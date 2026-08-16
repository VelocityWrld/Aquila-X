# Ground Control

## Concept

Aquila-X is proposed to use a rugged tablet running mission-planning and vehicle-monitoring software. The ground-control station is the operator-facing layer for mission preparation, authorization, telemetry review, payload management, alerts, logs, and emergency intervention.

## Core Functions

- Define and review mission plans.
- Configure geofences, altitude limits, speed limits, reserve-energy thresholds, and recovery behavior.
- Display vehicle state, link status, battery condition, navigation confidence, and health alerts.
- Provide manual override and controlled mission pause or abort functions.
- Review authorized payload data and export logs according to policy.
- Support maintenance checks, calibration records, and software-version tracking.

## Human Factors

The interface should make critical state visible, distinguish warnings from informational messages, reduce alarm fatigue, and require confirmation for high-impact actions. Operators should be trained on normal, degraded, and emergency procedures.

## Logging and Audit

Logs should include mission-plan version, operator identity, vehicle identity, software versions, command history, telemetry health, sensor alerts, link changes, battery state, and recovery events. Retention and access should follow the mission’s legal and privacy requirements.

## Security

Ground-control access should use strong authentication, role-based permissions, secure updates, encrypted storage, and device-management controls. Portable tablets should be protected against loss, unauthorized access, and accidental disclosure.
