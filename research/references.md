# Aquila-X Research and References

## Scope

This document is the canonical evidence register for the public Aquila-X engineering specification. It records the supplied technical source, manufacturer data used in the provisional reference configuration, and official aviation-regulatory context. It is not a supplier comparison, commercial assessment, certification dossier, or new research direction.

The repository distinguishes **source-stated proposal**, **manufacturer-published component data**, **derived first-order estimate**, and **verified test result**. The current repository contains no verified aircraft flight-test results.

## Primary project source

The primary technical source is [`archive/original-documents/Aquila-X-Complete-Notes.md`](../archive/original-documents/Aquila-X-Complete-Notes.md). It contains the original project concepts, configuration alternatives, technical rationale, proposed test activities, and unresolved questions. Non-technical planning content is excluded from the canonical public engineering documents.

## Manufacturer and component references

| Ref. | Source | Use in the specification |
| --- | --- | --- |
| [1] | [Holybro Pixhawk 6C Technical Specification](https://docs.holybro.com/autopilot/pixhawk-6c/technical-specification) | Controller processor, sensors, I/O, dimensions, mass, input voltage, and temperature data. |
| [2] | [NVIDIA Jetson Orin Nano Super Developer Kit](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/nano-super-developer-kit/) | Published compute, memory, storage, and board-power reference data. |
| [3] | [T-Motor U5 Power U-Type KV400](https://store.tmotor.com/product/u-power-u5.html) | Candidate motor, 6S/propeller context, and published maximum thrust reference. |
| [4] | [ENEPAQ 6S 30 Ah Li-ion battery datasheet](https://enepaq.com/wp-content/uploads/2025/02/Li-ion-30000-mAh-6S10P-21.6v-Battery-Pack-ENEPAQ-Unmanned-Aerial-Vehicle-UAV-Drones-Unmanned-Ground-Vehicles-UGV-Robots-AGV-and-AMR-battery-pack-Datasheet-1.pdf) | Nominal voltage, capacity, energy, mass, dimensions, charge, and discharge reference data. |
| [5] | [T-Motor Flame 60A 12S V2.0 ESC](https://store.tmotor.com/product/flame-60a-12s-V2-esc.html) | Candidate ESC voltage/current/protection data and compatibility limitation. |
| [6] | [Hobbywing XRotor Pro H110A 14S ESC](https://www.hobbywing.com/en/products/xrotor-pro-h110a-14s-bldc) | Separate 14S-class alternative; not part of the 6S reference pairing. |

The component pages support a **provisional compatibility study**, not a final bill of materials. In particular, the U5 maximum-thrust value is not a continuous hover point, and the Flame ESC page’s explicit U12 compatibility does not prove compatibility with the U5.

## Aviation and regulatory context

The source refers to the Nigeria Civil Aviation Authority as “NCAA” and to ICAO UAS frameworks. The following official references are retained for regulatory context only; their presence does not mean that Aquila-X has been approved, certified, registered, or authorized to operate.

| Ref. | Official source | Scope |
| --- | --- | --- |
| [7] | [Nigeria Civil Aviation Authority: Guidelines for the Operations of RPAS/UAV in Nigeria](https://ncaa.gov.ng/media/news/guidelines-for-the-operations-of-remotely-piloted-aircraft-systemsunmanned-aerial-vehicle-rpasuav-in-nigeria/) | Official NCAA guidance entry identified for Nigerian RPAS/UAV operations. |
| [8] | [NCAA RPAS Portal](https://rpas.ncaa.gov.ng/) | Official portal for Nigerian RPA/UAV registration and regulatory information. |
| [9] | [ICAO Model UAS Regulations](https://www.icao.int/UA/icao-model-uas-regulations) | ICAO model regulatory material for unmanned aircraft systems. |
| [10] | [ICAO Unmanned Aircraft Systems](https://www.icao.int/UA) | ICAO UAS regulatory and standards-development context. |

Regulatory applicability, operating approvals, spectrum permissions, privacy requirements, and data-protection obligations must be determined for the actual operating location and mission. No compliance conclusion is made here.

## Calculation evidence

The first-order power and propulsion calculations are implemented in [`aquila_x_calculations.py`](../aquila_x_calculations.py) and documented in [`docs/power-and-propulsion.md`](../docs/power-and-propulsion.md). The central relationships are:

```text
E_nominal = V_nominal × C_Ah
E_usable = E_nominal × usable-energy fraction × system efficiency
Endurance = E_usable ÷ average aircraft power
Pack current ≈ average aircraft power ÷ nominal battery voltage
Solar-equivalent time = solar input ÷ aircraft load × 60
Theoretical thrust-to-weight = summed published maximum thrust ÷ assumed aircraft mass
```

The 0.80 usable-energy fraction and 0.90 system-efficiency factor are explicitly provisional assumptions. The calculated endurance, current, solar contribution, and thrust ratios are **sensitivity estimates**, not flight-test data.

## Evidence status and unresolved terms

The presence of a component name or capability in the project source does not establish that it has been selected, procured, integrated, legally approved, or tested. There is currently no evidence for a completed airframe, validated 120–200 minute endurance, validated 10–20 minute solar contribution, validated noise reduction, validated obstacle avoidance, implemented facial recognition, implemented swarm compatibility, implemented satellite fallback, or implemented secure deletion.

The source retains quantitative statements such as 30 Ah, 30–60 Ah, 30–60 W solar support, 10–20 minutes, 120–200 minutes, 60% charging in 20–30 minutes, 0.7 Mach tip speed, and 3000–5000 KV motors. These remain source statements or proposed design targets until their configuration, conditions, measurements, and uncertainty are recorded.

The source also uses terms including “RF interception,” “radio interceptor,” “self-wipe,” “radar-absorbent coating,” “facial recognition,” and “swarm compatibility.” These remain proposed or conceptual terms requiring separate legal, privacy, security, and engineering review. They are not assumed implemented system capabilities.

## Citation and change discipline

Any future quantitative claim should identify the source, access or publication date where available, component revision, configuration, test conditions, measurement method, and uncertainty. Derived values must show the formula and assumptions. A manufacturer rating must not be presented as an aircraft-level performance result, and an unresolved question must not be silently filled with a generic UAV assumption.
