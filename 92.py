LIMIT = 10_000_000#_000

memoisation = {}

def stops_at_89(n):
    global memoisation
    visited = [n]
    value = None
    flag = False
    while True:
        if n in memoisation:
            flag = True
            value = memoisation[n]
        elif n == 1:
            flag = True
            value = False
        elif n == 89:
            flag = True
            value = True
        if flag:
            for k in visited:
                memoisation[k] = value
            return value

        n = sum(int(c) ** 2 for c in str(n))
        visited.append(n)

print(sum([stops_at_89(n) for n in range(1, LIMIT + 1)]))
