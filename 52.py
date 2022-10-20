# Method 1 : know that the repeating part of 1/7 is 142857 and that every x/7 (1 <= x <= 6) has the same digits in its repeating part but not the same order

# Method 2

n = 0
while True:
    n += 1

    multiples = [sorted(str(k * n)) for k in range(1, 7)]
    if all(multiple == multiples[0] for multiple in multiples[1:]):
        break

print(n)
