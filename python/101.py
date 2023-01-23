def lagrange(u: int, x: list[int], y: list[int]):
    n = len(x)
    v = 0

    for i in range(n):
        l_i = 1
        for j in range(n):
            if j == i:
                continue
            l_i *= (u - x[j]) / (x[i] - x[j])
        v += y[i] * l_i
    
    return v

def polynome(x0):
    y = 1
    sign = -1
    x = x0
    for i in range(10):
        y += x * sign
        sign *= -1
        x *= x0

    return y

DEGREE = 10

x = list(range(1, DEGREE + 1))
y = [polynome(v) for v in x]

total = 0

for n in range(1, DEGREE + 1):
    fit = round(lagrange(n + 1, x[:n], y[:n]), 0)
    total += fit

print(int(total))
