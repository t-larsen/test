"""
This is the "example" module.

>>> from warm.tvt import ftvt


The example module supplies one function, ftvt().  For example,

"""

def ftvt(n):
    """Return the factorial of n, an exact integer >= 0.

    If the result is small enough to fit in an int, return an int.
    Else return a long.

    >>> [ftvt(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> [ftvt(long(n)) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> ftvt(30)
    265252859812191058636308480000000L
    >>> ftvt(30L)
    265252859812191058636308480000000L
    
    """

    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result

