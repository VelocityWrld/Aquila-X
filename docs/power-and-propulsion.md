# Aquila-X Power and Propulsion

## Status

**Status: Proposed configuration set.** The source presents prototype and advanced-design component lists rather than one finalized propulsion and power system. The values below are retained as source statements, estimates, or candidates and are not validated performance specifications.

## Motor configurations

The prototype discussion references approximately four to six brushless DC motors for VTOL, with lower thrust than a later configuration. The advanced configuration references high-thrust brushless motors in a 3000–5000KV range. The source does not establish the final motor count, motor model, thrust requirement, propeller pairing, or airframe geometry.

The source also proposes low-KV brushless motors for quiet operation at lower speeds. This creates a configuration tension with the high-KV range stated for the advanced design. The documentation preserves both statements because the source does not establish whether they describe alternative configurations, a drafting inconsistency, or a final decision.

## ESC role and selection reasoning

An electronic speed controller regulates motor power in response to flight-controller commands. The source identifies braking, smooth acceleration, failsafe behavior, telemetry, low-noise modulation, and soft-start behavior as relevant features. Telemetry may include RPM, temperature, and power draw.

The source lists three to four mid-range ESCs in a prototype configuration and four high-performance ESCs with real-time telemetry in an advanced configuration. It names BLHeli_32 and SimonK as hobbyist examples and T-Motor Alpha and Hobbywing X-Rotor as advanced UAV examples. These are source-mentioned examples, not confirmed selections.

The design rationale is that precise ESC behavior can improve motor control, reduce abrupt energy spikes, and support quieter operation. Sinusoidal or field-oriented control is proposed to reduce switching noise and electromagnetic interference. Soft-start and soft-stop behavior are proposed to prevent sudden audible and electrical transients. Whether these behaviors are available in the selected hardware remains unresolved.

## Battery and battery management

The prototype materials list a 30Ah Li-ion battery pack. The advanced design lists a 30–60Ah smart battery system with a battery-management system and fast-charging circuit. The feature section separately states “30Ah+.” These values are retained as separate source statements; the repository does not select one capacity or claim that the figures are mutually compatible.

The source links battery management to endurance, fast charging, thermal behavior, and power availability for motors, computing, payloads, and communications. It states a possible smart fast-charging result of 60% in 20–30 minutes, but no charger, current, thermal limit, cell arrangement, or test result is provided. The fast-charging figure is therefore an unvalidated source estimate.

The required engineering questions include cell chemistry and configuration, voltage, peak current, discharge limits, BMS behavior, thermal protection, enclosure, mass, charging safety, and reserve policy. The source does not answer these questions.

## Solar augmentation

The source proposes lightweight flexible solar sheets for a prototype and integrated photovoltaic cells with a charge controller in an advanced configuration. It mentions low-wattage sheets, approximately 30–60W support, and a possible endurance contribution of roughly 10–20 minutes.

The source itself qualifies solar contribution as limited unless upgraded. The result depends on available area, illumination, orientation, conversion losses, charge-controller behavior, aircraft attitude, and mission demand. No measurement or energy model is present, so solar augmentation remains a proposed supplement rather than a primary energy source.

## Endurance claims and energy reasoning

The source states an estimated flight time of 120–200 minutes and separately discusses solar augmentation and battery capacity. These are source estimates, not validated endurance. They cannot be treated as a guaranteed operating range because the source does not provide mass, thrust, hover power, payload mass, weather, battery voltage, reserve, or test conditions.

A later validation path proposes comparing flight time with battery use and solar input. Until those measurements exist, the appropriate status is **requires validation**. The source does not establish whether the endurance estimate applies to the prototype, advanced configuration, a particular payload, or a particular flight mode.

## Propellers and acoustic tradeoffs

The source proposes carbon-nylon or composite low-noise propellers, low RPM, large diameter, optimized blade shapes, and a tip speed below 0.7 Mach to reduce high-frequency noise. These choices trade acoustic output against thrust, diameter clearance, mass, motor operating point, efficiency, and airframe packaging. The source does not provide propeller diameter, pitch, blade count, or test data.

Ducted fans are also proposed for safety and noise shielding, with an explicit warning that efficiency may decrease. This remains an alternative rather than a selected architecture.

## Power and propulsion integration questions

The final motor count, motor KV, ESC count, ESC control method, propeller geometry, battery capacity, BMS configuration, charging circuit, solar area, thermal path, and endurance reserve remain unresolved. The power subsystem must eventually be evaluated together with payload operation, Jetson compute load, communications, camera use, and vibration or acoustic controls. No implementation detail should be inferred from common UAV practice.


## First-order reference calculation

For a real-data reference point, this document uses the manufacturer-hosted ENEPAQ 6S 30 Ah Li-ion pack as a **candidate battery only**. Its published nominal voltage is 21.6 V and its published energy capacity is 648 Wh. The pack is listed at 3.43 kg. These are component-level manufacturer values, not Aquila-X flight results [1].

The basic nominal-energy relationship is:

```text
E_nominal = V_nominal × C_Ah
E_nominal = 21.6 V × 30 Ah = 648 Wh
```

