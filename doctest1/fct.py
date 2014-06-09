"""
Defines a function and demonstrates how to run the examples as doctests
which happens when executing the module as a script.

Run the doctest in ant of the follwing two ways:

    $ python fct.py      # quiet mode if all is tests are ok
    $ python fct.py -v   # verbose mode for all tests

Doctest preparation - the following line must not be removed as it
defines the function "f" in the workspace:

    >>> from fct import f   # DO NOT REMOVE THIS LINE

"""

import numpy as np

def f(x):
    """Computes exp(1+sin(x)).
    
    Examples:
        >>> f('a')
        Traceback (most recent call last):
        ...
        TypeError: Input must be a float or int.
        >>> f(1.0) # doctest: +ELLIPSIS
        6.3058071887055...
        >>> f(0)
        2.7182818284590451
        >>> [f(n) for n in range(5)] # doctest: +NORMALIZE_WHITESPACE
        [2.7182818284590451,
         6.3058071887055274,
         6.7483459258003178,
         3.1302723328262143,
         1.2753204810250782]
        >>> f(1.0)   # doctest: +ELLIPSIS
         7.3058071887055...
         
    """
    if not (type(x) == float or type(x) == int):
        raise TypeError('Input must be a float or int.')
    
    return np.exp(1.0 + np.sin(x))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    