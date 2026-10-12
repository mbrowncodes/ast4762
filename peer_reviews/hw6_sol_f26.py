#!/usr/bin/env python

# Initial version AST5765/4762 HW6 Solutions by Joseph Harrington <jh@physics.ucf.edu>
# Adapted by TK Fall 2024
# Cleaned up, changed HW7->HW6 by Joseph Harrington <jh@ucf.edu> Fall 2026

import numpy as np 
import matplotlib.pyplot as plt
import astropy.io.fits as fits
import os
import time

# My username...
# If you have a Unix-based machine, you can add who you are with getpwuid:
# import pwd
# username = pwd.getpwuid(os.getuid())[0]
# --> gives me my username on this machine
# This is harder to do with Windows (need something like PyWin32).

# So, if I'm using a different one from my Unix login, or I'm on Windows:
username = 'sol'

# # ----------------------------------------------------------------------------------
# # This is the start of the HW, which you did in Practicum 4:
# # ----------------------------------------------------------------------------------

# ### Define a variable (e.g., datadir) that holds the data directory name (including the final “/”) and another variable (e.g., fext) that holds the FITS extension string (including the dot (aka “.fits”) ). If you need more hard-coded values, come back and enter them in this section of the assignment.

datadir = '/home/jh/ast/teaching/ast5765/hw/hw6/hw6_data/'
fext    = '.fits'
extlen  = len(fext)

# ### Initialize two lists, one for your target images and one for your dark images (called, e.g., objfile and darkfile). These lists will contain the file names of the object (files rdpharocor_stars_13s_\*) and dark (files rdpharocor_dark_13s_\*) files. To populate the lists, use the appropriate os command to list the datadir. Don’t hard code the names in your homework file!
# 
# ### Your code should then identify whether a file should go into the objfile or darkfile list and populate the lists. Make sure to not include the .fits extension in the lists (as we already have this under fext, or whatever variable you created)!

allfiles = os.listdir(datadir)

for i in allfiles:
  print(i)

# Files printed (dummy=''' text ''' is like a multiline comment):
dummy = '''
rdpharocor_dark_13s_1.fits
rdpharocor_dark_13s_2.fits
rdpharocor_k_lampoff_1.fits
rdpharocor_k_lampoff_2.fits
rdpharocor_k_lampoff_3.fits
rdpharocor_k_lampoff_4.fits
rdpharocor_k_lampoff_5.fits
rdpharocor_k_lampon_4.fits
rdpharocor_k_lampon_5.fits
rdpharocor_stars_13s_1.fits
rdpharocor_stars_13s_2.fits
rdpharocor_stars_13s_3.fits
rdpharocor_stars_13s_4.fits
rdpharocor_stars_13s_5.fits
rdpharocor_stars_13s_6.fits
rdpharocor_stars_13s_7.fits
rdpharocor_stars_13s_8.fits
rdpharocor_stars_13s_9.fits
archival_data
'''

objfile  = []  # list for my science obs
darkfile = []  # list for my darks
for file in allfiles:
  if 'stars' in file:
    objfile.append(file[:-extlen])
  elif 'dark' in file:
    darkfile.append(file[:-extlen])

objfile  = sorted( objfile)
darkfile = sorted(darkfile)
print("objfile:")
for i in objfile:
  print(i)

print("darkfile:")
for i in darkfile:
  print(i)

# Filenames printed:
dummy = '''
objfile:
rdpharocor_stars_13s_1
rdpharocor_stars_13s_2
rdpharocor_stars_13s_3
rdpharocor_stars_13s_4
rdpharocor_stars_13s_5
rdpharocor_stars_13s_6
rdpharocor_stars_13s_7
rdpharocor_stars_13s_8
rdpharocor_stars_13s_9
darkfile:
rdpharocor_dark_13s_1
rdpharocor_dark_13s_2
'''

# ### Use informative statements to print datadir, fext, and only the last elements of objfile and darkfile (one from each).

print('The data for this HW are under folder: ',   datadir)
print('All files have an extension of: ',             fext)
print('The last element of the science obs is: ',  objfile[-1])
print(' and the last element for the darks is: ', darkfile[-1])

# Info printed:
dummy = '''
The data for this HW are under folder:  /home/jh/ast/teaching/ast5765/hw/hw6/hw6_data/
All files have an extension of:  .fits
The last element of the science obs is:  rdpharocor_stars_13s_9
 and the last element for the darks is:  rdpharocor_dark_13s_2
'''

# ### Read one data file and determine the data array sizes. Assign these to two variables (e.g., ny and nx).

