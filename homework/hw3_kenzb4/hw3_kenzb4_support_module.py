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
from my_module import my_func, other_func

#functions
def square(var1, var2):
    """returns the square of the input
    input: scalar or array of any dimention or numerical type
    output: scalar or array (depends on input), value squared

    Parameters
    -----------
    var1: array type of input
    var2: integer type of input

    Returns
    ---------
    sqvar1 : square of array input of var1
    sqvar2 : square of integer input of var2
    
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

    
    """
    

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
