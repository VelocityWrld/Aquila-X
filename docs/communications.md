# Aquila-X Communications

## Status and scope

**Status: Proposed communications architecture.** The source lists a long-range RF module, Wi-Fi, a 4G dongle, encrypted 5.8GHz communication, long-range RF, satellite fallback, and a rugged ground-control tablet. These are configuration options and proposed functions, not confirmed radio selections or an implemented network.

## Source-described communication paths

The prototype list describes interchangeable long-range RF, Wi-Fi, and 4G connectivity. The advanced onboard-systems list adds encrypted 5.8GHz, long-range RF, satellite fallback, and radio-interceptor language. The source does not define whether these links are simultaneous, which is primary, what the antenna arrangement is, or how link selection is controlled.

The proposed tablet is the human interface for mission planning and system monitoring. The communication architecture therefore has at least a conceptual vehicle-to-ground path, but the source does not specify a protocol, message format, command-authorization method, latency target, or link-budget assumption.

## Data categories

| Data category | Source relationship | Status |
| --- | --- | --- |
| Operator and mission commands | Ground-control tablet and mission planner are proposed. | Proposed; authorization and protocol unspecified. |
| Telemetry | ESC telemetry may include RPM, temperature, and power draw; flight and battery state are also relevant. | Proposed; complete telemetry schema unspecified. |
| Payload data | HD, thermal, PTZ, and sensor data may be processed onboard or transmitted. | Proposed; retention and access rules require definition. |
| Failsafe and recovery state | Multi-protocol redundancy and emergency landing are proposed. | Conceptual; triggers and link-loss behavior unspecified. |
| Monitoring or interception data | RF interception and signal monitoring are mentioned in the source. | Requires legal authorization and technical clarification; not an assumed capability. |

## Security and data handling

The source proposes encrypted transmission and on-device video processing. It also mentions AES-256 encrypted transmission, fail-safe memory dump or self-wipe, and satellite fallback. These items are recorded as proposed security or resilience concepts. The source does not establish key management, endpoint authentication, secure boot, update handling, access control, retention policy, or proof that deletion is complete.

On-device processing may reduce the amount of payload data sent over a link, but it does not by itself establish privacy or security. Sensitive sensing, including facial recognition, requires authorization, purpose limitation, controlled access, and human review. The repository does not add a legal or technical conclusion beyond this source-preserving boundary.

## Link resilience and failure behavior

The source’s multi-protocol redundancy and fallback language implies that communications loss is considered a system risk. It does not define which link is primary, how failover is triggered, how long a link may be absent, what happens to an active mission, or how an operator is notified.

A future implementation would need explicit behavior for link loss, degraded bandwidth, stale commands, conflicting commands from multiple links, and recovery after reconnection. These are unresolved questions. The current repository does not claim that redundancy or fallback has been implemented.

## Radio monitoring and interception language

The source includes “RF interception and signal monitoring” and “radio interceptor.” These terms are retained as source content but require careful status and authority boundaries. They do not establish authorization to collect, disrupt, decode, or access third-party communications. Any such function would require separate legal, spectrum, privacy, and security review. It is not treated as a default system requirement.

## Compliance boundary

The source proposes review of ITU frequency compliance and other regulatory requirements before regulated operation. The repository does not select frequencies, power levels, antenna configurations, encryption implementations, or cross-border operating assumptions. All communications choices remain subject to applicable aviation, spectrum, data-protection, and operational rules.

## Open questions

The source leaves unresolved the selected links, frequency plan, antenna design, encryption and key-management design, command authority, telemetry schema, failover policy, payload-data policy, and the exact meaning and authorization of monitoring or interception functions. These questions should remain visible rather than being completed with common communications practice.


## Communications engineering baseline

The source supports a modular communications study rather than a closed radio architecture. The candidates are long-range RF, Wi-Fi, interchangeable 4G, encrypted 5.8 GHz, and possible satellite fallback. The engineering baseline should define one primary command-and-control path, optional payload-data paths, and explicit behavior when each path is unavailable. No radio model, antenna, frequency, transmit power, or range is selected in this repository.

| Link function | Candidate source technology | Engineering data required before selection |
| --- | --- | --- |
| Flight-critical command and telemetry | Long-range RF | Frequency authorization, modulation, bandwidth, latency, range, antenna, power, link budget, and loss behavior. |
| Local configuration or short-range data | Wi-Fi | Operating mode, security, range, coexistence, and whether it is disabled in flight. |
| Wide-area backhaul | 4G dongle | Coverage, subscription-independent interface, power, antenna, latency, and loss behavior. |
| Payload stream | Encrypted 5.8 GHz or other data link | Data rate, encryption/key management, interference tolerance, and antenna placement. |
| Contingency path | Satellite fallback | Availability, latency, power, terminal mass, coverage, and operational authorization. |

Flight-critical commands should not be treated as equivalent to payload video. The system must eventually define command freshness, authentication, operator authorization, stale-command rejection, and a recovery state for loss of communications. The source proposes redundancy and emergency landing but does not provide a trigger table or implementation evidence.

## Verification requirements

A communications test record should report received-signal behavior, packet loss, latency, throughput, antenna orientation, aircraft attitude, range, terrain, and simultaneous payload load. Tests should separately evaluate command and telemetry continuity, payload streaming, link failover, reconnection, and stale-command rejection. The current project contains no such results; all range and resilience statements remain proposed.

The source’s RF-interception and signal-monitoring language is not promoted into a system requirement. It remains a source-described concept subject to explicit authorization, spectrum review, privacy controls, and a separate technical definition.
