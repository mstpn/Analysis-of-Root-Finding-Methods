"""
? Keep dataframe return in calculation?
    yes
? Balanced ranges (i.e. {-1,1} and {0,2} are same range, but not symmetric)
    balanced
? Coefficients for degrees (x^2 vs 100x^2)
    yes
? Trailing terms in degrees (x^3 vs x^3 + x^2 + x)
    no
? Tolerance
    1E-10
? nmax
    1000
? Where to time (in function or outside)
    outside

 """

import bisection
import bisection_mod
import bisection_nmax
import fixed_point
import newton_method_mod
import newton_method
import secant_method
import regula_falsi
import steffenson

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

""" 
TODO: Add a function that generates test case functions and stores them in an array
3d array:
    1st dimension: degree
    2nd dimension: coefficient
    3rd dimension: range

"""

# return a function that is a polynomial of degree with a coefficient

# generate a random polynomial of degree with a coefficient
# def generate_random_polynomial(degree, coefficient):
#     def f(x):
#         return coefficient * (x+np.random.randint(-100,100))**degree + np.random.randint(-100, 100)
#     return f
def generate_polynomial(degree, coefficient):
    def f(x):
        return coefficient * x**degree + x
    return f

# return a function that is a polynomial of degree with a coefficient, x and y offsets
def generate_polynomial_offset(degree, coefficient, x_offset, y_offset):
    def f(x):
        return coefficient * (x+x_offset)**degree + y_offset
    return f

# return a function that is the derivative of a polynomial of degree with a coefficient
def generate_derivative(degree, coefficient):
    def f(x):
        if degree - 1 < 0:
            return None
        return coefficient * degree * x**(degree - 1)
    return f

# return a function that is the second derivative of a polynomial of degree with a coefficient
def generate_second_derivative(degree, coefficient):
    def f(x):
        if degree - 2 < 0:
            return None
        return coefficient * degree * (degree - 1) * x**(degree - 2)
    return f


"""
TODO: Create a function that tests runs the test suite on each function
store functions in array?
Use helper function that knows what parameters to pass to each function
    how? 
        do we just use write each one manually?
need to time run of the function and store it in an array of dicts?
    dict: {concat(function_name, degree, coefficient, range): time}

    orrrrr
        we have the 3d array of test cases, but they are actually dicts
            we have the key be the case, then the value is an array of dicts
                dict: {function_name: time}

"""

NMAX = 1000
TOL = 1E-10
FRAME = True
# range = 10^steps
RANGE_STEPS = 5
# coefficient = 10^steps
COEF_STEPS = 5
DEGREE_STEPS = 5
NUM_RUNS = 100


# TODO: change the range, coeff, degree steps to be calculated ahead of time and passed in??

# Main function
if __name__ == "__main__":
    # {method: {range#: {degree#: {coefficient#: [time, #iterations]}}}}
    results = {}

    # BISECTION
    # ! We need to step degree to be only odd numbers
    # TODO: apply this for all methods
    
    print("=========================================")
    print("\tBISECTION")
    print("=========================================")
    results["bisection"] = bisection.test(
        NMAX, TOL, FRAME, RANGE_STEPS, COEF_STEPS, DEGREE_STEPS, NUM_RUNS)

    # BISECTION MOD
    print("=========================================")
    print("\tBISECTION MOD")
    print("=========================================")
    results["bisection_mod"] = bisection_mod.test(
        TOL, FRAME, RANGE_STEPS, COEF_STEPS, DEGREE_STEPS, NUM_RUNS)



    # Coefficient vs Time graphs
    for method in results:
        for bounds in results[method]:
            for degree in results[method][bounds]:
                xpoints = np.array([])
                ypoints = np.array([])
                for coefficient in results[method][bounds][degree]:
                    xpoints = np.append(xpoints, coefficient)
                    ypoints = np.append(
                        ypoints, results[method][bounds][degree][coefficient][0])
                plt.plot(xpoints, ypoints, label="degree: " + str(degree))
            plt.legend()
            plt.xlabel("Coefficient")
            plt.ylabel("Time (ns)")
            plt.title(str(method).capitalize() + ": Bounds " + str(bounds))
            plt.xscale("log")
            plt.show()

            # print(method, bounds, degree, coefficient,
            #       results[method][bounds][degree][coefficient])
