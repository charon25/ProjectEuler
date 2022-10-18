# Obviously less than 6 digits because 10^6 > 6 * 9^5

def sum_digit_fifth_power(n):
    total = 0
    for c in str(n):
        total += int(c) ** 5
    return total

total = 0

for n in range(10, 5 * (9 ** 5) + 1):
    if n == sum_digit_fifth_power(n):
        print(n)
        total += n

print(total)
