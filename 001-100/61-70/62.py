def get_smallest_by_length(length: int, target: int):
    MIN_VALUE = 10**(length - 1)
    MAX_VALUE = 10**length

    counter = {}
    min_cube_by_digits = {}

    n = 0
    cube = 0
    while cube < MAX_VALUE:
        n += 1
        cube = n * n * n
        if cube >= MIN_VALUE:
            sorted_digits = tuple(sorted(str(cube)))
            if not sorted_digits in counter:
                counter[sorted_digits] = 0
                min_cube_by_digits[sorted_digits] = cube
            counter[sorted_digits] += 1
    
    min_cube = MAX_VALUE + 1
    for sorted_digits, count in counter.items():
        if count == target:
            min_cube = min(min_cube, min_cube_by_digits[sorted_digits])

    if min_cube > MAX_VALUE:
        return None
    else:
        return min_cube

COUNT = 5

length = 1
while True:
    cube = get_smallest_by_length(length, COUNT)
    if cube:
        break

    length += 1

print(cube)
