#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Mackenzie Brown
# Homework 5 
# 9/27/2026


# In[24]:


import numpy as np
import matplotlib.pyplot as plt 


# In[33]:


print("Problem 2")
# practicum code pasted
poisson_arr = np.random.poisson(10000, 396)   #number instance, size 
uniform_arr = np.random.uniform(0, 10**6, 4)  #low, high, size
combo_data = np.concatenate((poisson_arr,uniform_arr))
# print(combo_data.size)  --> amount of elements 
mean =   np.mean(combo_data)     #finding mean
median = np.median(combo_data)   # median
print("Mean:",   mean) 
print("Median:", median)
sigma = np.std(combo_data)       #and sigma
print("Sigma:",  sigma, "\n")
subsample = combo_data[np.abs(combo_data - mean) < 5 * sigma] # create sub-sample
# print(subsample.size)   --> amount of elements 
print("Sub Sample Mean:",   np.mean(subsample)) 
print("Sub Sample Median:", np.median(subsample))
print("Sub Sample Sigma:",  np.std(subsample), "\n")




# hw 5, problem 2 contribution
sub2_sample = subsample[np.abs(subsample - np.mean(subsample)) < 5 * sigma]
# print(sub2_sample.size)  --> amount of elements 
print("Sub-Sub Sample Mean:",   np.mean(sub2_sample)) 
print("Sub-Sub Sample Median:", np.median(sub2_sample))
print("Sub-Sub Sample Sigma:",  np.std(sub2_sample))


# In[34]:


print("Problem 3")

# make routine: sigrej()
def sigrej(arr, rej, b_mask=None):
    """
    iterative sigma rejection on an array
    
    Parameters:
    -----------
    arr : numerical array type of data
    rej : numerical tuple form, number of standard deviations to use (rejection limit)

    Return:
    ---------
    mask : Boolean mask, telling true or false for array length of arr 

    Optional Parameters:
    --------------------
    b_mask : if provided, array given with True = good values and False = bad
    values, if None, array same legnth is given with all True values

    Examples:
    ---------
    ex 1: 
    >>>x = np.array([1., 2., 3., 150., 5.])
    >>>sigrej(x, (5.0, 5.0))
    [ True  True  True  True  True]

    ex2:
    >>>x = np.array([1., 2., 3., 150., 5.])
    >>>b_mask = np.array([True, True, False, True, True])
    >>>sigrej(x, (5.0, 5.0))
    [ True  True False  True  True]
    
    """
    num_it = len(rej) # tells amount of times to iterate over and sigma multipliers
  
    if b_mask is None:  
        mask = np.ones(arr.shape, dtype=bool)
        # make a boolean array, same shape as one given, but every value is True 
    else: 
        #print array with values that are bad equal to False, and good value 
        #equal to true
        if b_mask.shape != arr.shape:
            raise ValueError("b_mask must have the same shape as arr")
        mask = b_mask.copy()

    for i in range(num_it):
        # for every value in length of array, we will iterate over it 
        good_data = arr[mask]

        mean =   np.mean(good_data)
        sigma =  np.std(good_data)

        good = np.abs(arr - mean) < rej[i] * sigma  # values that are less than given sigma
        # value are kept under variable good 
        mask = np.logical_and(mask, good)  #
                    
    return mask 

    


# In[36]:


check = sigrej(combo_data, (5., 5.))
cleaned_data = combo_data[check]
print("Cleaned Data Mean:", np.mean(cleaned_data))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




