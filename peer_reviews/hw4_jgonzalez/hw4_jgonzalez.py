#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Jaedon Gonzalez
# Homework 4
# 9/20/2026


# In[41]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


# In[9]:


print("Problem 2")

# Draws N = 10,000 random samples from a Gaussian distribution of width (sigma) = 13 and mean (mu) = 55.
dist = np.random.normal(55, 13, 10000)


# In[51]:


# Plots a histogram of dist from 0 to 100 with step size of 1.
plt.xlabel("x")
plt.ylabel("N(x)")
plt.title("Histogram of a Gaussian")
plt.hist(dist, bins=np.arange(0,100,1))
plt.savefig("hw4_jgonzalez_problem2_graph1.png")


# In[148]:


x = np.arange(0.5, 100.5, 1)         # Creates an array from 0.5 to 100.5 with step size 1.
pdf = norm.pdf(x, 55, 13)*10000      # Upscales the amplitude of a Gaussian Distribution to fit the Histogram's height.

# Plots a Gaussian Distribution on top of a Histogram.
plt.hist(dist, bins=np.arange(0,100,1))
plt.xlabel("x")
plt.ylabel("N(x)")
plt.title("Histogram of a Gaussian")
plt.plot(x, pdf)
plt.savefig("hw4_jgonzalez_problem2_graph2.png")

