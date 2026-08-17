from pathlib import Path

battery_wh = 648.0
nominal_v = 21.6
usable_fraction = 0.80
system_efficiency = 0.90
usable_wh = battery_wh * usable_fraction * system_efficiency

powers_w = [500, 750, 1000, 1250]
print('Battery gross energy (Wh):', battery_wh)
print('Usable-energy assumption:', usable_fraction)
print('System-efficiency assumption:', system_efficiency)
print('Estimated usable energy (Wh):', round(usable_wh, 2))
print('\nPower, endurance, nominal pack current')
for p in powers_w:
    hours = usable_wh / p
    current = p / nominal_v
    print(p, round(hours * 60, 1), round(current, 1))

for solar_w in [30, 60]:
    for p in [500, 750, 1000]:
        equivalent_minutes = solar_w / p * 60
        print('Solar equivalent minutes per hour at', solar_w, 'W and', p, 'W load:', round(equivalent_minutes, 2))

max_thrust_kg_each = 2.85
motor_count = 4
max_total_thrust_kg = max_thrust_kg_each * motor_count
print('\nTheoretical static maximum thrust basis (kgf):', max_total_thrust_kg)
for mass in [6, 8, 10]:
    print('Theoretical max thrust-to-weight at', mass, 'kg:', round(max_total_thrust_kg / mass, 2))

print('\nSource caveat: motor maximum thrust is not a hover or continuous operating point; actual thrust, current, propeller, voltage, temperature, and controller conditions must be measured or obtained from a complete test table.')

Path('/home/ubuntu/aquila_x_calculations.txt').write_text(
    'Calculation definitions:\n'
    'Usable energy = nominal battery energy × usable-energy fraction × electrical/propulsive system efficiency.\n'
    'Endurance (hours) = usable energy (Wh) ÷ average aircraft power (W).\n'
    'Average pack current (A) = average power (W) ÷ nominal battery voltage (V).\n'
    'Solar equivalent time (minutes per hour) = solar input (W) ÷ aircraft load (W) × 60.\n'
    'Theoretical static thrust-to-weight ratio = four × published maximum motor thrust ÷ assumed aircraft mass.\n'
    'All outputs are first-order estimates, not flight-test results.\n'
)
