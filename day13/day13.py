import numpy as np

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]
    i = lines.index("")
    coordinates = np.array([[int(y) for y in x.split(",")] for x in lines[:i]])
    input_instructions = [(x[11], int(x[13:])) for x in lines[i + 1:]]
    input_grid = np.zeros((max(coordinates[:, 1]) + 1, max(coordinates[:, 0]) + 1))
    for x, y in coordinates:
        input_grid[y, x] = 1


def solve_a(grid, instruction):
    axis, val = instruction

    if axis == "x":
        grid = grid.transpose()

    grid_f = np.flipud(grid[val + 1:val * 2 + 1])
    grid = grid[0:val]
    grid[val - len(grid_f):] += grid_f

    if axis == "x":
        grid = grid.transpose()

    return grid, np.count_nonzero(grid)


def solve_b(grid, instructions):
    for instruction in instructions:
        grid, _ = solve_a(grid, instruction)

    return grid


def print_grid(grid):
    for y in grid:
        for x in y:
            print("#" if x else ".", end="")
        print()


print(solve_a(input_grid, input_instructions[0])[1])
print_grid(solve_b(input_grid, input_instructions))
