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

TODO: Citations
    professors code
    course notes
    matplotlib docs
    pandas docs
    https://en.wikipedia.org/wiki/Secant_method#Computational_example
    https://en.wikipedia.org/wiki/Bisection_method#Algorithm
    https://docs.python.org/3/library/csv.html
        or maybe just use the python docs mainpage

?: Change degree from odd to powers of 10 like coefficient/bounds
    use the y offset to make sure the function has values on either side of x-axis
"""