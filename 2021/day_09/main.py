"""Main solution file: Day 9."""

from numpy import prod
import os
from typing import List


ADJACENT_DIRS = {
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
    'up': [-1, 0]
}
INPUT_FILE = 'input.txt'


def part_1() -> int:
    """Return risk level of heatmap."""
    input = _load_input()
    rows = len(input)
    cols = len(input[0])

    low_points = list()

    for row in range(rows):
        for i in range(cols):
            num = input[row][i]
            adjacent_vals = list()

            for ad in ADJACENT_DIRS.values():
                new_row = row + ad[0]
                new_col = i + ad[1]

                if 0 <= new_row < rows and 0 <= new_col < cols:
                    val = input[new_row][new_col]
                    adjacent_vals.append(val)

            if all(adj > num for adj in adjacent_vals):
                low_points.append(num)

    return sum(low_points) + len(low_points)


def part_2() -> int:
    """Return product of three largest basins."""
    input = _load_input()
    rows = len(input)
    cols = len(input[0])

    points_seen = [[False] * cols for _ in range(cols)]

    basin_sizes = list()

    for row in range(rows):
        for col in range(cols):
            basin_size = _depth_first_search(
                col,
                cols,
                input,
                points_seen,
                row,
                rows
            )
            basin_sizes.append(basin_size)

    sorted_basins = sorted(basin_sizes, reverse=True)
    top_three = sorted_basins[:3]
    return prod(top_three)


def _depth_first_search(
    col: int,
    cols: int,
    input: List[List[int]],
    points_seen: List[List[bool]],
    row: int,
    rows: int
) -> int:
    """Recursively use depth-first search to find basin size.

    Args:
        col (int): current column in row of input
        cols (int): total columns in row of input
        input (matrix): heatmap as a matrix
        points_seen (matrix): track whether input coordinate has been evaluated
        row (int): current row in input
        row (int): total rows in input
    """
    if not (0 <= row < rows and 0 <= col < cols):
        return 0

    if points_seen[row][col]:
        return 0

    if input[row][col] == 9:
        return 0

    points_seen[row][col] = True
    basin_size = 1

    for ad in ADJACENT_DIRS.values():
        new_row = row + ad[0]
        new_col = col + ad[1]
        basin_size += _depth_first_search(
            new_col,
            cols,
            input,
            points_seen,
            new_row,
            rows
        )

    return basin_size


def _load_input() -> List[List[int]]:
    """Load input data from text file."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), INPUT_FILE)
    f = open(filepath, 'r')
    data = f.read()
    f.close()

    raw_input = data.strip().split('\n')
    return [[int(i) for i in input] for input in raw_input]


# print(part_1())   # 541
# print(part_2())   # 847504
