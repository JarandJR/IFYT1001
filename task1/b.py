import numpy as np
import matplotlib.pyplot as plt
import math

print("4 b)")
print()

g = 9.81
y = 0.8
v0x = 100

t = math.sqrt((2*y)/g)

print(f"g = {g}m/s^2\nstarting height: y = {y}m\nstarting speed: vox = {v0x}s")
print(f"\nThe time the canonball uses before hitting the ground\n{round(t,2)} s")
