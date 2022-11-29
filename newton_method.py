import pandas as pd 
import numpy as np

def newton_method(f, Df, x0, TOL = 1e-4, Nmax = 100, Frame = True):
    '''
    Parameters
    ----------
    f : function
        DESCRIPTION.
    Df : function
        DESCRIPTION. the derivative of f
    x0 : float
        DESCRIPTION. Initial estimate
    TOL : TYPE, optional
        DESCRIPTION. Tolerance (epsilon). The default is 1e-4.
    Nmax : Int, optional
        DESCRIPTION. Maximum number of iterations. The default is 100.
    Frame : bool, optional
        DESCRIPTION. If it is true, a dataframe will be returned. The default is True.

    Returns
    -------
    xn, fxn, Dfxn, n
    or
    a dataframe

    '''

    xn=np.zeros(Nmax, dtype=float)
    fxn=np.zeros(Nmax, dtype=float)
    Dfxn=np.zeros(Nmax, dtype=float)
    xn[0] = x0
    for n in range(0,Nmax-1):
        fxn[n] = f(xn[n])
        if abs(fxn[n]) < TOL:
            Dfxn[n] = Df(xn[n])
            if Frame:
                return pd.DataFrame({'xn': xn[:n+1], 'fxn': fxn[:n+1], 'Dfxn': Dfxn[:n+1]})
            else:
                return xn, fxn, Dfxn, n
        Dfxn[n] = Df(xn[n])
        if Dfxn[n] == 0:
            print('Zero derivative. No solution found.')
            return None
        xn[n+1] = xn[n] - fxn[n]/Dfxn[n]
    print('Exceeded maximum iterations. No solution found.')
    return None