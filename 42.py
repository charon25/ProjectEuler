with open('42.txt', 'r') as fi:
    words = fi.read().split(',')

def word_value(word):
    return sum(ord(c) - 64 for c in word) # 64 = ord('A') - 1

# Method 1

from math import sqrt

total = 0

for word in words:
    value = word_value(word)
    n = (-1 + sqrt(8 * value + 1)) / 2
    if n % 1 == 0:
        total += 1

print(total)

# Method 2

max_value = max(word_value(word) for word in words)

triangular_numbers = []
t = 0
n = 1
while t < max_value:
    t += n
    n += 1
    triangular_numbers.append(t)

total = sum(word_value(word) in triangular_numbers for word in words)
print(total)
