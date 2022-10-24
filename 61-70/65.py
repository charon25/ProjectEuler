def coeff_cont_frac(n):
    if n == 0:
        return 2
    if n % 3 == 2:
        return 2 * (1 + n // 3)

    return 1

def cont_frac(N):
    alpha, beta = coeff_cont_frac(N), 1
    for k in range(N - 1, -1, -1):
        alpha, beta = alpha * coeff_cont_frac(k) + beta, alpha
    
    return (alpha, beta)

N = 100

print(sum(map(int, str(cont_frac(N - 1)[0]))))
