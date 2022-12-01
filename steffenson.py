import math
import pandas as pd


# rewrite this using he np.zeros() array method found in other functions
def steffenson(g, a, b, nmax, tol, df):
    c0 = (a + b) / 2
    for n in range(nmax + 1):
        c1 = g(c0)
        c2 = g(c1)
        c_new = stef_iteration(c0, c1, c2)
        temp_df = pd.DataFrame(data={'n': n, 'c0':c0,'c1':c1,'c2':c2,'c_new':c_new,'|c_new - c0|':abs(c_new - c0)}, index=[0])
        df = pd.concat([df,temp_df], ignore_index=True)
        if abs(c_new - c0) < tol:
            return df
        c0 = c_new
    return df


def stef_iteration(c0, c1, c2):
    return c0 - (c1 - c0)**2 / (c2 - 2*c1 + c0)

def g(x):
    return math.sqrt(x)


# if name main
if __name__ == "__main__":
    df = pd.DataFrame(columns=['n', 'c0', 'c1', 'c2', 'c_new', '|c_new - c0|'])
    df = steffenson(g, 0, 1, 5, 1e-6, df)

    print("\n\nstef\n\n", df)

    lat = df.to_latex()
    print(lat)