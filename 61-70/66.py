# Algorithm taken from https://fr.wikipedia.org/wiki/%C3%89quation_de_Pell-Fermat#Fraction_continue

from math import isqrt

def cont_frac_coeffs(n):
    a0 = isqrt(n)

    alpha, beta = -a0, 1
    coeffs = list()
    alpha_beta = set()
    
    while not (alpha, beta) in alpha_beta:
        alpha_beta.add((alpha, beta))
        beta = (n - alpha * alpha) // beta
        a = (-alpha + a0) // beta
        coeffs.append(a)
        alpha = -alpha - a * beta
    
    if len(coeffs) % 2 == 1 and len(coeffs) > 1:
        p = len(coeffs)
        while len(coeffs) < 2 * p - 1:
            beta = (n - alpha * alpha) // beta
            a = (-alpha + a0) // beta
            coeffs.append(a)
            alpha = -alpha - a * beta
    elif len(coeffs) % 2 == 0:
        coeffs.pop()

    coeffs.insert(0, a0)
    return coeffs

def cont_frac(n):
    coeffs = cont_frac_coeffs(n)
    N = len(coeffs)
    alpha, beta = coeffs[N - 1], 1
    for k in range(N - 2, -1, -1):
        alpha, beta = alpha * coeffs[k] + beta, alpha
    
    return (alpha, beta)

LIMIT = 1000

print(max([D for D in range(2, LIMIT + 1) if isqrt(D)**2 != D], key=lambda D:cont_frac(D)[0]))
