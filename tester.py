# File imports
import bisection
import bisection_mod
import bisection_nmax
import fixed_point
import newton_method_mod
import newton_method
import secant_method
import regula_falsi
import steffenson

# Library imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from time import time_ns
import csv

# Constants
NMAX = 1000
TOL = 1E-10
FRAME = True
# range = 10^steps
RANGE_STEPS = 5
# coefficient = 10^steps
COEF_STEPS = 5
DEGREE_STEPS = 5
NUM_RUNS = 100
METHODS = [
    "bisection",
    "bisection_mod",
    # "fixed_point",
    # "newton_method_mod",
    # "newton_method",
    # "secant_method",
    # "regula_falsi",
    # "steffenson"
]


def generate_polynomial_offset(degree, coefficient, x_offset, y_offset):
    """
    Returns a function that is a polynomial of degree with a coefficient, x and y offsets
    """
    def f(x):
        return coefficient * (x+x_offset)**degree + y_offset
    return f


def generate_derivative(degree, coefficient):
    """
    Returns a function that is the derivative of a polynomial of degree with a coefficient
    """
    def f(x):
        if degree - 1 < 0:
            return None
        return coefficient * degree * x**(degree - 1)
    return f


def generate_second_derivative(degree, coefficient):
    """ 
    Returns a function that is the second derivative of a polynomial of degree with a coefficient
    """
    def f(x):
        if degree - 2 < 0:
            return None
        return coefficient * degree * (degree - 1) * x**(degree - 2)
    return f


def test(method, nmax, tol, frame, range_steps, coef_steps, degree_steps, num_runs):
    """
    Test a method with a range of functions

    Parameters:
        method: method to test
        nmax: maximum number of iterations
        tol: tolerance
        frame: whether to return dataframe
        range_steps: number of steps to take in range
        coef_steps: number of steps to take in coefficient
        degree_steps: number of steps to take in degree
        num_runs: number of runs to average

    return dictionary format
        {range#: {degree#: {coefficient#: [time, #iterations]}}}
    """

    result_dict = {}
    for abs_range in (10**x for x in range(1, range_steps+1)):
        result_dict[abs_range] = {}
        for degree in (2*x + 1 for x in range(0, degree_steps)):
            result_dict[abs_range][degree] = {}
            for coef in (10**x for x in range(0, coef_steps)):
                print(
                    f"abs_range: {abs_range}, degree: {degree}, coef: {coef}")
                elapsed_time = 0
                num_iterations = 0
                valid_runs = 0
                for i in range(0, num_runs):
                    abs_offset = 10
                    x_offset = np.random.randint(-abs_offset, abs_offset)
                    y_offset = 0
                    f = generate_polynomial_offset(
                        degree, coef, x_offset, y_offset)
                    # ===timing starts here===
                    start = time_ns()
                    result = method_test(
                        method, f, abs_range, nmax, tol, frame)
                    end = time_ns()
                    # ===timing ends here===
                    if result is not None:
                        # store time in nanoseconds
                        elapsed_time += (end - start)
                        # store number of iterations
                        num_iterations += len(result) - 1
                        valid_runs += 1
                # store result
                if valid_runs > 0:
                    avg_time = elapsed_time / valid_runs
                    avg_iterations = num_iterations / valid_runs
                    result_dict[abs_range][degree][coef] = [
                        avg_time, avg_iterations]
    return result_dict


def method_test(name, f, abs_range, nmax, tol, frame):
    """
    Test a specific method

    Parameters:
        name: name of module to test
        f: function to test
        abs_range: absolute range ofTODO: Writeup function
        nmax: maximum number of iterations
        tol: tolerance
        frame: whether to return dataframe
    """

    if name not in METHODS:
        print("Method not found")
    elif name == "bisection":
        return bisection.bisection(f, -abs_range, abs_range+1, nmax, tol, frame)
    elif name == "bisection_mod":
        return bisection_mod.bisection_mod(f, -abs_range, abs_range+1, tol, frame)
    elif name == "fixed_point":
        pass
    elif name == "newton_method_mod":
        pass
    elif name == "newton_method":
        pass
    elif name == "secant_method":
        pass
    elif name == "regula_falsi":
        pass
    elif name == "steffenson":
        pass
    return None


if __name__ == "__main__":
    """
    Main function
    """

    # =====================================
    #              Calculation
    # =====================================

    # {method: {range#: {degree#: {coefficient#: [time, #iterations]}}}}
    results = {}
    for method in METHODS:
        print("\n\n\n=========================================")
        print(f"\t{method}")
        print("\n=========================================")
        results[method] = test(
            method, NMAX, TOL, FRAME, RANGE_STEPS, COEF_STEPS, DEGREE_STEPS, NUM_RUNS)

    # =====================================
    #              Graphing
    # TODO: save graphs to file
    # =====================================

    # Coefficient vs. Time
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

    # =====================================
    #              Data Output
    # =====================================
    # Modified from:
    # https://stackoverflow.com/questions/29400631/python-writing-nested-dictionary-to-csv
    fields = ['Method', 'Bounds', 'Degree',
              'Coefficient', 'Time', 'Iterations']
    with open("results_output.csv", "w", newline='') as f:
        w = csv.DictWriter(f, fields)
        w.writeheader()
        for method in results:
            for bounds in results[method]:
                for degree in results[method][bounds]:
                    for coefficient in results[method][bounds][degree]:
                        w.writerow({
                            'Method': method,
                            'Bounds': bounds,
                            'Degree': degree,
                            'Coefficient': coefficient,
                            'Time': results[method][bounds][degree][coefficient][0],
                            'Iterations': results[method][bounds][degree][coefficient][1]
                        })
