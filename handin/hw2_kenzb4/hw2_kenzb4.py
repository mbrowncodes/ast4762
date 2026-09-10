#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Mackenzie Brown
# Homework 2
# 9/2/2026


# In[2]:


import numpy as np 
import matplotlib.pyplot as plt


# In[3]:


#problem 2 

# a1) create array with integers x from 0 to 1000, how many elements are needed?

x = np.arange(0,1001,1) #start at 0, include 1000, step size 1 (int)
x_shape = np.shape(x) #to tell number of elements
print("The number of elements needed is", x_shape)


# a2) print datatype, min, and max of array

print(type(x)) # print data type x
print(min(x)) # minimum value
print(max(x)) # maximum value

# b1) re-scale x to contain values from 0 to 2pi

x = x*(2*np.pi / 1000) # multiply values of 0 by 2pi/1000 (cancels denom for last term so == 2pi)

# b2) print min and max of new x array

print(min(x)) #new scaled arrays min
print(max(x))

# c) make array y, values are sine values of x

y = np.sin(x) # array with values of sin(x)
print(y)

# d) print value of element 234 of y

print(y[233]) #0 is first element -- 233 is 234th element


# In[9]:


#problem 3 

# a) plot y vs x 
plt.plot(x,y) 
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Sin Function') 
# b) save as png
plt.savefig('Problem2_kenzb4.png') #saved as .png
plt.show()



# In[4]:


#problem 4

# a) make 'ramp' array with 101 evenly spaced elements from -1 to 1

ramp = np.arange(-1,1.01, 0.02) #array with -1 to 1, spacing is 0.02

clipped = np.clip(ramp, -0.5, 0.5) #clip array ramp, make values < -0.5 
# equal to -0.5, and make values >0.5 equal to 0.5

plt.plot(ramp, ramp, 'r', ramp, clipped, 'b') #plot ramp x and y in red
# plot ramp and clipped ramp(y values) in blue
plt.yticks(np.arange(-1.0, 1.25, 0.25)) #change y axis ticks to range from -1 to 1
plt.title('Clipped Ramp') 
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig('Problem3_kenzb4.pdf') #save as pdf
plt.show()


# In[ ]:


#problem 5 
#give 2 urls outside UCF that give free astronomical software
#written in python, write paragraph of each package 


# https://astroquery.readthedocs.io/en/latest/
'''
Astroquery is very helpful for downloading astronomical data from databases. 
Rather than going to different astronomy websites manually, Astroquery allows you 
to send queries to these databases in one place and get their information returned 
to you, in a usable way for Python coding. For many research projects, you will want
to reference multiple databases and compare the different data provided. Astroquery 
makes this easier by accessing them in one place rather than learning to navigate each
site to download its data to individual files for each site. Instead this keeps your data 
in one easy to track place. 
'''
# https://docs.stingray.science/en/stable/
'''
Stingray is another free Python library that is used to analyze astronomical time-series
data. It is specifically designed to work with and manipulate data from X-ray observations.
This is especially useful when working with light curves and studying the brightness
changes of astronomical objects over time. I actually just did a research project
looking into the light curves of different asteroids, along with other data. Learning 
about Stingray was interesting and I wish I knew about it earlier. Stingray requires
many familiar packages that we use in astronomical coding such as Astropy, Numpy, Scipy,
and Matplotlib. It can also be used to simulate data sets with statistical modeling.  
'''

