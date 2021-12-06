import numpy as np


def part1(values: [[int]]) -> int:
    gamma = values.mean(axis=0).round()
    epsilon = 1 - gamma
    return _to_decimal(gamma) * _to_decimal(epsilon)


def part2(values: [[int]]) -> int:
    def _round_up(value: int):
        return 1 if value == 0.5 else round(value)

    gamma = values
    epsilon = values

    for i in range(len(values[0])):
        if len(gamma) == 1:
            break

        common = _round_up(gamma.mean(axis=0)[i])
        gamma = gamma[gamma[:, i] == common]

    for i in range(len(values[0])):
        if len(epsilon) == 1:
            break

        common = 1 - _round_up(epsilon.mean(axis=0)[i])
        epsilon = epsilon[epsilon[:, i] == common]

    return _to_decimal(gamma) * _to_decimal(epsilon)


def _to_decimal(bit_list: [int]) -> int:
    return int(bit_list.dot(2 ** np.arange(bit_list.size)[::-1]))


with open("input.txt") as f:
    contents = f.read().split("\n")
    puzzle_input = np.array([np.array([int(digit) for digit in row]) for row in contents if row])

print("Part 1: ", part1(puzzle_input))
print("Part 2: ", part2(puzzle_input))
