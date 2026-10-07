#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Mackenzie Brown
# Homework 6 (and Practicum 4 )
# 10/01/2026


# In[5]:


# imports
import numpy as np
import os 
import astropy.io.fits as fits


# In[30]:


print("Problem 2")
#2a 

# Hardcoded variables here 
datadir = "hw6_data/" #location of data 
fext = ".fits" #fits extenstion


# In[23]:


#2b 

objfile = []    #initalize target images
darkfile = []   #initalize dark images

#COME BACK AND FIX TO SORT DATA, USE SORT ROUTINE

for filename in sorted(os.listdir(datadir)):
    sort_f, fext = os.path.splitext(filename) # split each file into name and ".fits" part
    
    if "rdpharocor_stars_13s_" in sort_f:
        objfile.append(sort_f)
    elif "rdpharocor_dark_13s_" in sort_f:
        darkfile.append(sort_f)


# In[24]:


#2c

#imformative print statements (datadir, fext, last element of objfile and darkfile)
print("\n", "Data Directory:",   datadir, "\n",
            "File Extention:",   fext, "\n",
            "Last Object File:", objfile[-1], "\n",
            "Last Dark File:",   darkfile[-1], "\n")


# In[25]:


#2d 

# read in random element in objfile (choose element 3)
with fits.open(os.path.join(datadir, objfile[3] + fext)) as hdul:
    data = hdul[0].data #name data
    ny, nx = data.shape #assign data array sizes
    


# In[26]:


#2e 

# contain number of files in lists, by query size of list 
nobj =  len(objfile)
ndark = len(darkfile)

#imformative print statements 
print("\n", "Number of Rows:",         ny, "\n",
            "Number of Columns:",      nx, "\n",
            "Number of Object Files:", nobj, "\n",
            "Number of Dark Files:",   ndark)


# In[27]:


print("Problem 3")
# write commands to make and populate data cubes with target and dark images 

#3a
sample_dark_arr = np.zeros((ndark, ny, nx), dtype = np.float64) #dark array 

sample_obj_arr = np.zeros( (nobj, ny, nx),  dtype = np.float64) #obj array 

#check shapes of arrays
print("\n", "Shape of the Dark Array:",   sample_dark_arr.shape, "\n",
            "Shape of the Object Array:", sample_obj_arr.shape) 


# In[28]:


#3b

#populate data, read in target and dark data into arrays
for i in range(nobj): 
    sample_obj_arr[i], objhead = fits.getdata(os.path.join(
        datadir, objfile[i] + fext), header = True) 
   
for i in range(ndark): 
    sample_dark_arr[i], darkhead = fits.getdata(os.path.join(
        datadir, darkfile[i] + fext), header = True) 

print("Object Observation Date:", objhead["DATE-OBS"])
print("Dark Observation Date:", darkhead["DATE-OBS"])


# In[29]:


#3c
print("Object Observation Time:", objhead["TIME-OBS"])
print("Dark Observation Time:", darkhead["TIME-OBS"])


# In[ ]:





# In[ ]:




