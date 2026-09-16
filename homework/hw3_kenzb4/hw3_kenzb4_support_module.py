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

# function imports
#from my_module import my_func, other_func

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
    stack over flow: https://stackoverflow.com/questions/62106028/what-is-the-difference-between-np-linspace-and-np-arange

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
    """
    z = var1**2
    return z

def squareplot(low, high, pt_num, saveplot=False):
    """ plots the square of numbers
    input: the range of values, a high and low number for range
    and number of points
    output: an array of evenly spaced points from low to high with spacing 
    related to pt numbers, call square function on new array
    plot arrays y vs x (regualr array,x, and array with square function called on it, y)

    Parameters
    -----------
    low: scalar (integer or float value)
        gives the lowest number in the plot, the min value 
    high: scalar (integer or float value)
        gives the highest number in the plot, the max value
    pt_num: (positive integer)
        number of points in plot 
    
 
    Returns
    ---------
    x: array of range (low, high, pt_num), from low to and including high with
    step size of number of points
    y: array that is the squared value of array x, same step size, range now differs
    plot : save plot through file, not given here
    
    Other Parameters
    ----------------
    saveplot = False

    Raises
    ------
    check to see what happens if (high is < low)
    check to see if any step sizes dont work
    
    See Also
    --------

    Notes
    -------
    uses function square 

    Refrences
    ---------

    Examples
    --------
    >>>squareplot(0, 10, 5)
    # the plots are given 
    >>>squareplot(.1, 7, 20)
    # the plot is given
    >>>squareplot(.1, 7, 20, "testsquareplot.pdf"
    #pdf file of plot saves in directory 
    """
    

    
    x = np.linspace(low, high, pt_num) #makes array from input graph values
    #includes highest value in x
    y = square(x) #makes new array that is square of x array values

    plt.figure(  figsize=(8,5)  ) #make figure readable size
    plt.plot(x, y)  # plot x vs y 
    plt.title("Square Function") # following homework naming convention
    plt.xlabel("Input")
    plt.ylabel("Output")

    if saveplot is not False:
        plt.savefig(saveplot, format="pdf") # if optional parameter is not False
        # save plot, as pdf with their inputted "filename.pdf"
    return 


"""
    Revisions
    ---------
    2026-09-15 ma755497@ucf.edu edited Revisions section, to note that this
               file was made a copy and is edited
"""


pass
