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
    plot arrays y vs x 

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
    """
    >>>squareplot(0, 10, 5)

    
    x = np.linspace(low, high, pt_num) #makes array from input graph values
    y = square(x) #makes new array that is square of x array values

    plt.figure(  figsize=(8,5)  ) #make figure readable size
    plt.plot(x, y)  # plot x vs y 
    plt.title("Square Function") # following homework naming convention
    plt.xlabel("Input")
    plt.ylabel("Output")

    #saveplot = False
    return

   

#example function 
def foo(var1, var2, long_var_name='hi') :
    #this is our function's docstring!
    """A one-line summary that does not use variable names or the
    function name.

    Several sentences providing an extended description. Refer to
    variables using back-ticks, e.g. `var`.

    Parameters
    ----------
    var1 : array_like
        Array_like means all those objects -- lists, nested lists, etc. --
        that can be converted to an array.  We can also refer to
        variables like `var1`.
    var2 : int
        The type above can either refer to an actual Python type
        (e.g. ``int``), or describe the type of the variable in more
        detail, e.g. ``(N,) ndarray`` or ``array_like``.
    Long_variable_name : {'hi', 'ho'}, optional
        Choices in brackets, default first when optional.

    Returns
    -------
    describe : type
        Explanation
    output : type
        Explanation
    tuple : type
        Explanation
    items : type
        even more explaining

    Other Parameters
    ----------------
    only_seldom_used_keywords : type
        Explanation
    common_parameters_listed_above : type
        Explanation

    Raises
    ------
    BadException
        Because you shouldn't have done that.

    See Also
    --------
    otherfunc : relationship (optional)
    newfunc : Relationship (optional), which could be fairly long, in which
              case the line wraps here.
    thirdfunc, fourthfunc, fifthfunc

    Notes
    -----
    Notes about the implementation algorithm (if needed).

    This can have multiple paragraphs.

    You may include some math:

    .. math:: X(e^{j\omega } ) = x(n)e^{ - j\omega n}

    And even use a greek symbol like :math:`omega` inline.

    References
    ----------
    Cite the relevant literature, e.g. [1]_.  You may also cite these
    references in the notes section above.

    .. [1] O. McNoleg, "The integration of GIS, remote sensing,
       expert systems and adaptive co-kriging for environmental habitat
       modelling of the Highland Haggis using object-oriented, fuzzy-logic
       and neural-network techniques," Computers & Geosciences, vol. 22,
       pp. 585-588, 1996.

    Examples
    --------
    These are written in doctest format, and should illustrate how to
    use the function.  Use the plain python prompt (">>> ") for the
    example commands, and put the expected output on a line without a
    prompt, as follows:


    >>> a=[1,2,3]
    >>> print([x + 3 for x in a])
    [4, 5, 6]
    >>> print("a\n\nb")
    a
    <BLANKLINE>
    b

    The examples in docstrings can be run with the 'doctest' package:

    python -m doctest -v doctest_simple_with_docs.py

    See:

    https://pymotw.com/2/doctest/

    for more examples.  There are several different testing packages,
    including 'doctest' and 'nose'.  All use the same format when it
    comes to tests in docstrings, but offer different testing
    functionality.

    nosetests --with-doctest your_python_file.py

    If your example prints random numbers, use an ellipsis ('...') to
    skip the part of the output that is variable.

    Revisions
    ---------
    2026-09-15 ma755497@ucf.edu edited Revisions section, to note that this
               file was made a copy and is edited
   """


    pass
