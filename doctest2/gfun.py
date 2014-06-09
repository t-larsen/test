"""
Defines a function and demonstrates how to run the examples as doctests
which happens when executing the module as a script.

Run the doctest in ant of the follwing two ways:

    $ python gfun.py      # quiet mode if all is tests are ok
    $ python gfun.py -v   # verbose mode for all tests

Doctest preparation - the following line must not be removed as it
defines the function "f" in the workspace:

    >>> from gfun import g   # DO NOT REMOVE THIS LINE

"""

import numpy as np

def g(x):
    """Computes sin(x**2).
    
    Input:
        x (float, int) : 
    Output:
        g (float) : sin(x**2)
    Examples:
        >>> print('{0:.5f}'.format(g(2.0)))
        -0.75680
        >>> print('{0:.7e}'.format(g(2.0)/7.66E-7))
        -9.8799281e+05
        >>> round(g(2.0), 6)
        -0.756802
        
    """
    if not type(x) == float:
        raise TypeError('Input must be a float.')
    
    return np.sin(x**2)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    