#!/usr/bin/env python
# coding: utf-8

# In[57]:


# Mackenzie Brown
# Homework 6
# 10/05/2026


# In[58]:


#imports
import numpy as np
import os
import astropy.io.fits as fits


# In[60]:


# Hardcoded variables here 
datadir = "hw6_data/" #location of data 
fext = ".fits" #fits extenstion
objfile = []    #initalize target images
darkfile = []   #initalize dark images

#hw 6 hardcoded variables 
med_dark_file = "dark_13s_med"
graph_1_file = "hw6_kenzb4_prob2_graph1"


# In[61]:


print("Practicum 4 Recap")
for filename in sorted(os.listdir(datadir)):
    sort_f, fext = os.path.splitext(filename) # split each file into name and ".fits" part
    
    if "rdpharocor_stars_13s_" in sort_f:
        objfile.append(sort_f)
    elif "rdpharocor_dark_13s_" in sort_f:
        darkfile.append(sort_f)
print("\n", "Data Directory:",   datadir, "\n",
            "File Extention:",   fext, "\n",
            "Last Object File:", objfile[-1], "\n",
            "Last Dark File:",   darkfile[-1], "\n")
with fits.open(os.path.join(datadir, objfile[3] + fext)) as hdul:
    data = hdul[0].data #name data
    ny, nx = data.shape #assign data array sizes
nobj =  len(objfile)
ndark = len(darkfile)

#imformative print statements 
print("\n", "Number of Rows:",         ny, "\n",
            "Number of Columns:",      nx, "\n",
            "Number of Object Files:", nobj, "\n",
            "Number of Dark Files:",   ndark)
sample_dark_arr = np.zeros((ndark, ny, nx), dtype = np.float64) #dark array 
sample_obj_arr = np.zeros( (nobj, ny, nx),  dtype = np.float64) #obj array 

#check shapes of arrays
print("\n", "Shape of the Dark Array:",   sample_dark_arr.shape, "\n",
            "Shape of the Object Array:", sample_obj_arr.shape) 
for i in range(nobj): 
    sample_obj_arr[i], objhead = fits.getdata(os.path.join(
        datadir, objfile[i] + fext), header = True) 
   
for i in range(ndark): 
    sample_dark_arr[i], darkhead = fits.getdata(os.path.join(
        datadir, darkfile[i] + fext), header = True) 

print("Object Observation Date:", objhead["DATE-OBS"])
print("Dark Observation Date:", darkhead["DATE-OBS"])


# In[62]:


print("Problem 2")
#2a 

# make function to use median combo method: combine stack images
def median_combine(image_arr):
    """
    median combines stack of images together into one 2D image
    
    Parameters:
    -----------
    image_arr :  array, 3D array containing stack of images, axis[0] represent individual 
    images, axis[1] and axis[2] is image rows and columns
    
    Returns:
    --------
    median_image : array, 2D array with median value at each pixel for all images in stack
    
    Notes:
    --------
    specificy the axis to only work on image size, works over the stack of images 
    axis = 0 to not use a loop
    """
    median_image = np.median(image_arr, axis=0)

    return median_image


# In[63]:


#2b
# call function on dark data, print pixel [217,184]
median_dark = median_combine(sample_dark_arr)
print("Median dark pixel [217, 184]:", median_dark[217, 184])


# In[53]:


#2c
# add history entry in dark header
darkhead["HISTORY"] = "Median combined dark frame"


# In[54]:


#2d
# write median dark (with header abive) to new file
fits.writeto(med_dark_file + fext, median_dark, darkhead, overwrite=True)


# In[65]:


#2e
corrected_obj_arr = sample_obj_arr - median_dark # subtract median dark from obj arr
fits.writeto(graph_1_file + fext, corrected_obj_arr[0], objhead, overwrite = True)

print("Object before:", sample_obj_arr   [0, 217, 184])
print("Object after:",  corrected_obj_arr[0, 217, 184])


# In[ ]:





# In[ ]:




