KEY_LENGTH = 3

def get_all_keys():
    ord_alphabet = [ord(c) for c in 'abcdefghijklmnopqrstuvwxyz']
    for c1 in ord_alphabet:
        for c2 in ord_alphabet:
            for c3 in ord_alphabet:
                yield (c1, c2, c3)

with open('59.txt', 'r') as fi:
    numbers = list(map(int, fi.read().split(',')))

length = len(numbers)

for key in get_all_keys():
    decrypted = [n ^ key[k % KEY_LENGTH] for k, n in enumerate(numbers)]
    message = ''.join(map(chr, decrypted)).lower()
    if message.count('e') > 0.1 * length and max(decrypted) <= 122:
        break

print(sum(decrypted))
