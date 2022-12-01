import pandas as pd 
import numpy as np
import tester
from time import time_ns

def test(tol, frame, range_steps, coef_steps, degree_steps, num_runs):
    # result_dict = {range#: {degree#: {coefficient#: [time, #iterations]}}}
    result_dict = {}
    for abs_range in (10**x for x in range(1, range_steps+1)):
        result_dict[abs_range] = {}
        for degree in (2*x + 1 for x in range(0, degree_steps)):
            result_dict[abs_range][degree] = {}
            for coef in (10**x for x in range(0, coef_steps)):
                print(
                    f"abs_range: {abs_range}, degree: {degree}, coef: {coef}")
                # f = generate_polynomial(degree, coef)
                elapsed_time = 0
                num_iterations = 0
                for i in range(0, num_runs):  
                    f = tester.generate_polynomial_offset(degree, coef,np.random.randint(-abs_range+1, abs_range-1),0)
                    start = time_ns()
                    result = bisection_mod(
                        f, -abs_range, abs_range+1, tol, frame)
                    end = time_ns()
                    if result is not None:
                        # store time in nanoseconds
                        elapsed_time += (end - start)
                        # store number of iterations
                        num_iterations += len(result) - 1
                # store result
                avg_time = elapsed_time/num_runs
                avg_iterations = num_iterations/num_runs
                result_dict[abs_range][degree][coef] = [avg_time, avg_iterations]
    return result_dict


def bisection_mod(f, a, b, tol = 1e-4, frame = True):
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
        print("Bisection method is inapplicable .")
        return None
    
    # let c_n be a point in (a_n, b_n)
    nmax= int(np.ceil(np.log2(np.abs(b-a)/tol)))+2
    an=np.zeros(nmax, dtype=float)
    bn=np.zeros(nmax, dtype=float)
    cn=np.zeros(nmax, dtype=float)
    fcn=np.zeros(nmax, dtype=float)
    # initial values
    an[0]=a
    bn[0]=b

    n=0
    for n in range(0, nmax-1):
        cn[n]=(an[n] + bn[n])/2
        fcn[n]=f(cn[n])
        if f(an[n])*fcn[n] < 0:
            an[n+1]=an[n]
            bn[n+1]=cn[n]
        elif f(bn[n])*fcn[n] < 0:
            an[n+1]=cn[n]
            bn[n+1]=bn[n]
        else:
            print("Bisection method fails.")
            return None
        if (abs(fcn[n]) < tol):
            if frame:
                return pd.DataFrame({'an': an[:n+1], 'bn': bn[:n+1], 'cn': cn[:n+1], 'fcn': fcn[:n+1]})
            else:
                return an, bn, cn, fcn, n
        
    if frame:
        return pd.DataFrame({'an': an[:n+1], 'bn': bn[:n+1], 'cn': cn[:n+1], 'fcn': fcn[:n+1]})
    else:
        return an, bn, cn, fcn, n