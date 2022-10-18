with open('22.txt', 'r') as fi:
    names = fi.read().split(',')

def value(string):
    return sum(ord(c) - 64 for c in string) # 64 = ord('A') - 1

names.sort()

print(sum(k * value(name) for k, name in enumerate(names, start=1)))
