from math import factorial

FACTORIALS = {d: factorial(d) for d in range(10)}

def func(n):
    return sum(FACTORIALS[int(d)] for d in str(n))

def chain_length(n):
    chain = set()
    while not n in chain:
        chain.add(n)
        n = func(n)
    
    return len(chain)

LIMIT = 1_000_000
TARGET = 60

count = 0

for n in range(LIMIT + 1):
    if chain_length(n) == TARGET:
        count += 1

print(count)

