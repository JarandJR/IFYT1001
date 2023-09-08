import numpy as np
import matplotlib.pyplot as plt
import math

print("4 a)")

g = 9.81
y = 9
x = 1.75
#time used
t = math.sqrt((2*y)/g)
v0 = x/t
print()
print(f"g = {g}m/s^2\nstarting height: y = {y}m\nledge length: x = {x}m\ntime before the swimmer hits the water: t = {round(t,2)}s")
print(f"\nThe swimmer needs to have a minimum speed of:\n{v0} m/s\nto hit the water and not the ground")