import numpy as np

with open("input.txt") as f:
    coords = [x.strip().split("->") for x in f.readlines()]
    coords = [([int(x) for x in a.split(",")], [int(x) for x in b.split(",")]) for a, b in coords]
    coords = np.array(coords)

grid = np.zeros((2, coords[:, :, 1].max() + 1, coords[:, :, 0].max() + 1))

for a, b in coords:
    d = np.sign(b - a)
    while not np.array_equal(a, b + d):
        grid[np.prod(d), a[0], a[1]] += 1
        a += d

print(np.count_nonzero(grid[0] > 1))
print(np.count_nonzero(grid.sum(0) > 1))
