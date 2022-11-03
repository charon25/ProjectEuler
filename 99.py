from math import log

with open('99.txt', 'r') as fi:
    lines = fi.read().splitlines()

def log_line(index):
    global lines
    base, exp = map(int, lines[index].split(','))

    return exp * log(base)

# The 1 compensates the 0-indexing
print(1 + max(range(len(lines)), key=log_line))
