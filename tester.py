"""
? Keep dataframe return in calculation?
? Balanced ranges (i.e. {-1,1} and {0,2} are same range, but not symmetric)
? Coefficients for degrees (x^2 vs 100x^2)
? Trailing terms in degrees (x^3 vs x^3 + x^2 + x)
? Tolerance
? nmax
? Where to time (in function or outside)

 """

from bisection import bisection
from bisection_mod import bisection_mod
from bisection_nmax import bisection_nmax
from fixed_point import fixed_point
from newton_method_mod import newton_method_mod
from newton_method import newton_method
from secant_method import secant_method
from regula_falsi import regula_falsi
from steffenson import steffenson

import numpy as np
import pandas as pd

""" 
TODO: Add a function that generates test case functions and stores them in an array
3d array:
    1st dimension: degree
    2nd dimension: coefficient
    3rd dimension: range

"""
# def generate_test_cases(max_range, max_degree, max_coefficient) -> tuple(list, list):
#     ranges = []
#     for i in range(max_range):
#         ranges.append([-i, i])
    
# return a function that is a polynomial of degree, coefficeint with a given number of terms
def generate_function(degree, coefficient, terms):
    def f(x):
        sum = 0
        for i in range(terms):
            sum += coefficient * x**(degree - i)
        return sum
    return f

# return a function that is the derivative of a polynomial of degree, coefficeint with a given number of terms
def generate_derivative(degree, coefficient, terms):
    def f(x):
        sum = 0
        for i in range(terms):
            if degree - i - 1 < 0:
                break
            sum += coefficient * (degree - i) * x**(degree - i - 1)
        return sum
    return f

# return a function that is the second derivative of a polynomial of degree, coefficeint with a given number of terms
def generate_second_derivative(degree, coefficient, terms):
    def f(x):
        sum = 0
        for i in range(terms):
            if degree - i - 2 < 0:
                break
            sum += coefficient * (degree - i) * (degree - i - 1) * x**(degree - i - 2)
        return sum
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




# Main function
if __name__ == "__main__":
    pass

