"""Day 04: Main solution file."""

import os
from typing import List

INPUT_FILE = 'input.txt'

DIRS = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
    'up_left': [-1, -1],
    'up_right': [-1, 1],
    'down_left': [1, -1],
    'down_right': [1, 1]
}

def part_one() -> int:
    """Return the number of rolls of paper that can be accessed by a forklift."""
    data = _load_data()
    total_count = 0

    for row_idx, row in enumerate(data):
        for col_idx, _ in enumerate(data[row_idx]):
            if data[row_idx][col_idx] != '@':
                continue

            count = 0

            for d in DIRS:
                new_row_idx = row_idx + DIRS[d][0]
                new_col_idx = col_idx + DIRS[d][1]

                if 0 <= new_row_idx < len(data) and 0 <= new_col_idx < len(row):
                    if data[new_row_idx][new_col_idx] == '@':
                        count += 1

            if count < 4:
                total_count += 1

    return total_count


def part_two() -> int:
    """Return the number of rolls of paper that can be removed."""
    data = _load_data()
    data_copy = [list(line) for line in data]

    actual_total_count = 0

    # could be replaced with a recursive function all well
    while True:
        data_copy, total_count = _part_two_helper(data_copy)

        if total_count == 0:
            break

        actual_total_count += total_count

    return actual_total_count


def _part_two_helper(data: List[List[str]]) -> tuple[List[List[str]], int]:
    """Helper function for part two."""
    total_count = 0

    for row_idx, row in enumerate(data):
        for col_idx, _ in enumerate(data[row_idx]):
            if data[row_idx][col_idx] != '@':
                continue

            count = 0

            for d in DIRS:
                new_row_idx = row_idx + DIRS[d][0]
                new_col_idx = col_idx + DIRS[d][1]

                if 0 <= new_row_idx < len(data) and 0 <= new_col_idx < len(row):
                    if data[new_row_idx][new_col_idx] == '@':
                        count += 1

            if count < 4:
                data[row_idx][col_idx] = '.'
                total_count += 1

    return data, total_count

# # # # # # # #
# LOAD INPUT  #
# # # # # # # #

def _load_data() -> List[str]:
    """Load data from text file. Returns a list strings."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), INPUT_FILE)
    f = open(filepath, 'r')
    data = f.read()
    f.close()

    return data.strip().split('\n')

# print(part_one()) # 1370
# print(part_two()) # 8437
