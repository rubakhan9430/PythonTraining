#Kinetic Energy
# KE = 1/2(mv^2)
import math
def kinetic_energy(mass,velocity):
    KE = 0.5 *(mass*(pow(velocity,2)))
    return KE
mass = float(input('Enter Mass:'))
velocity = float(input('Enter Velocity:'))
KE = kinetic_energy(mass,velocity)
print('Kinetic Energy:',KE)