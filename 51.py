with open('primes.txt', 'r') as fi:
    primes = list(map(int, fi.read().splitlines()))

TWO_POWERS = [tuple(bin(n)[2:].zfill(k) for n in range(1, 2**k) if bin(n).count('1') != 1) for k in range(20)]
def get_min_by_length(LENGTH):
    models_primes: dict[str, list] = {}

    for prime in primes:
        if prime >= 10**LENGTH or prime < 10**(LENGTH - 1):
            continue

        prime_str = str(prime)
        length = len(prime_str) - 1
        models = []
        for perm in TWO_POWERS[length]:
            # print(perm)
            if len(set(c for k, c in enumerate(prime_str[:-1]) if perm[k] == '1')) == 1:
                models.append(''.join(c if perm[k] == '0' else '*' for k, c in enumerate(prime_str[:-1])) + prime_str[-1])

        models.extend(prime_str[:l] + '*' + prime_str[l+1:] for l in range(length))
        
        for model in models:
            if not model in models_primes:
                models_primes[model] = []
            models_primes[model].append(prime)

    for model, models_primes in models_primes.items():
        if len(models_primes) >= COUNT:
            return min(models_primes)
    
    return None


COUNT = 8

length = 2
min_prime = None
while not min_prime:
    min_prime = get_min_by_length(length)
    length += 1
    
print(min_prime)
