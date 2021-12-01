import numpy as np

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]
    lines = np.array(list(map(int, lines)))

sums = np.array([np.sum(lines[i:i + 3]) for i in range(len(lines) - 2)])
diff = sums[1:] - sums[:-1]
print(len([x for x in diff if x > 0]))
