import pandas as pd 
import numpy as np

def newton_method_mod(f, Df, x0, m = 1, tol = 1e-4, nmax = 100, frame = True):
    '''
    Parameters
    ----------
    f : function
        DESCRIPTION.
    Df : function
        DESCRIPTION. the derivative of f
    x0 : float
        DESCRIPTION. Initial estimate
    m: int
        DESCRIPTION. the multiplicity of the root
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
    Dfxn=np.zeros(nmax, dtype=float)
    xn[0] = x0
    for n in range(0,nmax-1):
        fxn[n] = f(xn[n])
        if abs(fxn[n]) < tol:
            Dfxn[n] = Df(xn[n])
            if frame:
                return pd.DataFrame({'xn': xn[:n+1], 'fxn': fxn[:n+1], 'Dfxn': Dfxn[:n+1]})
            else:
                return xn, fxn, Dfxn, n
        Dfxn[n] = Df(xn[n])
        if Dfxn[n] == 0:
            print('Zero derivative. No solution found.')
            return None
        xn[n+1] = xn[n] - m*(fxn[n]/Dfxn[n])
    print('Exceeded maximum iterations. No solution found.')
    return None