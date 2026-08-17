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


## Provisional real-data reference hardware

The following table establishes a study configuration so that the hardware discussion can use real published values without pretending that the configuration is final.

| Item | Provisional candidate | Published data relevant to Aquila-X | Remaining engineering question |
| --- | --- | --- | --- |
| Flight controller | Holybro Pixhawk 6C | STM32H743 FMU; ICM-42688-P and BMI088 inertial sensors; IST8310 magnetometer; MS5611 barometer; 16 PWM outputs; two CAN buses; 34.6 g plastic-case or 59.3 g aluminum-case mass; 84.8 × 44 × 12.4 mm; 6 V maximum input; −40 to 85 °C operating range [1]. | Power-module compatibility, mounting, vibration environment, firmware, sensor placement, and aircraft integration remain open. |
| Companion computer | NVIDIA Jetson Orin Nano Super Developer Kit | 67 INT8 TOPS; 8 GB LPDDR5; external NVMe/SD support; 7–25 W published power range [2]. | Airborne board selection, thermal path, storage retention, vibration isolation, software image, and failure behavior remain open. |
| Motor | T-Motor U5 KV400 | 6S and 14–16 inch propeller context; 2.85 kg published maximum thrust; manufacturer-described water/dust resistance and low-noise characteristics [3]. | Complete thrust/current/propeller table, continuous operating point, motor mass, mounting, and four-motor vehicle compatibility remain open. |
| Battery | ENEPAQ 6S 30 Ah Li-ion | 21.6 V nominal; 648 Wh; 3.43 kg; 206 × 124.3 × 70.5 mm; 50 A maximum charge current; 300 A continuous discharge value marked with an asterisk [4]. | BMS behavior, usable energy, discharge conditions, reserve, enclosure, thermal behavior, connector installation, and airframe fit remain open. |
| ESC | T-Motor Flame 60A 12S V2.0 study candidate | 6–12S LiPo; 60 A continuous; 80 A peak for 10 s; protections named for startup failure, signal loss, motor lock-up, and overload [5]. | The manufacturer page names U12 compatibility rather than U5 compatibility; matching to the U5/propeller load remains open. |

These published values are not a bill of materials. The battery’s 3.43 kg mass and the Jetson’s 7–25 W board power range are especially important to the mass and energy discussions, but neither closes the aircraft-level budget.

## Compatibility logic

The U5 page recommends 6S operation and 14–16 inch propellers, which makes a 6S battery a more coherent study point than combining the motor directly with a 14S-only design assumption [3]. The Flame ESC supports 6–12S, but its stated U12 compatibility means that motor/ESC compatibility must still be demonstrated rather than inferred from voltage alone [5]. The Hobbywing H110A is documented separately as a 14S-class candidate and is not part of the 6S reference pairing [6].

This compatibility distinction matters because electrical voltage range is only one constraint. Current demand, propeller loading, signal protocol, thermal dissipation, mounting, firmware behavior, telemetry, and failure response must also agree. The repository therefore treats the U5, battery, and ESC as a **compatibility study**, not as an approved propulsion package.

## Mass and energy implications

The ENEPAQ battery alone is published at 3.43 kg. A first-order energy estimate for the battery is:

```text
E_nominal = 21.6 V × 30 Ah = 648 Wh
```

For planning sensitivity only, applying 0.80 usable-energy fraction and 0.90 combined system-efficiency factor gives 466.6 Wh estimated usable energy. This estimate does not include the airframe, motors, ESCs, payload, wiring, landing gear, solar hardware, communications, or reserve policy. The detailed calculation and endurance sensitivity table are maintained in [`docs/power-and-propulsion.md`](../docs/power-and-propulsion.md).

## References

[1]: https://docs.holybro.com/autopilot/pixhawk-6c/technical-specification "Holybro Pixhawk 6C Technical Specification"
[2]: https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/nano-super-developer-kit/ "NVIDIA Jetson Orin Nano Super Developer Kit"
[3]: https://store.tmotor.com/product/u-power-u5.html "T-Motor U5 Power U-Type KV400"
[4]: https://enepaq.com/wp-content/uploads/2025/02/Li-ion-30000-mAh-6S10P-21.6v-Battery-Pack-ENEPAQ-Unmanned-Aerial-Vehicle-UAV-Drones-Unmanned-Ground-Vehicles-UGV-Robots-AGV-and-AMR-battery-pack-Datasheet-1.pdf "ENEPAQ 6S 30 Ah Li-ion pack datasheet"
[5]: https://store.tmotor.com/product/flame-60a-12s-V2-esc.html "T-Motor Flame 60A 12S V2.0 ESC"
[6]: https://www.hobbywing.com/en/products/xrotor-pro-h110a-14s-bldc "Hobbywing XRotor Pro H110A 14S ESC"
