def roman_sub(n, c10, c5, c1):
    if n == 9:
        return c1 + c10
    elif n == 4:
        return c1 + c5
    elif n >= 5:
        return c5 + c1 * (n % 5)
    else:
        return c1 * (n % 5)

def to_roman(n: int):
    m, c, d, u = map(int, str(n).zfill(4))

    return 'M' * m + roman_sub(c, 'M', 'D', 'C') + roman_sub(d, 'C', 'L', 'X') + roman_sub(u, 'X', 'V', 'I')

VALUES = {'': 0, 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

def from_roman(roman: str):
    chars = list(roman)
    index = 0
    while index < len(roman) - 1:
        if VALUES[chars[index]] < VALUES[chars[index + 1]]:
            chars[index + 1] = chars[index] + chars[index + 1]
            chars[index] = ''
            index += 1

        index += 1
    
    return sum(VALUES[char] for char in chars)

with open('89.txt', 'r') as fi:
    romans = fi.read().splitlines()

total = 0

for roman in romans:
    total += len(roman) - len(to_roman(from_roman(roman)))

print(total)
