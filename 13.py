with open('13.txt', 'r') as fi:
    numbers = map(int, fi.read().splitlines())

print(str(sum(numbers))[:10])
