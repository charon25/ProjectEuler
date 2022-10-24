from math import isqrt

def cont_frac_period_len(n):
    a0 = isqrt(n)
    if n == a0 * a0:
        return 0

    length = 1
    alpha, beta = -a0, 1
    alpha_beta = dict()
    
    while not (alpha, beta) in alpha_beta:
        ALPHA, BETA = alpha, beta
        beta = (n - alpha * alpha) // beta
        a = (-alpha + a0) // beta
        alpha_beta[(ALPHA, BETA)] = length
        alpha = -alpha - a * beta
        length += 1
    
    return length - alpha_beta[(alpha, beta)]

LIMIT = 10_000

print(sum(1 for n in range(1, LIMIT + 1) if cont_frac_period_len(n) % 2 == 1))
