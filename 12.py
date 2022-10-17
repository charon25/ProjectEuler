from math import isqrt

def divisor_count(n):
    count = 0
    sqrt_n = isqrt(n)
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            count += 2
    
    if n == sqrt_n * sqrt_n:
        count -= 1
    
    return count

# According to OEIS (A063440), it is not under n = 10000

n = 10000
while True:
    tn = (n * (n + 1)) // 2
    divisors = divisor_count(tn)
    if divisors > 500:
        print(tn)
        break
    
    n += 1
