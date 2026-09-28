#!/usr/bin/env python
# coding: utf-8

# In[93]:


# Mackenzie Brown
# Practicum 3 
# 9/23/2026


# In[94]:


import linfit as L
import numpy as np
import matplotlib.pyplot as plt


# In[98]:


print("Problem 1")
#1a

# read in data from file
model_1 = np.loadtxt("practicum3_1.dat", skiprows = 2,   max_rows = 100)
# picks out data for model 1 (no header, until the end of values)
model_2 = np.loadtxt("practicum3_1.dat", skiprows = 105)
# picks out data for model 2 (none of model 1 and no headers)

#model 1 data 
x1 = model_1[:, 0] # all values in first column (x column)
y1 = model_1[:, 1] # all values in 2nd column (y column)
#model 2 data
x2 = model_2[:, 0] # x function squared 
y2 = model_2[:, 1] # y function squared 

#plot model 1 
plt.figure(figsize=(7,7))
plt.plot(x1, y1, ".", label="Model 1 Data", markersize = 14)
plt.title("Model 1", fontsize = 18)
plt.xlabel("x", fontsize = 15)
plt.ylabel("f(x)", fontsize = 15)
plt.legend()


# In[99]:


#1b
# make function to run print statements 
def fitted_values(v):
    """
    prints out the fitted variables 

    paramters:
    v : array that calls linfit function with error
    """
    print("Fitted Y-Intercept:", v[0])
    print("Fitted Slope:",       v[1])
    print("Uncertainty Y-Intercept:", v[2])
    print("Uncertainty Slope:",       v[3], "\n")


# errors
fit1 = L.linfit(y1, x1, 0.5) 
fit2 = L.linfit(y1, x1, 0.9) 
fit3 = L.linfit(y1, x1, 0.2) 

print("Sigma Y = 0.5")
fitted_values(fit1)
print("Sigma Y = 0.9")
fitted_values(fit2)
print("Sigma Y = 0.2")
fitted_values(fit3)


def plot_lin(x, y, fit, title, filename=None):
    """
    plotting for the linfit function 

    parameters:
    x :     x values of data
    y :     y values of data
    fit :   variable for L.linfit()
    title : title of graph

    returns:
    a plotted graph with a linear fit
    """
    plt.figure(figsize=(7,7))
    plt.plot(x, y, ".", label="Data", markersize = 14)
    plt.plot(x, fit[7], "-", label="Linear Fit", markersize = 18)
    plt.title(title, fontsize = 18)
    plt.xlabel("x",    fontsize = 15)
    plt.ylabel("f(x)", fontsize = 15)
    plt.legend()

    if filename is not None:
        plt.savefig(filename)
    

fit1_05 = plot_lin(x1, y1, fit1, "Model 1 Y Uncertainty 0.5") # plot uncertainity of 
#0.5 and fit it 





# In[100]:


#1c 

def find_chi (v):
    """
    print statment for L.linfit value

    parameter: 
    v: array that calls linfit function with error
    """
    print("Chi-Squared:", v[4])
    print("Probabilty of worse Chi-Squared:", v[5])


print("Sigma Y = 0.5")
find_chi(fit1)
print("Sigma Y = 0.9")
find_chi(fit2)
print("Sigma Y = 0.2")
find_chi(fit3)



fit1_05 = plot_lin(x1, y1, fit1, "Model 1 Y Uncertainty 0.5", 
                  "practicum3_kenzb4_graph_1c.png")



# In[107]:


#1d

fit_2 = L.linfit(y2, x2, 0.5)
fitted_values(fit_2)
find_chi(fit_2)

plot_lin(x2, y2, fit_2, "Model 2 Linear Fit", 
        "practicum3_kenzb4_graph_1d.png")


# In[105]:


print("Problem 2")
#1a
poisson_arr = np.random.poisson(10000, 396) #number instance, size 
uniform_arr = np.random.uniform(0, 10**6, 4) #low, high, size

combo_data = np.concatenate((poisson_arr,uniform_arr))

mean =   np.mean(combo_data)
median = np.median(combo_data)

print("Mean:",   mean) 
print("Median:", median)

sigma = np.std(combo_data)
print("Sigma:",  sigma)


# In[106]:


#1b

subsample = combo_data[np.abs(combo_data - median) < 5 * sigma]

print("Mean:",   np.mean(subsample)) 
print("Median:", np.median(subsample))
print("Sigma:",  np.std(subsample))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




