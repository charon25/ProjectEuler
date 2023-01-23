def is_palindrome(string):
    return string == string[::-1]

LIMIT = 1_000_000

total = 0

# Only odd numbers can be base 2 palindromes
for n in range(1, LIMIT, 2):
    if is_palindrome(str(n)) and is_palindrome(bin(n)[2:]):
        total += n

print(total)
