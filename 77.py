with open('primes.txt', 'r') as fi:
    primes = list(map(int, fi.read().splitlines()))

def count_ways(LIMIT, coins):
    ways = [0 for _ in range(LIMIT + 1)]
    ways[0] = 1

    for coin in coins:
        if coin > LIMIT:
            break
        for i in range(coin, LIMIT + 1):
            ways[i] = ways[i - coin] + ways[i]
    
    return ways[LIMIT]

TARGET = 5000

n = 1
while True:
    n += 1
    ways = count_ways(n, primes)
    if ways > TARGET:
        break

print(n)
