"""Main solution file: Day 9."""

import os
from typing import List

INPUT_FILE = 'input.txt'

UP = [-1, 0]
RIGHT = [0, 1]
DOWN = [1, 0]
LEFT = [0, -1]


def part_1():
    """Return risk level of heatmap."""
    input = _load_input()
    adjacent_dirs = [UP, DOWN, LEFT, RIGHT]
    rows = len(input)
    cols = len(input[0])

    low_points = list()

    for row in range(rows):
        for i in range(cols):
            num = input[row][i]
            adjacent_vals = list()

            for ad in adjacent_dirs:
                new_row = row + ad[0]
                new_col = i + ad[1]

                if 0 <= new_row < rows and 0 <= new_col < cols:
                    val = input[new_row][new_col]
                    adjacent_vals.append(val)

            if all(adj > num for adj in adjacent_vals):
                low_points.append(num)

    return sum(low_points) + len(low_points)


def _load_input() -> List[List[int]]:
    """Load input data from text file."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), INPUT_FILE)
    f = open(filepath, 'r')
    data = f.read()
    f.close()

    raw_input = data.strip().split('\n')
    return [[int(i) for i in input] for input in raw_input]


print(part_1())   # 541

