############################################################################
# Python
# Date: 8/30/2024
# This program performs various scientific calculations.
############################################################################

import math

# Calulate Reynolds Number
# Re = [u * L] / v
velocity = 9
kinematic_viscosity = 0.0015
char_lin_dem = 0.875
reynolds_num = (velocity * char_lin_dem) / kinematic_viscosity
print(f'Reynolds number is {reynolds_num:.1f}')

# Calculate wavelength
# λ = [2 * d * sin θ] / n
distance = 0.028
degrees = 35
theta_radians = math.radians(degrees)
order = 1
wavelength = (2 * distance * math.sin(theta_radians)) / order
print(f'Wavelength is {wavelength} nm')

# Calculate production rate
# qt = qi / [1 + b * di * t] ^ (1/b)
repro_rate = 100
decline_rate = 2 
hyperbolic_const = 0.8
time = 10
production_rate = repro_rate / math.pow((1 + hyperbolic_const * decline_rate * time), (1/hyperbolic_const))
print(f'Production rate is {production_rate} barrels/day')

# Calculate change of velocity
# ∆v = ve * ln(mi / mf)
initial_mass = 11000
final_mass = 8300
exhaust_velocity = 2028
change_in_vel = exhaust_velocity * math.log(initial_mass / final_mass)
print(f'Change of velocity is {change_in_vel} m/s')
