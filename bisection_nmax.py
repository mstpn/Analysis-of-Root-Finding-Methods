import numpy as np

def bisection_nmax(a, b, TOL):
    '''
    Parameters
    ----------
    a : float
        DESCRIPTION. a is the left side of interval [a, b]
    b : float
        DESCRIPTION. b is the right side of interval [a, b]
    TOL : float, optional
        DESCRIPTION. Tolerance (epsilon). The default is 1e-4.

    Returns
    -------
    nmax
    '''
    return int(np.ceil(np.log2(np.abs(b-a)/TOL)))