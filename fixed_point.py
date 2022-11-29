import pandas as pd 
import numpy as np

def fixed_point(g, x0, tol, nmax):
    '''
    Parameters
    ----------
    g : function 
        DESCRIPTION. A function. Here we use lambda functions
    a : float
        DESCRIPTION. a is the left side of interval [a, b]
    b : float
        DESCRIPTION. b is the right side of interval [a, b]
    nmax : Int, optional
        DESCRIPTION. Maximum number of iterations. The default is 1000.
    tol : float, optional
        DESCRIPTION. Tolerance (epsilon). The default is 1e-4.

    Returns
    -------
    a dataframe
    '''
    
    xn = np.zeros(nmax, dtype=float)
    En = np.zeros(nmax, dtype=float)
    xn[0] = x0
    En[0] = x0
    
    for n in range(0, nmax-1):
        xn[n+1] = g(xn[n])
        En[n+1] = np.abs(xn[n+1]-xn[n])
        if En[n+1] < tol:
            return pd.DataFrame({'xn': xn[0:n+2], 'En': En[0:n+2]})
    return None