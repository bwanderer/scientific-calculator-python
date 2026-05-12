############################################################################
# Python
# Date: 9/4/2024
# This program will perform various scientific calculations.
############################################################################

import statistics
import math 

# Ohm's Law: V = IR
current = 5
resistance = 20
voltage = current * resistance
print(f'The voltage across a conductor with resistance {resistance} ohms and a current of {current} amps is {voltage} volts.')

# Kinetic Energy: (1/2) * m * v^2
mass = 100
velocity = 21
kinetic_energy = (1/2) * mass * (velocity**2)
print(f'The kinetic energy of an object with mass {mass} kg and velocity {velocity} m/s is {kinetic_energy} joule.')

# Standard Deviation: formula found in mathisfun.com
test_scores = [98, 56, 72, 85, 92, 45, 62, 77]
num = len(test_scores)

iteration = 0
mean = 0

for score in test_scores:
    mean += score
mean /= num

for score in test_scores:
    iteration += (score - mean)**2
standard_deviation = math.sqrt(iteration / num)
stdev_funct = statistics.stdev(test_scores)

print(f'Standard Deviation of test scores, using manual code, is {standard_deviation}')
print(f'Standard Deviation of test scores, using stdev function, is {stdev_funct}')

# Force: F = m * a
mass = 549054
gravity = 9.81
force = mass * gravity
print(f'The force required to move the Space X Falcon 9, with a mass of {mass} kg, \nto begin liftoff if earth gravity is {gravity} m/s^2, is {force} newtons.')
