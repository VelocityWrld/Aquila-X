# Power and Propulsion

## Propulsion Concept

The preliminary design uses brushless motors, electronic speed controllers, and low-noise propellers. Prototype materials reference approximately four to six VTOL motors and three to four mid-range ESCs, while the final-build concept references four high-performance ESCs with telemetry. The final motor count and geometry remain design decisions.

## Electronic Speed Controllers

An ESC receives commands from the flight controller and regulates motor power. Candidate feature requirements include telemetry, current and temperature monitoring, controlled acceleration, soft start and stop, braking behavior where appropriate, failsafe handling, and low-noise modulation. BLHeli_32, SimonK, T-Motor Alpha, and Hobbywing X-Rotor are examples mentioned in the source material, not confirmed selections.

## Battery and Power Management

The source concept references a 30 Ah Li-ion prototype battery and a 30–60 Ah smart-battery system with BMS and fast-charging circuitry for a later build. These values are preliminary and must be reconciled with cell chemistry, voltage, current demand, thermal limits, mass, enclosure, and aviation safety requirements.

## Solar Augmentation

Lightweight flexible solar sheets or integrated photovoltaic cells are proposed as an augmentation source. The source material mentions approximately 30–60 W support and a possible 10–20 minute endurance contribution. Actual benefit depends on area, illumination, orientation, conversion efficiency, power electronics, and mission profile; it must be measured rather than assumed.

## Propellers and Noise

Low-RPM, large-diameter propellers with optimized blade geometry may reduce acoustic output, subject to vehicle-size and thrust constraints. Composite or carbon-fiber materials, balanced assemblies, and careful motor alignment can reduce vibration. Tip-speed and aerodynamic noise should be measured during controlled testing.

## Energy Verification

The power budget should include hover, transition, cruise if applicable, payloads, onboard compute, communications, thermal management, reserve energy, and contingencies. Endurance claims should be based on repeatable tests with defined payload, weather, battery condition, and reserve criteria.
