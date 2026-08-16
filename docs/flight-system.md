# Flight System

## Concept

The flight system is a VTOL-capable control stack that coordinates lift, attitude, navigation assistance, propulsion outputs, and operator commands. The preliminary concept references a Pixhawk 6C or Cube Orange-class flight controller for prototype evaluation, subject to compatibility, supply, and certification review.

## Flight Functions

The proposed system supports controlled take-off and landing, hover, transition or forward-flight behavior where applicable, waypoint missions, return-to-home or safe recovery behavior, and manual or supervised-autonomy modes. Exact VTOL geometry and transition mechanics remain to be defined by the airframe design.

## Flight-Critical Inputs

The flight controller may use IMU data, barometric altitude, GNSS position, magnetometer data where appropriate, optical flow, range sensing, airspeed or other vehicle-specific measurements, battery state, motor telemetry, and operator commands. Sensor validity and disagreement must be monitored continuously.

## Flight Modes

| Mode | Purpose | Human oversight |
|---|---|---|
| Manual or assisted | Direct operator control with stabilization support | Continuous |
| Position hold | Maintain position using available navigation inputs | Continuous monitoring |
| Mission | Execute an approved route or task plan | Required, with override available |
| Return or recovery | Move toward a predefined safe recovery behavior after a trigger | Required where communications permit |
| Emergency landing | Reduce risk after a critical fault | Safety logic with operator awareness |

## Testing Roadmap

Testing should begin with bench checks, propulsion restraint tests, sensor calibration, tethered or controlled low-risk tests, and incremental flight envelopes. Test cards should define acceptance criteria, weather limits, abort conditions, battery reserves, observer roles, and data-recording requirements.

## Safety Note

Aquila-X is not represented as flight-ready or certified. Any real-world testing requires qualified personnel, a safe test site, applicable approvals, airspace coordination, maintenance controls, and a documented emergency plan.
