# Lucas DeLoach
# AST4762C hw4
# 9-20-26
print("Question 1:")
print("Lucas DeLoach")
print("AST4762C hw4")
print("9-20-26")

import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import norm

print("\nQuestion 2:")

print("\nPart a")

rng    = np.random.default_rng()
N      = 10000
mu     = 55
sigma  = 13
sample = rng.normal(loc=mu, scale=sigma, size=N)
print(sample)

print("\nPart b")

bin_edges = np.arange(0, 101, 1)

plt.figure()
plt.hist(sample, bins=bin_edges)
plt.title("Histogram of a Gaussian of width 13 and mean 55")
plt.xlabel("x")
plt.ylabel("N(x)")

histogram_filename = "hw4_Lucas_DeLoach_problem2_partb_graph1.png"
plt.savefig(histogram_filename, format='png')
print(f"Histogram successfully saved as {histogram_filename}")
plt.show()

print("\nPart c")

bin_centers = np.arange(0.5, 100, 1)
expected_counts = N * norm.pdf(bin_centers, loc=mu, scale=sigma)

plt.figure()
plt.hist(sample, bins=bin_edges, label='Histogram of Gaussian estimate')
plt.plot(
    bin_centers, 
    expected_counts, 
    color='tab:orange', 
    label='Analytic Gaussian'
)
plt.legend()
plt.title("Histogram of a Gaussian of width 13 and mean 55")
plt.xlabel("x")
plt.ylabel("N(x)")

plot_filename = "hw4_Lucas_DeLoach_problem2_partc_graph1.png"
plt.savefig(plot_filename, format='png', bbox_inches='tight')

print(f"Plot successfully saved as {plot_filename}")
plt.show()

print("\nQuestion 3 (Extra credit):")

print("\nPart a")

print("Answer saved as hw4_Lucas_DeLoach_problem3_parta_pdf1.pdf")

print("\nPart b")

print("Answer saved as hw4_Lucas_DeLoach_problem3_partb_pdf1.pdf")
