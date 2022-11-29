import pandas as pd 
import numpy as np

def secant_method(f, x0, x1, tol = 1e-4, nmax = 100, frame = True):
    '''
    Parameters
    ----------
    f : function
        DESCRIPTION.
    x0 : float
        DESCRIPTION. First initial estimate
    x1 : float
        DESCRIPTION. Second initial estimate
    tol : TYPE, optional
        DESCRIPTION. Tolerance (epsilon). The default is 1e-4.
    nmax : Int, optional
        DESCRIPTION. Maximum number of iterations. The default is 100.
    frame : bool, optional
        DESCRIPTION. If it is true, a dataframe will be returned. The default is True.

    Returns
    -------
    xn, fxn, Dfxn, n
    or
    a dataframe

    '''

    xn=np.zeros(nmax, dtype=float)
    fxn=np.zeros(nmax, dtype=float)
    
    xn[0] = x0
    xn[1] = x1
    for n in range(1, nmax-1):
        fxn[n] = f(xn[n])
        if abs(fxn[n]) < tol:
            if frame:
                return pd.DataFrame({'xn': xn[:n+1], 'fxn': fxn[:n+1]})
            else:
                return xn, fxn, n
        Dfxn = (f(xn[n]) - f(xn[n-1])) / (xn[n] - xn[n-1])
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn[n+1] = xn[n] - fxn[n]/Dfxn
    print('Exceeded maximum iterations. No solution found.')
    return None