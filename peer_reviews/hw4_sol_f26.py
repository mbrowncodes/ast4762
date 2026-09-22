#! /usr/bin/env python3

# UCF AST5765/4762
# Original version: HW4 Solutions Joseph Harrington <jh@physics.ucf.edu>

import numpy as np
import matplotlib.pyplot as plt
import subprocess

plt.ion()

print("Solutions")
print("AST 4762/5765")
print("HW 4")

# === Problem 1 ===

print("=== Problem 2a ===")

Num   = 10000
sigma =    13.
cx    =    55.

gsamp = np.random.normal(cx, sigma, Num)

# === Problem 2 ===

print("=== Problem 2b ===")

nbin = 100
dbin =   1.
fbin =   0.
lbin = 100.

plt.figure(1)
bins = np.arange(fbin, lbin+dbin, dbin)
# The plt.hist() function returns the histogram data as well as
# plotting it.  Use a dummy variable to hold the result, or else it
# prints on the screen.  Traditionally such variables are called
# things like "dummy".
dummy = plt.hist(gsamp, bins=bins)
plt.xlabel('x')
plt.ylabel('N(x)')
plt.title('Histogram of a Gaussian')
#plt.savefig('hw5_sol_prob1_graph1.png')
plt.show()


print("=== Problem 2c ===")

x = bins[:bins.size] + dbin/2
y = Num * 1./np.sqrt(2.*np.pi*sigma**2) * np.exp(-0.5 * ((x-cx)/sigma)**2 )
plt.plot(x, y, 'o-', linewidth=4)
#plt.savefig('hw4_sol_prob1_graph2.png')
plt.show()



print("=== Problem 3 ===")
print("See comments in log.")

# === Problem 3 solutions: ===

# We have the Gaussian probability distribution:
#   p_G(x | mu, sigma) = 1/sqrt(2 pi sigma**2) * exp(- 1/2 * ((x-mu)/sigma)**2)

# We need to find Gamma, such that
#   p_G(mu + Gamma/2 | mu, sigma) = 1/2 * p_G(mu | mu, sigma)

# so,
#  1/(     sigma*np.sqrt(2.*np.pi)) * np.exp(-1/2. * ((mu+Gamma/2.-mu)/sigma)**2)
#= 1/(2. * sigma*np.sqrt(2.*np.pi)) * np.exp(-1/2. * ((mu         -mu)/sigma)**2)

# so
#  exp(- 1/2. * ((Gamma/2.)/sigma)**2) = 1/2.

# and
#   Gamma**2 = 4. * 2. * ln(2.) * sigma**2

# finally
#   Gamma = sqrt(8.*ln(2)) * sigma
#         = 2.3548         * sigma

# (Note that the book didn't round the result accurately.)
# Also, this is another example of good coding style.  The expression:

#  1/(     sigma*np.sqrt(2.*np.pi)) * np.exp(-1/2. * ((mu+Gamma/2.-mu)/sigma)**2)
#= 1/(2. * sigma*np.sqrt(2.*np.pi)) * np.exp(-1/2. * ((mu         -mu)/sigma)**2)

# makes clear that there are two similarities between the first and
# second lines, so some cancellation will be possible.  If we had
# written the lines

#  1/(sigma * np.sqrt(2.* np.pi)) * np.exp(- 1/2. * ((mu+Gamma/2.-mu)/sigma)**2)
#  = 1/(2. * sigma * np.sqrt(2.* np.pi)) * np.exp(- 1/2. * ((mu-mu)/sigma)**2)

# this is much less clear.  When you are writing code, this kind of
# alignment can make a big difference in verifying that successive lines
# do not have typos.  It also makes it much easier, a few years in the
# future when you want to use the code for something new, for you to
# understand what you were doing previously.

# === Problems 3b ===

# Lines on log-log plots indicate power laws, y = b * x**m.

# on a log-log plot,
# x = log(x')
# y = log(y')

# y = m*x + b
# log(y') = m * log(x')    + b
# log(y') =     log(x'**m) + b
# y' = x'**m * exp(b)
# exp(b) is a constant, so
# y' = b' * x'**m
# where b' > 0

