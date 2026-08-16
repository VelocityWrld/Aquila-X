# Sensor Fusion

## Purpose

Sensor fusion combines complementary measurements into a more stable estimate of vehicle state, position, motion, and nearby obstacles. The preliminary Aquila-X concept references GPS, IMU, barometer, Lidar, optical flow, ultrasonic, IR, and camera inputs.

## Fusion Design Goals

The system should account for sensor latency, calibration, noise, vibration, environmental limitations, and temporary outages. It should publish confidence or validity indicators alongside estimates so that the flight controller and autonomy layer can apply appropriate safeguards.

## Conceptual Data Flow

```text
Raw sensors -> timestamping and calibration -> validity checks
           -> state and obstacle estimators -> flight/autonomy consumers
           -> logs and health monitoring
```

## Failure Handling

Examples of degraded conditions include GNSS loss, optical-flow failure in low texture, Lidar saturation, barometer disturbance, camera obstruction, vibration-induced IMU noise, and disagreement between independent estimates. The system should detect these conditions, reduce autonomy where appropriate, alert the operator, and follow a documented recovery policy.

## Verification

Fusion performance should be verified using recorded sensor datasets, hardware-in-the-loop testing, controlled environmental tests, and incremental flight tests. Metrics should include estimation error, latency, recovery time, false confidence, and behavior during conflicting measurements.
