LIMIT = 100

coins = list(range(1, LIMIT))


ways = [0 for _ in range(LIMIT + 1)]
ways[0] = 1

for coin in coins:
    for i in range(coin, LIMIT + 1):
        ways[i] = ways[i - coin] + ways[i]

print(ways[LIMIT])
