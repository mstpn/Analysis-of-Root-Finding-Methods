# parses polynomials of the form a0 + a1*x^1 + a2*x^2 + ... + an*x^n
def parse_degree_str(poly_str):
    split_by_degree = poly_str.split('x^')
    degrees = [0]
    for term in split_by_degree:
        degree = 0
        for ch in term:
            if ch.isnumeric():
                degree = degree * 10 + int(ch)
            else:
                break
        degrees.append(degree)
    return max(degrees)

if __name__ == "__main__":
    deg1 = 'x^1'
    deg2 = 'x^1 + x^2'
    deg3 = '3 + 4x^x + 5x^2 +16x^3'

    print(parse_degree_str(deg1))
    print(parse_degree_str(deg2))
    print(parse_degree_str(deg3))

def algo(coef, degree, range):
    pass
    # some switch/if statements for these

    # highest impact factor is the degree of the polynomial
    # second highest impact factor is the range of the polynomial
    # third highest impact factor is the coefficient of the polynomial

    # we make decisions based on the highest impact factor
    # our algorithm looks for cases to subvert this order of importance