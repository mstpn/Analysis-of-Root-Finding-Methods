import pandas as pd
import numpy as np


def steffenson(g, a, b, tol, nmax):
    c0_n = np.zeros(nmax, dtype=float)
    c1_n = np.zeros(nmax, dtype=float)
    c2_n = np.zeros(nmax, dtype=float)
    c_new_n = np.zeros(nmax, dtype=float)
    error_n = np.zeros(nmax, dtype=float)

    n = 0
    c0_n[0] = (a + b) / 2
    for n in range(nmax - 1):
        c1_n[n] = g(c0_n[n])
        c2_n[n] = g(c1_n[n])
        c_new_n[n] = c0_n[n] - (c1_n[n] - c0_n[n])**2 / \
            (c2_n[n] - 2*c1_n[n] + c0_n[n])
        error_n[n] = abs(c_new_n[n] - c0_n[n])
        if abs(c_new_n[n] - c0_n[n]) < tol:
            break
        c0_n[n+1] = c_new_n[n]
    return pd.DataFrame({'n': np.arange(n+1), 'c0': c0_n[0:n+1], 'c1': c1_n[0:n+1], 'c2': c2_n[0:n+1], 'c_new': c_new_n[0:n+1], '|c_new - c0|': error_n[0:n+1]})
