"""
Doctest required import:
    >>> from fun.mathfun import f

Support imports:
    >>> import os


"""


def f(x, state=None, f_name='_dummy.dat'):
    """Computes exp(1 + sin(x)) and possibly push result to file fname.

    Input:
        x : real, int
            Input to exp(1 + sin(x)).
        state : None, 'clean' or 'append'
            Tells if output file is involved and if clean
            or appended fields.
        f_name : str
            Name of file in which 'x  f(x)' is stored.
    Output:
        f : real
    Raises:
        TypeError if x is not a float or int.
        TypeError if fname is not a str.
    Examples:
        >>> round(f(0.1), 8)
        3.00366562
        >>> round(f(0.1, state=None), 8)
        3.00366562
        >>> test_name = 'test/fun/mathfun/test_mathfun_func_A.dat'
        >>> round(f(0.1, state='clean', f_name=test_name), 8)
        3.00366562
        >>> round(f(3, state='clean', f_name=test_name), 10)
        3.1302723328
        >>> round(f(-3, state='append', f_name=test_name), 10)
        2.3605154163
        >>> os.remove(test_name) if os.path.isfile(test_name) else None

    """
    import numpy as np

    # Catch bad input
    if not type(x) in (float, int):
        raise TypeError("Input ({!r}) must be a float or int.".format(x))
    if not type(f_name) == str:
        raise TypeError("Input ({!r}) must be a str.".format(f_name))

    # Compute output
    fx = np.exp(1 + np.sin(x))

    # Create file if necessary
    if state is not None:
        if state == 'clean':
            with open(f_name, 'w') as f_handle:
                np.savetxt(f_handle, np.array([x, fx]).reshape(-1, 2))
        elif state == 'append':
            with open(f_name, 'a') as f_handle:
                np.savetxt(f_handle, np.array([x, fx]).reshape(-1, 2))
        else:
            raise NameError("Wrong value ({!r}) for 'state'.".format(state))

    return fx


if __name__ == '__main__':
    #
    f(3, f_name='_f.dat', state='clean')
