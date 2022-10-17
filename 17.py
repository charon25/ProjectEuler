UNITS = {
    0: 0,
    1: 3,
    2: 3,
    3: 5,
    4: 4,
    5: 4,
    6: 3,
    7: 5,
    8: 5,
    9: 4
}

TEENS = {
    10: 3,
    11: 6,
    12: 6,
    13: 8,
    14: 8,
    15: 7,
    16: 7,
    17: 9,
    18: 8,
    19: 8
}

TENS = {
    20: 6,
    30: 6,
    40: 5,
    50: 5,
    60: 5,
    70: 7,
    80: 6,
    90: 6
}

HUNDRED = 7

AND = 3

ONE_THOUSAND = 3 + 8

def letter_count(n):
    if n < 10:
        return UNITS[n]
    
    if n < 20:
        return TEENS[n]
    
    if n < 100:
        return TENS[n - n % 10] + UNITS[n % 10]

    if n == 1000:
        return ONE_THOUSAND
    
    c = n // 100

    if n % 100 == 0:
        return UNITS[c] + HUNDRED
    else:
        return UNITS[c] + HUNDRED + AND + letter_count(n % 100)


print(sum(letter_count(n) for n in range(1, 1000 + 1)))
