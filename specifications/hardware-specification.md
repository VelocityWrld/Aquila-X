# Aquila-X Hardware Specification

## Status

**Status: Preliminary candidate hardware specification.** The source supplies prototype and advanced-design material lists. This document is not a final component list, compatibility result, or validated hardware configuration.

## Structure and airframe

The prototype discussion names a lightweight carbon-fiber-reinforced polymer frame with some 3D-printed ABS parts. The advanced configuration names aerospace-grade CFRP or a titanium-aluminum alloy with thermal and UV protection. The source does not establish which material, geometry, mass, center of gravity, or structural load case is current.

The source also mentions VTOL capability, high-wind tolerance, IP65-plus weather resistance, heat-management vents, cooling fins, tough terrain, and remote operations. These are proposed design goals or configuration claims. Structural analysis, weather-sealing tests, thermal tests, and wind tests are not present.

## Propulsion hardware

The prototype list names approximately four to six brushless DC motors and three to four mid-range ESCs. The advanced list names high-thrust brushless motors in a 3000–5000KV range and four high-performance ESCs with real-time telemetry. The source separately proposes low-KV motors for quiet operation. Motor count, motor model, KV, voltage, propeller pairing, and final ESC architecture remain unresolved.

The source’s ESC reasoning includes controlled acceleration, braking, failsafe behavior, soft-start and soft-stop, low-noise modulation, and telemetry for RPM, temperature, and power draw. BLHeli_32, SimonK, T-Motor Alpha, and Hobbywing X-Rotor are named examples, not selected components.

## Battery and solar hardware

The prototype list names a 30Ah Li-ion battery pack. The advanced list names a 30–60Ah smart battery system with BMS and fast-charging circuitry. Lightweight flexible solar sheets are proposed for one configuration, while integrated photovoltaic cells with a charge controller and 30–60W support are proposed for another.

The source states possible 10–20 minute solar augmentation and smart charging to 60% in 20–30 minutes. These are unvalidated source estimates. Cell arrangement, voltage, current, mass, charge limits, thermal protection, charger design, solar area, and reserve policy are not established.

## Flight-control and computing hardware

Pixhawk 6C or Cube Orange is named as a candidate flight controller. Jetson Orin Nano is named for onboard AI processing, with a custom Aquila AI Core proposed for facial recognition and autonomous routing. The source does not establish the software image, compute load, storage, thermal solution, interface, or failure behavior.

The architecture therefore preserves a candidate separation between flight control and higher-level computation. This is a documentation inference based on the source listing separate components, not an implemented interface.

## Payload and sensing hardware

The source proposes an HD 1080p camera with a pan-tilt-zoom gimbal for a prototype and a dual HD/thermal PTZ camera system for an advanced configuration. It also lists GPS, IMU, barometer, basic Lidar, temperature sensors, optical flow, ultrasonic, and infrared sensing.

The source does not establish simultaneous installation, sensor placement, calibration, gimbal stabilization, thermal camera performance, Lidar range, or payload mass. Facial recognition and night-vision language remains a proposed processing or payload capability requiring authorization and validation.

## Propellers and vibration hardware

Carbon-nylon or composite low-noise propellers are proposed. The source recommends large-diameter, low-RPM, optimized blade geometry, carbon or composite materials, and a tip speed below 0.7 Mach as an acoustic target. No propeller diameter, pitch, blade count, or thrust data is supplied.

Rubber dampeners, silicone grommets, foam mounting, shock-absorbing motor mounts, and shock-absorbing landing gear are proposed to reduce vibration transmission. Their stiffness, placement, mass, resonance behavior, and effect on control are unresolved.

## Communications and ground hardware

The source lists long-range RF, Wi-Fi, interchangeable 4G connectivity, encrypted 5.8GHz, satellite fallback, and a rugged ground-control tablet. These are proposed options. The source does not establish radio models, antennas, frequency plan, power levels, link budget, encryption implementation, or tablet software.

## Hardware conflicts and unknowns

The final mass, center of gravity, thrust-to-weight ratio, motor voltage and current, propeller geometry, thermal limits, structural loads, environmental sealing, electromagnetic compatibility, battery configuration, solar contribution, and component availability remain unresolved. These should not be filled with generic UAV assumptions.
