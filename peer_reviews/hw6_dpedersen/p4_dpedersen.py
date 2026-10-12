#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Dalton Pedersen
# P4 / HW6
# 10/03/26


# In[22]:


import os
import astropy.io.fits as fits
import numpy as np


# In[23]:


datadir = 'hw6_data/'

fext = '.fits'


# In[24]:


objfile = []
darkfile = []


# In[25]:


for fname in os.listdir(datadir):
    #check if it is a fits file
    if fname.endswith(fext):
        #remove fits extension to get root name
        root_name = fname[:-len(fext)]

        #check if it is target or dark
        if fname.startswith('rdpharocor_stars_13s'):
            objfile.append(root_name)
        elif fname.startswith('rdpharocor_dark_13s'):
            darkfile.append(root_name)


# sort files to put in order
objfile.sort()
darkfile.sort()


# In[ ]:





# In[26]:


print(f'Data Directory: {datadir}')
print(f'Fits Extension: {fext}')
print(f'Last object file: {objfile[-1] if objfile else 'None'}') # error handling for empty objfile list
print(f'Last dark file: {darkfile[-1] if darkfile else 'None'}')


# In[27]:


#make path to sample file
sample_path = os.path.join(datadir, objfile[0] + fext)


# In[28]:


with fits.open(sample_path) as hdul:
    sample_data = hdul[0].data
    ny, nx = sample_data.shape


# In[31]:


#this should not be hardcoded because it is very simple to determine this directly
# this allows the code to be more adaptable
nobj = len(objfile)
ndark = len(darkfile)


# In[32]:


print(f'Image Dimensions (ny, nx): ({ny}, {nx})')
print(f'Number of object files: {nobj}')
print(f'Number of dark files: {ndark}\n')


# In[33]:


objcube = np.zeros((nobj, ny, nx), dtype=np.float64)
darkcube = np.zeros((ndark, ny, nx), dtype=np.float64)


# In[34]:


print(f'Object data cube shape: {objcube.shape}')
print(f'Dark data cube shape: {darkcube.shape}')


# In[36]:


objhead = None

for i, filename in enumerate(objfile):
    filepath = os.path.join(datadir, filename + fext)
    with fits.open(filepath) as hdul:
        objcube[i] = hdul[0].data.astype(np.float64)
        objhead = hdul[0].header #save last header


# In[37]:


darkhead = None

for i, filename in enumerate(darkfile):
    filepath = os.path.join(datadir, filename + fext)
    with fits.open(filepath) as hdul:
        darkcube[i] = hdul[0].data.astype(np.float64)
        darkhead = hdul[0].header #save last header


# In[38]:


obj_date_obs = objhead.get("DATE-OBS", "N/A")
dark_date_obs = darkhead.get("DATE-OBS", "N/A")


# In[39]:


print(f'Object Image Last DATE-OBS: {obj_date_obs}')
print(f'Dark Image Last DATE-OBS: {dark_date_obs}')


# In[40]:


# Extra Credit Problem 3:
#Typically in the fits standard the date-obs is formatted as a utc timestamp.
# This would contain the date and time and looking for time-obs is redundant.


# In[ ]:




