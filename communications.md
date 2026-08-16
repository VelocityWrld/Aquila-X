# Communications

## Concept

The preliminary Aquila-X concept references long-range RF, Wi-Fi, cellular connectivity, encrypted links, satellite fallback, and a rugged ground-control tablet. These are architectural options rather than confirmed radio selections.

## Communication Functions

| Function | Purpose |
|---|---|
| Command and control | Carry authorized operator commands and safety status |
| Telemetry | Report vehicle state, battery, link quality, faults, and mission progress |
| Payload data | Transfer approved imagery or sensor outputs according to mission policy |
| Maintenance | Support diagnostics, configuration review, and software updates |

## Security Requirements

Communications should use authenticated endpoints, encryption in transit, key rotation, least-privilege access, replay protection, secure configuration, and auditable logs. Sensitive payload data should be minimized and retained only for an approved purpose.

## Link Management

The system should monitor link quality, latency, packet loss, and failover state. Loss-of-link behavior must be explicit, tested, and consistent with the approved operating area and safety case. A communications failure should not cause uncontrolled behavior or bypass of flight limits.

## Spectrum and Legal Review

Radio equipment, frequencies, power levels, antenna configurations, encryption features, and cross-border operation require review under applicable spectrum and aviation rules. References in the source material to interception or monitoring should not be interpreted as authorization to collect, disrupt, or access third-party communications. Any spectrum-monitoring research must be lawful, scoped, and conducted by qualified personnel.