exampfile = datadir+objfile[0]+fext
print(exampfile)

# /home/jh/ast/teaching/ast5765/hw/hw6/hw6_data/rdpharocor_stars_13s_1.fits

exampdata = fits.getdata(exampfile)
nx, ny = exampdata.shape

print(nx, ny)

# 1024 1024


# ### Define two variables (called, e.g., nobj and ndark) that contain the numbers of files in the objfile and darkfile lists by querying the sizes of the lists. Why should you not hardcode it? 
# 
# ### Use informative statements to print ny, nx, nobj, and ndark

nobj  = len(objfile)
ndark = len(darkfile)

print(nobj, ndark)

# 9 2

print('The size of my images is {0:d} by {1:d} pixels.'.format(nx, ny) )

# The size of my images is 1024 by 1024 pixels.

print('I have a total of {0:d} target images and {1:d} dark images'.format( nobj, ndark) )

# I have a total of 9 target images and 2 dark images

# ### Create two 3D arrays (float64), one for the objects and one for the darks. Your arrays should have sizes (nobj, ny, nx) and (ndark, ny, nx) respectively. Print the shapes of these arrays.

obj  = np.zeros(( nobj, ny, nx))
dark = np.zeros((ndark, ny, nx))

print(obj.shape, dark.shape)

# (9, 1024, 1024) (2, 1024, 1024)

# ### Read the target and dark data into the arrays. Save the last header from each set in a variable (e.g., objhead and darkhead). Read and print the date of observation (DATE-OBS) from each of these.

for i in range(nobj):
  file = datadir + objfile[i] + fext
  obj[i,:,:],   objhead = fits.getdata(file, header= True)

for i in range( ndark ):
  file = datadir + darkfile[i] + fext
  dark[i,:,:], darkhead = fits.getdata(file, header=True)

# ### Extra credit (5 points) Why not print TIME-OBS?
# 

# It's blank in the "stars" images.


# # ----------------------------------------------------------------------------------
# # ...and this is the solution to the actual HW:
# # ----------------------------------------------------------------------------------

# ### Use the appropriate numpy (or other) function that allows you to median-combine the images in a single function call, without loops. The function should accept your 3D array and return the median-combined 2D array.

# Problem 2a

# The function is np.median()

# Problem 2b

darkmeddata = np.median(dark, axis=0)
prty = 217 # y-pixel value to print
prtx = 184 # x-pixel value to print
print("darkmeddata ({0:d}, {1:d}) = {2:.3f}".format(
                     prty,  prtx,    darkmeddata[prty, prtx]))

# darkmeddata[217, 184] = 19.000000

# Problem 2c

# Note: "import time" at start of notebook, NOT HERE!

darkhead.add_history(  'medcombine: '
                     + time.strftime('%a %b %d %H:%M:%S %Z %Y')
                     + username)

darkhead.add_history('Median combination of ' + str(dark.shape[0])
                     +' images.')
darkhead.add_history('Some header entries (like times) are wrong.')

# Problem 2d

# get the name from the darkfile list:
outname = darkfile[0][:-1]

# ...and write it out to the requested file name:
fits.writeto(outname + 'med' + fext,
             np.float32(darkmeddata), darkhead, overwrite=True)

print(f"See FITS file {outname+'med'+fext}.")

# See FITS file rdpharocor_dark_13s_med.fits.

# Problem 2e

print("Before subtraction, obj[{0:d}, {1:d}, {2:d}] = {3:.2f}".format(
                                0,     prty,  prtx,    obj[0, prty, prtx]))

# Before subtraction, obj[0, 217, 184] = 10879.00

# do the subtraction in loop or in one line:

#for o in range(obj):
#    obj[o, :, :] = obj[ o, :, :] - darkmeddata

obj -= darkmeddata

# This is called "broadcasting".  If two arrays of non-matching size
# are to be operated on, and one fits nicely into the other, the
# smaller one will be repeated to make up the empty space.  This is
# like an implicit "for" loop that subtracts darkmeddata from each
# image in objdata in turn, but it's faster, easier to read, and
# therefore much less prone to bugs.  Use it whenever you can!

print("After subtraction, obj[{0:d}, {1:d}, {2:d}] = {3:.2f}".format(
                               0,     prty,  prtx,    obj[0, prty, prtx]))

# After subtraction, obj[0, 217, 184] = 10860.00

# write it out:
fits.writeto('hw6_myname_prob2_graph1'+fext,
             np.float32(obj[0]), objhead, overwrite=True )