The aircraft cannot normally use all nominal energy if it is to preserve reserve, protect the battery, and account for conversion and wiring losses. For an illustrative planning estimate only, define:

```text
E_usable = E_nominal × f_usable × η_system
```

Using an explicitly provisional usable-energy fraction of 0.80 and an explicitly provisional combined electrical/propulsive efficiency factor of 0.90:

```text
E_usable = 648 Wh × 0.80 × 0.90 = 466.6 Wh
```

The two factors above are **engineering assumptions for sensitivity analysis**, not manufacturer values and not validated Aquila-X values. They should be replaced by measured reserve policy, battery discharge data, power-conversion losses, and aircraft test data.

For a constant average aircraft power assumption, the first-order endurance estimate is:

```text
t_endurance[h] = E_usable[Wh] ÷ P_average[W]
```

| Assumed average aircraft power | First-order endurance using 466.6 Wh usable energy | Nominal pack current at 21.6 V |
| ---: | ---: | ---: |
| 500 W | 56.0 min | 23.1 A |
| 750 W | 37.3 min | 34.7 A |
| 1,000 W | 28.0 min | 46.3 A |
| 1,250 W | 22.4 min | 57.9 A |

These values are not endurance claims. They show why the source-stated 120–200 minute estimate cannot be accepted without a much lower demonstrated average power, a different energy store, a different aircraft mass and propulsion system, or a change in the operating definition. The calculation also excludes the detailed variation between hover, transition, climb, cruise, payload operation, compute load, communications, wind, battery temperature, and reserve.

The approximate pack current relationship is:

```text
I_pack[A] = P_average[W] ÷ V_nominal[V]
```

At 1,000 W, the nominal current is approximately 46.3 A before accounting for voltage sag, transient demand, conversion losses, and the distinction between average and peak current. The ENEPAQ datasheet publishes a 300 A continuous-discharge figure with an asterisk; that component rating must not be interpreted as an aircraft operating target [1].

## First-order propulsion margin check

The T-Motor U5 KV400 page publishes a maximum thrust of 2.85 kg and recommends 6S operation with 14–16 inch propellers [2]. If four identical motors were used, the arithmetic upper-bound sum would be:

```text
T_sum,published-max = 4 × 2.85 kgf = 11.4 kgf
```

A theoretical thrust-to-weight ratio at an assumed aircraft mass is then:

```text
T/W_theoretical = T_sum,published-max ÷ M_aircraft
```

| Assumed aircraft mass | Arithmetic ratio using 11.4 kgf published maximum sum |
| ---: | ---: |
| 6 kg | 1.90 |
| 8 kg | 1.43 |
| 10 kg | 1.14 |

This is not a design clearance. The motor maximum is not a hover point or necessarily a continuous operating point, and the page does not provide the complete propeller, current, voltage, temperature, or test-condition table needed to turn it into an aircraft thrust budget. The 3.43 kg battery alone consumes a substantial portion of any eventual mass budget [1] [2].

## First-order solar contribution check

For an assumed constant aircraft load, the energy-equivalent contribution of a solar input is:

```text
solar_equivalent_minutes_per_hour = P_solar ÷ P_aircraft × 60
```

At a 750 W aircraft load, 30 W of solar input is equivalent to approximately 2.4 minutes of aircraft energy per hour, while 60 W is equivalent to approximately 4.8 minutes per hour before accounting for orientation, shading, conversion losses, charge-controller behavior, temperature, and aircraft attitude. Therefore, the source’s proposed 30–60 W solar augmentation cannot by itself substantiate a 10–20 minute endurance increase without a defined duration, illumination profile, collection area, and measured net energy balance.

## Reference configuration status

The current data supports a **provisional compatibility study**, not a closed propulsion specification: candidate Pixhawk 6C flight controller; candidate Jetson Orin Nano Super developer kit; candidate four-motor U5 KV400, 6S, 14–16 inch propulsion arrangement; candidate 6S 30 Ah battery; and a candidate ESC that must still be matched to the motor and propeller load. The manufacturer describes the Flame 60A 12S V2.0 ESC as supporting 6–12S LiPo and 60 A continuous/80 A peak, but specifically names U12 motor compatibility, so it is not automatically a validated U5 pairing [3]. The H110A remains a separate 14S-class ESC alternative and should not be mixed into the 6S baseline without a new compatibility analysis [4].

### References

[1]: https://enepaq.com/wp-content/uploads/2025/02/Li-ion-30000-mAh-6S10P-21.6v-Battery-Pack-ENEPAQ-Unmanned-Aerial-Vehicle-UAV-Drones-Unmanned-Ground-Vehicles-UGV-Robots-AGV-and-AMR-battery-pack-Datasheet-1.pdf "ENEPAQ 6S 30 Ah Li-ion pack datasheet"
[2]: https://store.tmotor.com/product/u-power-u5.html "T-Motor U5 Power U-Type KV400 motor"
[3]: https://store.tmotor.com/product/flame-60a-12s-V2-esc.html "T-Motor Flame 60A 12S V2.0 ESC"
[4]: https://www.hobbywing.com/en/products/xrotor-pro-h110a-14s-bldc "Hobbywing XRotor Pro H110A 14S ESC"
