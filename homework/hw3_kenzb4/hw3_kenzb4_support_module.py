"""Support file for homework 3, containing function square and squareplot
square will take in input and output with the square of that value, may
be a scalar or array

squareplot will plot the squared numbers, takes in 3 arguments, low end 
and high end of plot, as well as number of points to plot
includes one argument (saveplot=False), it creates array x
evenly spaced points from low to high range
calls function square(once) to get array y
plot y vs x
axis (vert = output, hori = input)


"""
#imports 
import os 
import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt  
import astropy.io.fits as fits


#functions
def square(var1):
    """returns the square of the input
    input: scalar or array of any dimention or numerical type
    output: scalar or array (depends on input), value squared

    Parameters
    -----------
    var1: inputted variable (either a float, integer, or a numpy
    array) 
    

    Returns
    ---------
    sqvar1 : square of input of var1 (float, integer, or numpy
    array)
    
    Other Parameters
    ----------------

    Raises
    ------
    
    See Also
    --------

    Notes
    -------

    Refrences
    ---------

    Examples
    --------
    #ex 1:
    >>>array1 = np.arange(0,11,1) # create array from 0 up to and including 10
    >>>print (array1)
    [ 0  1  2  3  4  5  6  7  8  9 10]
    >>>print(square(array))
    [  0   1   4   9  16  25  36  49  64  81 100]

    #ex2:
    >>>integer1 = 3
    >>>print(square(integer1))
    9
    
    #ex3:
    >>>print(square(3))
    9

    #ex4:
    >>>print(square(3.3))
    10.889999999999999

    #ex5
    >>>print(square(np.arange(0,11,1)))
    [  0   1   4   9  16  25  36  49  64  81 100]

    Revisions
    ---------
    2026-09-15 ma755497@ucf.edu edited Revisions section, to note that this
               file was made a copy and is edited
    """
    z = var1**2
    return z


    pass
