import pandas as pd 
import numpy as np

def regula_falsi(f, a, b, Nmax = 1000, TOL = 1e-4, Frame = True):
    '''
    Parameters
    ----------
    f : function 
        DESCRIPTION. A function. Here we use lambda functions
    a : float
        DESCRIPTION. a is the left side of interval [a, b]
    b : float
        DESCRIPTION. b is the right side of interval [a, b]
    TOL : float, optional
        DESCRIPTION. Tolerance (epsilon). The default is 1e-4.
    Frame : bool, optional
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
    an=np.zeros(Nmax, dtype=float)
    bn=np.zeros(Nmax, dtype=float)
    cn=np.zeros(Nmax, dtype=float)
    fcn=np.zeros(Nmax, dtype=float)
    # initial values
    an[0]=a
    bn[0]=b

    for n in range(0,Nmax-1):
        cn[n]= (an[n]*f(bn[n]) - bn[n]*f(an[n])) / (f(bn[n]) - f(an[n]))
        fcn[n]=f(cn[n])
        if f(an[n])*fcn[n] < 0:
            an[n+1]=an[n]
            bn[n+1]=cn[n]
        elif f(bn[n])*fcn[n] < 0:
            an[n+1]=cn[n]
            bn[n+1]=bn[n]
        else:
            print("Regula falsi method fails.")
            return None
        if (abs(fcn[n]) < TOL):
            if Frame:
                return pd.DataFrame({'an': an[:n+1], 'bn': bn[:n+1], 'cn': cn[:n+1], 'fcn': fcn[:n+1]})
            else:
                return an, bn, cn, fcn, n
        
    if Frame:
        return pd.DataFrame({'an': an[:n+1], 'bn': bn[:n+1], 'cn': cn[:n+1], 'fcn': fcn[:n+1]})
    else:
        return an, bn, cn, fcn, n