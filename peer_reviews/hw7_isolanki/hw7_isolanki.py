#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Homework 7
#Ishita Solanki
#Created on Thu Oct  1 17:39:35 2026

import numpy as np
from astropy.io import fits
import os

print("Problem 2")

#Hard-coded values stored in variables
datadir = "hw6_data/"

fext = '.fits'

#strings to help categorize the files
obj_text  = 'stars'
dark_text = 'dark'

#string for name of median dark frame 
dark_name         = 'dark_13s_med.fits'
obj_dark_sub_name = 'hw7_isolanki_prob2_graph1.fits'


#Part a

"""The np.median() function can be used to median combine the image in a single
function call, without loops. The first argument will be the 3D array and the 
second argument will be axis = 0. This is an additional thing we have to specify
to apply the median function across the images as we want. Axis 0 is for the 
images (outermost dimension), axis 1 is for the rows and axis 2 is for the 
columns.
"""

#Reading in the data, code from practicum 

#initializing the lists
objfile  = []
darkfile = []

#iterating over every file/folder in datadir
for file in os.listdir(datadir):
    
    #splitting into filename and extension
    parts = os.path.splitext(file)
    fname = parts[0]
    
    #take only .fits files
    if parts[-1] == fext:
        
        #to get the target images
        if obj_text in fname:
            objfile.append(fname)
            
        #to get the dark images
        elif dark_text in fname:
            darkfile.append(fname)
            
objfile.sort()      #sorting as the list was out of order


#load the fits file as header data unit list
header = fits.getheader(datadir + objfile[0] + fext)

#using the headers to get the dimensions of the data array
nx = header['NAXIS1']
ny = header['NAXIS2']

#length of the arrays
nobj  = len(objfile)
ndark = len(darkfile)


#Creating the dataframes, with datatype float 64 and desired shape
objdata  = np.zeros((nobj,  ny, nx), dtype = np.float64)
darkdata = np.zeros((ndark, ny, nx), dtype = np.float64)


#Populating the dataframes

#iterating to get data from each target fle and store it 
for i in range(nobj):
    objdata[i,:,:]  = fits.getdata(datadir + objfile[i] + fext) 
    
    #store header of last target file
    if i == nobj - 1:
        objhead     = fits.getheader(datadir + objfile[i] + fext)

#iterating to get data from each dark fle and store it    
for k in range(ndark):
    darkdata[k,:,:] = fits.getdata(datadir + darkfile[k] + fext) 
    
    #store header of last dark file
    if k == ndark - 1:
        darkhead    = fits.getheader(datadir + darkfile[k] + fext)
 
    
#Part b

#Median combine along the axis containg images
darkdata_med = np.median(darkdata, axis = 0) 

print("Value of pixel [217, 184] of the median-combined dark image: ", \
      darkdata_med[217, 184])

#Part c   

#Add history entry to the header
darkhead['HISTORY'] = "Produced by median-combineding two dark frames"

#Part d

#write the median dark
fits.writeto(dark_name, darkdata_med, header = darkhead, overwrite = True)

#Part e
print("Value of pixel [217, 184] of the first object frame before dark " 
      + "subtraction: ", objdata[0, 217, 184])


#subtracting the median dark frame from every object frame
#this will work due to broadcasting in numpy
objdata -= darkdata_med

objhead['HISTORY'] = 'Subtracted median-combined dark frame'

#write the first frame
fits.writeto(obj_dark_sub_name, objdata[0], header = objhead, overwrite = True)

print("Value of pixel [217, 184] of the first object frame before dark " 
      + "subtraction: ", objdata[0, 217, 184])
