print("Problem 1")


# lebronjames
# Homework 2
# September 9, 2026


print("Problem 2")

import numpy as np

#a1
x = np.arange(0,1001)
print("Number of elements: ", x.size)

#a2
print("Array data type: ", x.dtype)
print("Minimum: ", x.min(), "Maximum: ", x.max())

#b1
x = x*(2*np.pi / 1000)
print("\nNew Minimum: ", x.min(), "New Maximum: ", x.max())

#C
y = np.sin(x)

#D
print("The value of element 234 is: ", y[234])

print("\nProblem 3")
import matplotlib.pyplot as grph
#using grph to save time, creating the figure below

grph.figure()

grph.plot(x, y)

grph.xlabel("x (Rad)")
grph.ylabel("sin(x)")
grph.title("Sine of X from 0 to 2pi")

#Apparently you can add a grid which is cool
grph.grid(True)

grph.savefig("Sine_Graph.png")
grph.close()

#4
print("\nProblem 4")
#a1 101 evenly spaced values
r = np.linspace(-1, 1, 101)
print("r: size = ", r.size, "Minimum =", r.min(), "Maximum= ", r.max())

#a2 clip
rclip = np.clip(r, -0.5, 0.5)

#b1 plotting both

grph.figure()
grph.plot(r, label="Original")
grph.plot(rclip, label="Clipped")
grph.xlabel("Index")
grph.ylabel("Value")
grph.title("Original vs Clipped")
grph.legend()
grph.grid(True)

#b2
grph.savefig("original_clipped_graph.pdf")
grph.close()

#5
print("\nProblem 5")
print(''''
1: Astroquery  https://astroquery.readthedocs.io/
Astroquery provides acces tto astronomical data archives. It acts as a client to SIMBAD, VizieR, NED, SDSS, and many other. It permits you to search catalogs, download FITS files, and retrieve data about objects and observations.
2: Lightkurve  https://docs.lightkurve.org/
Lightkurve is a Python package designed for analyzing time series photometry from telescopes such as Kepler, K2, and TESS. It simplifies light curves, removing outlighers and normalizing flux data, while searching for transits or variability. It also contains plotting and periodogram tools, and is very useful when it comes to exploring exoplanet signals or stellar pulsations.
''')
