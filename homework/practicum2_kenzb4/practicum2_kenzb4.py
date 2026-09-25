#!/usr/bin/env python
# coding: utf-8

# In[48]:


# Mackenzie Brown
# Practicum 2 
# 9/21/2026


# In[49]:


import numpy as np
import matplotlib.pyplot as plt


# In[50]:


print("Problem 1")
# ai prompt: write a code that creates a subsample containing N random draws
# from a Gaussian distribution with a width of omega = 13 and mean of mu = 55

def subsample (N):
    """
    given constant values of omega and mu, calculate gaussian distribution from N draws

    parameter:
    N - number of draws
    return:
    gaussian distribution
    """
    return np.random.normal(55, 13, N) #random values, normal = gaussian
    # fills in specific values of omega and mu, calculate with given N
    


# In[51]:


print ("Problem 2")


sample_values = [] #set equal to empty list to add into 
for i in np.arange(0,10): 
    # loop through 0-9
    sample_gaus = subsample(10) # gaussian with N = 10
    sample_mu = np.mean(sample_gaus) # find mean from sample
    sample_omega = np.std(sample_gaus) # find standard deviation from sample
    sample_values += [i, sample_mu, sample_omega] # add all found values into list
    
sample_values = np.array(sample_values).reshape(10,3) # turn list into array
# shape array into 10 x 3 form
print(sample_values)
    


# In[52]:


print("Problem 3")
# prompt: write a code creating a subsample containing N=10 random draws, with an omega of
# 13 and mean of 55, for each sample record the sample number (0 to 9), the sample mean
# and the sample standard deviation in an array with one row per sample (10x3 array), write
# in python and use numpy

np.random.seed(42) # set random seed for reproducibility

# parameters 
num_samples_ai = 10
N_ai = 10
mean_ai = 55
omega_ai = 13

#generate 10 samples, each containing N=10 random draws (shape: 10x10)
draws = np.random.normal(loc = mean_ai, scale = omega_ai, size = (num_samples_ai, N_ai))

# calculate metrics across each sample (axis=1)
sample_numbers = np.arange(num_samples_ai).reshape(-1,1)
sample_means = np.mean (draws, axis = 1, keepdims = True)
sample_std = np.std(draws, axis = 1, ddof = 1, keepdims = True)

# combine into 10x3 array
results_array = np.hstack((sample_numbers, sample_means, sample_std))
print("Results Array")
print(results_array)

# my code compares using the np.mean and np.std to find the sample values, except
# my code uses a for loop and ai code does not, they stack the found values of each to 
# make one 10x3 array, i made a list then converted into an array and reshaped 


# In[53]:


print("Problem 4")
np.savetxt("practicum2_kenzb4_array_to_txt_file.txt", results_array,
           header = "Number of Draws is: 10")
# name file, give input (my array), header adds comment to top of page


# In[54]:


print("Problem 5")



def calculate_results(N):
    """
    given different N values, find 10 samples (find mean and std)
    for each N, sample 10 times, record in 2D array for each, append to file

    parameters:
    N number of random draws

    results:
    array of sample values for each N
    sample values have sample mean and sample omega 
    
    
    """
    sample_values = [] # set empty list to hold values

    for i in np.arange(0,10):
        sample_gaus = subsample(N) 
        sample_mean = np.mean(sample_gaus) 
        sample_omega = np.std(sample_gaus)
        sample_values.append([sample_mean, sample_omega]) # add mean and omega into the sample list
    
    sample_values = np.array(sample_values) #convert to array

    with open("practicum2_kenzb4_array_to_txt_file.txt", "a") as f:
        np.savetxt(f, sample_values, header = f"Number of Draws is: {N}")
        # save array made into file without writing over its preexisting data
        
    return (sample_values)
    

results_100 =     calculate_results(100)
results_1000 =    calculate_results(1000)
results_10000 =   calculate_results(10000)
results_100000 =  calculate_results(100000)
results_1000000 = calculate_results(1000000)
       


# In[55]:


print("Problem 6")

# ai help prompt: if i have 6 10 row arrays, 1 being 3 columns and 5 being 2 columns, 
#how can i read in just htier mean values, for the first 10x3 array it is
#in the second column and for the 5 10x2 arrays it is in the first column


#load text for each value, for 10 use column 2
#skip rows corresponding to location in file
mean_10 =       np.loadtxt("practicum2_kenzb4_array_to_txt_file.txt", skiprows = 1,
                     max_rows = 10, usecols=1)
# for all others 100-1000000 use column 1
mean_100 =      np.loadtxt("practicum2_kenzb4_array_to_txt_file.txt", skiprows = 12,
                     max_rows = 10, usecols=0)
mean_1000 =     np.loadtxt("practicum2_kenzb4_array_to_txt_file.txt", skiprows = 23,
                     max_rows = 10, usecols=0)
mean_10000 =    np.loadtxt("practicum2_kenzb4_array_to_txt_file.txt", skiprows = 34,
                     max_rows = 10, usecols=0)
mean_100000 =   np.loadtxt("practicum2_kenzb4_array_to_txt_file.txt", skiprows = 45,
                     max_rows = 10, usecols=0)
mean_1000000 =  np.loadtxt("practicum2_kenzb4_array_to_txt_file.txt", skiprows = 56,
                     max_rows = 10, usecols=0)

def calc_std(file_data):
    '''
    take data read in from file and calculate the standard deviation

    parameters:
    10x1 array

    result:
    float value of standard deviation
    '''
    std_sample = np.std(file_data) #calculates standard deviation 

    return std_sample

#ai help prompt: can i write a print statement where it will have the sample size and 
# and standard deviation as a string and then values below but all evenly spaced

sample_sizes = [10, 100, 1000, 10000, 100000, 1000000] #writes values as list
std_values = [calc_std(mean_10), calc_std(mean_100), calc_std(mean_1000), 
              calc_std(mean_10000), calc_std(mean_100000), calc_std(mean_1000000)]
# writes calculated standard deviations for each value in list




print(f"{'Sample Size' : <15}{'Std. Dev. of Mean' : <20}\n"
      f"{sample_sizes[0] : <15}{std_values[0] : <20.1f}\n"
      f"{sample_sizes[1] : <15}{std_values[1] : <20.1f}\n"
      f"{sample_sizes[2] : <15}{std_values[2] : <20.1f}\n"
      f"{sample_sizes[3] : <15}{std_values[3] : <20.1f}\n"
      f"{sample_sizes[4] : <15}{std_values[4] : <20.1f}\n"
      f"{sample_sizes[5] : <15}{std_values[5] : <20.1f}\n")
# print all evenly spaced with f line and to 1 decimal place for standard deviation




# In[56]:


#Make a log-log plot of the standard deviation of the mean vs. sample
#size. The sample size should be the independent variable on your plot. Save as
#PNG
print("Problem 7")
# make standard deviation of mean into array --> turn into log
sample_sizes = np.array(sample_sizes) #takes previous list and converts into array
sample_sizes_log = np.log(sample_sizes) # converts array into log

# make sample size into array --> turn into log
std_values = np.array(std_values) #takes previous list and converts into array
std_values_log = np.log(std_values)

#plot with log of each array
plt.plot(sample_sizes_log, std_values_log, linewidth = 3)
plt.title("Log-Log Graph")
plt.xlabel("Sample Sizes")
plt.ylabel("Standard Deviation")
plt.savefig("practicum2_kenzb4_graph1.png") #save as png
          


# In[ ]:




