import numpy as np
import matplotlib.pyplot as plt
import math

print("4 d)")

print("Equation 1: x = v0*cos(alfa)*t")
print("Equation 2: y = v0*sin(alfa)*t - 1/2*g*t^2")
print("This results in:")
print("cos(alfa) = x / v0*t")
print("sin(alfa) = (y + 1/2*g*t^2)/vo*t")
print("tan_alfa is the function made by inserting equation 1 & 2\ninto tan(alfa) = sin(alfa)/cos(alfa)")

#Method from tan(α) preperaed with sin α / cos α
def tan_alfa(x):
    return -0.1 + (0.367)/np.cos(x)**2

#X is from 0.2 - 1.3 to remove unnecessary noise
x = np.linspace(0.2,1.3,101)
tan_a = tan_alfa(x)
tan = np.tan(x)
#plots the two functions
plt.plot(x, tan_alfa(x))
plt.plot(x, np.tan(x))

#The intercept points
intercepts = np.argwhere(np.diff(np.sign(tan - tan_a))).flatten()
plt.plot(x[intercepts], tan_a[intercepts], 'ro')

plt.grid()
plt.show() 

print("intercept between tan(α) & tan_alfa(α)")
print("The intercepts are in radians. So to convert to degrees, we need to multiply the result with 360∘/2*π")
print(f"1: α = {round(x[intercepts][0], 1)} = {round(round(x[intercepts][0], 1)*((360)/(2*np.pi)))}∘\n2: α = {round(x[intercepts][1],3)} = {round(x[intercepts][1]*((360)/(2*np.pi)))}∘")