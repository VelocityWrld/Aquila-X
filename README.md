# Aquila-X

> Aquila-X is a proposed AI-assisted VTOL unmanned aerial system concept focused on autonomous navigation, modular sensing, long-endurance operations, and vibration-aware flight control.

## Overview

Aquila-X is a design-stage concept organized around a VTOL airframe, brushless propulsion, electronic speed controllers, battery and possible solar augmentation, onboard AI processing, sensor fusion, HD and thermal PTZ imaging, communications, and a rugged ground-control tablet. The source material also records detailed reasoning about vibration isolation, acoustic reduction, failsafe behavior, data handling, and controlled validation.

The repository is a technical record, not a completed engineering dossier. Non-technical planning material is outside the scope of this public documentation.

## Current status

**Conceptual / design-stage.** The repository documents proposed architecture, candidate components, source-stated estimates, validation ideas, and unresolved design questions. It does not establish a completed prototype, flight-certified design, validated performance report, or flight-ready software.

Numerical values and capability statements retain their source status. A component named in the notes is not necessarily selected, procured, integrated, tested, or legally approved.

## System

At a high level, Aquila-X consists of a VTOL airframe; brushless motors, propellers, and ESCs; battery, BMS, charging, and possible solar systems; a candidate flight controller; a Jetson Orin Nano-class onboard computer; HD and thermal PTZ payloads; GPS, IMU, barometric, Lidar, optical-flow, ultrasonic, infrared, and temperature sensing in proposed combinations; communications links; and a ground-control interface.

The proposed architecture is coupled. Mass, propulsion, battery capacity, thermal management, vibration, acoustic output, sensor quality, camera stability, autonomy, and communications cannot be evaluated independently. The source does not establish a final configuration.

## Documentation

- [Overview](docs/overview.md)
- [System Architecture](docs/system-architecture.md)
- [Flight System](docs/flight-system.md)
- [Sensing and Perception](docs/sensing-and-perception.md)
- [Navigation and Autonomy](docs/navigation-and-autonomy.md)
- [Sensor Fusion](docs/sensor-fusion.md)
- [Power and Propulsion](docs/power-and-propulsion.md)
- [Communications](docs/communications.md)
- [Ground Control](docs/ground-control.md)
- [Noise and Vibration](docs/noise-and-vibration.md)

## Specifications

- [System Specification](specifications/system-specification.md)
- [Hardware Specification](specifications/hardware-specification.md)
- [Software Specification](specifications/software-specification.md)

## Research and evidence status

- [References and Evidence Status](research/references.md)

No new research direction or external literature review is included. The references document records source traceability, contradictions, evidence status, and what would require later validation.

## Archive

- [Technical source notes](archive/original-documents/Aquila-X-Complete-Notes.md)

The public archive copy preserves the source’s technical content. It is a curated technical record rather than an unchanged copy of the owner-supplied source.

## Project status

### What exists

The repository contains a structured technical record of the Aquila-X concept, expanded from the source notes into canonical documentation, preliminary specifications, a validation-oriented evidence record, and a curated technical archive copy.

### What does not yet exist

No physical prototype, certified airframe, validated flight-performance dataset, selected final bill of materials, verified supplier configuration, flight-ready software, completed autonomy implementation, validated acoustic result, or completed sensor-fusion implementation is established by the available material.

## Responsible development boundary

Any future implementation would require qualified engineering review, controlled testing, lawful authorization, privacy-preserving data handling, spectrum and aviation review, human oversight, and explicit treatment of sensitive capabilities such as facial recognition, RF monitoring, autonomous routing, self-wipe behavior, or emergency-landing AI.

## License

No open-source license has been selected. Until a license is added, the repository contents remain protected by applicable copyright law and should not be assumed to be freely reusable.
