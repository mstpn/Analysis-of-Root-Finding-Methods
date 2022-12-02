import pandas as pd 
import numpy as np

def regula_falsi(f, a, b, tol = 1e-4, nmax = 1000, frame = True):
    '''
    Parameters
    ----------
    f : function 
        DESCRIPTION. A function. Here we use lambda functions
    a : float
        DESCRIPTION. a is the left side of interval [a, b]
    b : float
        DESCRIPTION. b is the right side of interval [a, b]
    tol : float, optional
        DESCRIPTION. Tolerance (epsilon). The default is 1e-4.
    frame : bool, optional
        DESCRIPTION. If it is true, a dataframe will be returned. The default is True.

    Returns
    -------
    an, bn, cn, fcn, n
    or
    a dataframe
    '''
    
    if f(a)*f(b) >= 0:
        print("Regula falsi method is inapplicable .")
        return None
    
    # let c_n be a point in (a_n, b_n)
    an=np.zeros(nmax, dtype=float)
    bn=np.zeros(nmax, dtype=float)
    cn=np.zeros(nmax, dtype=float)
    fcn=np.zeros(nmax, dtype=float)
    # initial values
    an[0]=a
    bn[0]=b

    n=0
    for n in range(0,nmax-1):
        cn[n]= (an[n]*f(bn[n]) - bn[n]*f(an[n])) / (f(bn[n]) - f(an[n]))
        fcn[n]=f(cn[n])
        # need to check if fcn[n] is zero first
        if (abs(fcn[n]) < tol):
            if frame:
                return pd.DataFrame({'an': an[:n+1], 'bn': bn[:n+1], 'cn': cn[:n+1], 'fcn': fcn[:n+1]})
            else:
                return an, bn, cn, fcn, n
        if f(an[n])*fcn[n] < 0:
            an[n+1]=an[n]
            bn[n+1]=cn[n]
        elif f(bn[n])*fcn[n] < 0:
            an[n+1]=cn[n]
            bn[n+1]=bn[n]
        else:
            print("Regula falsi method fails.")
            return None
        
    if frame:
        return pd.DataFrame({'an': an[:n+1], 'bn': bn[:n+1], 'cn': cn[:n+1], 'fcn': fcn[:n+1]})
    else:
        return an, bn, cn, fcn, n