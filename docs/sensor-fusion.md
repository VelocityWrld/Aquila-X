# Aquila-X Sensor Fusion

## Status

**Status: Proposed sensor-fusion concept.** The source explicitly mentions GPS plus IMU fusion and a broader combination of Lidar, optical flow, ultrasonic, infrared, and barometric inputs. It does not define a fusion algorithm, filter, confidence model, or validated estimator.

## Why fusion appears in the concept

The source places several sensors around the same problems: navigation, terrain mapping, obstacle avoidance, and flight precision. Combining measurements is proposed because each source may be affected by different conditions, while vibration can introduce error into cameras and inertial sensors. The source does not claim that fusion has already resolved those limitations.

## Source-described inputs

| Input | Source-described relevance | Unresolved detail |
| --- | --- | --- |
| GPS | Fused with IMU for navigation. | Accuracy, outage behavior, and authority during disagreement are unspecified. |
| IMU | Provides motion information and is paired with GPS. | Calibration, drift, vibration filtering, and mounting are unspecified. |
| Barometer | Included in the sensor-fusion list and used for altitude-related information. | Pressure disturbances and fusion weighting are unspecified. |
| Lidar | Used for obstacle avoidance, terrain mapping, and fusion. | Range, saturation behavior, and environmental limits are unspecified. |
| Optical flow | Included in the fusion concept and proposed for motion support. | Lighting, texture, and failure behavior are unspecified. |
| Ultrasonic | Included as a complementary ranging input. | Operating range and exact role are unspecified. |
| Infrared | Included as a complementary sensing input. | The source does not define whether it is thermal imaging, ranging, or another use in the fusion path. |
| Camera | Used for HD, thermal, PTZ, tracking, and recognition concepts. | The source does not define whether camera data contributes to state estimation. |

## Conceptual processing chain

A documentation-level interpretation of the source is:

```text
Raw sensors -> alignment and validity checks -> combined state or obstacle estimate
           -> flight and autonomy consumers -> operator visibility and logs
```

This diagram is a conceptual organization of the source, not a proposed implementation diagram. The source does not establish timestamping, synchronization, calibration order, estimator type, update rate, or data bus.

## Confidence and disagreement

The source does not explicitly define confidence values or a disagreement policy. It does, however, identify multiple independent measurements and proposes failsafe behavior and sensor fusion. The repository therefore marks confidence handling as an unresolved design requirement rather than claiming that it exists.

Important unresolved cases include GPS and IMU disagreement, Lidar and optical-flow disagreement, barometer disturbance, camera obstruction, vibration-induced IMU error, unavailable optical flow, and degraded or saturated range sensing. The source does not say which sensor becomes authoritative in any case. The system should not be described as robust to these conditions until such behavior is designed and tested.

## Relationship to autonomy and flight control

The fused estimate is conceptually relevant to the AI navigation, terrain-mapping, and obstacle-avoidance functions described in the source. It may also support the flight controller, but the source does not specify whether the flight controller receives raw data, a fused state, or both. The boundary between the onboard AI Core and the flight controller remains open.

Because the source proposes human-supervised mission planning and emergency behavior, any fusion failure should be visible to the operator or should cause a documented reduction in autonomy. That is a safety-oriented interpretation of the source’s stated failsafe concerns, not evidence of an implemented supervisor.

## Vibration and environmental effects

The source recommends dampeners and foam mounting because vibration can introduce sensor error. It also proposes testing in heat, wind, dust, and difficult terrain. These conditions may affect sensor quality, but the source gives no test measurements or calibration requirements.

The fusion design therefore depends on mechanical design, sensor placement, thermal management, weather exposure, and power stability. A sensor-fusion result cannot be treated as independent of those subsystems.

## Validation path

The source proposes controlled flights, data logging, GPS or airspace-precision review, heat-management review, and iterative sensor placement. A future technical record could compare estimated state against a known reference and record degraded-input behavior, but the source does not define that reference, metric, or test method. Current fusion status remains **requires validation**.

## Open questions

The source does not establish the estimator, calibration process, time synchronization, confidence representation, disagreement policy, sensor priority, data-retention format, or interface to the flight controller and autonomy layer. These questions remain unresolved.


## Engineering fusion responsibilities

The source supports a staged fusion responsibility model without specifying an implementation. Each sensor input should eventually carry at least a timestamp, validity state, and calibration identity before it is consumed by navigation or flight functions. This is an engineering requirement to be defined, not a claim that the current system implements it.

| Fusion responsibility | Required definition | Current status |
| --- | --- | --- |
| Time alignment | Sensor timestamps, clock source, allowable skew, and delayed-data handling. | Unresolved. |
| Calibration | Factory, installation, thermal, and in-field calibration records. | Unresolved. |
| Validity | Conditions under which GPS, IMU, barometer, range, flow, and camera data are accepted or rejected. | Unresolved. |
| Disagreement handling | Response to inconsistent position, altitude, motion, or obstacle measurements. | Unresolved. |
| Output authority | Whether the fused state feeds Pixhawk, Jetson, operator display, or more than one consumer. | Unresolved. |
| Degraded mode | Reduction in autonomy or recovery behavior when inputs are missing or invalid. | Proposed safety requirement; no implementation evidence. |

The Pixhawk 6C publishes integrated inertial and barometric sensor resources, while the source separately proposes external Lidar, optical-flow, ultrasonic, infrared, and GPS inputs [1]. This makes the controller a plausible home for flight-state estimation, but the repository does not infer firmware support, bus wiring, estimator configuration, or sensor priority from the hardware list alone.

## Verification evidence

Before the fusion concept can support an engineering performance claim, tests should record synchronized raw inputs, validity transitions, fused outputs, and the selected reference truth. At minimum, the evidence should cover static initialization, controlled motion, GPS outage, optical-flow degradation, range-sensor saturation, barometric disturbance, vibration exposure, thermal changes, and companion-computer loss. The source proposes controlled flight and data logging but does not supply results or acceptance thresholds.

## Reference

[1]: https://docs.holybro.com/autopilot/pixhawk-6c/technical-specification "Holybro Pixhawk 6C Technical Specification"
