def is_move_valid(grid, x, y, value):
    if value in grid[y]:
        return False

    if any(grid[yy][x] == value for yy in range(9)):
        return False

    xbox, ybox = x // 3, y // 3
    for yy in range(3 * ybox, 3 * (ybox + 1)):
        for xx in range(3 * xbox, 3 * (xbox + 1)):
            if grid[yy][xx] == value:
                return False

    return True

def print_grid(grid):
    print('===')
    for k, row in enumerate(grid):
        for j, cell in enumerate(row):
            print(cell, end='')
            if j % 3 == 2:
                print(' ', end='')
        print()
        if k % 3 == 2 and k < 8:
            print()
    print('===')

def solve_sudoku(grid: list[list[int]]):
    cells = []
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                cells.append((x, y))

    tested = {cell: 0 for cell in cells}
    index = 0
    cell = cells[0]

    while index < len(cells):
        cell = cells[index]

        while tested[cell] == 9:
            tested[cell] = 0
            grid[y][x] = 0
            index -= 1
            x, y = cell = cells[index]

        x, y = cell = cells[index]
        grid[y][x] = 0
        value = tested[cell] + 1
        if is_move_valid(grid, x, y, value):
            grid[y][x] = value
            tested[cell] = value
            index += 1
        else:
            tested[cell] = value
    
    return grid


with open('96.txt', 'r') as fi:
    grids: list[list[str]] = []
    for line in fi:
        if line.startswith('Grid'):
            grids.append([])
        else:
            grids[-1].append(line.strip())
    
for i in range(len(grids)):
    grid = grids[i]
    grid = [list(map(int, row)) for row in grid]
    grids[i] = grid


total = 0

for grid in grids:
    solved_grid = solve_sudoku(grid)
    total += 100 * grid[0][0] + 10 * grid[0][1] + grid[0][2]

print(total)
