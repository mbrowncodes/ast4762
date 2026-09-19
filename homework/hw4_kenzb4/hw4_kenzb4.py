#!/usr/bin/env python
# coding: utf-8

# In[14]:


#Mackenzie Brown
#Homework 4 
#9/16/2026


# In[15]:


#imports
import numpy as np
import matplotlib.pyplot as plt


# In[17]:


print("Problem 2")

#2a draw random sample of N from gauss dist with given N, sigma, and mu
N = 10000 # number of observations
sigma = 13 # standard deviation
mu = 55 # mean
s = np.random.normal(mu, sigma, N) #draws samples from normal gaussian distribution


# In[18]:


#2b plot histogram of sample (bins 0-100), width 1, save png

plt.hist(s, bins = range(0,101)) #plot of given N, mu, and sigma values
# sets bin numbers 0-100 width of 1
plt.title("Gaussian Distribution Histogram")
plt.ylabel("N(x)")
plt.xlabel("x")
plt.savefig('hw4_kenzb4_graph1.png') #save as png

 


# In[19]:


#2c overplot gaussian distribution

bins = np.arange(0.5, 100, 1) # redefine bins so they approx in center of bin
gaus_eq = 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(-(bins - mu)**2 / (2 * sigma**2))
# gaussian function with my variables 
plt.hist(s, bins = range(0,101)) #regular plot 
plt.plot(bins, N * gaus_eq, color = 'r', linewidth = 3) # plot line, account for larger sample
# multiply function by large N
plt.title("Histogram of Gaussian")
plt.ylabel("N(x)")
plt.xlabel("x")
plt.savefig('hw4_kenzb4_graph2.png') #save another png for this graph


# In[ ]:





# In[ ]:




