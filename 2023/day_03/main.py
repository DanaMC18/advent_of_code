"""Main solution file: day 03."""

import os
from typing import List

INPUT_FILE = 'input.txt'
DIRECTIONS = {
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
    """Return the sum of valid part numbers in schematic."""
    data = _load_data()
    max_row = len(data) - 1
    valid_nums = []

    for row, line in enumerate(data):
        max_col = len(line) - 1
        number = ''
        is_valid = False
        for col, char in enumerate(line):
            if char.isnumeric():
                number = number + char

                for dr in DIRECTIONS.values():
                    next_row = row + dr[0]
                    next_col = col + dr[1]

                    if next_row < 0 or next_row > max_row:
                        continue
                    if next_col < 0 or next_col > max_col:
                        continue

                    next_char = data[next_row][next_col]

                    if next_char != '.' and not next_char.isnumeric():
                        is_valid = True
            else:
                if is_valid:
                    valid_nums.append(number)
                    is_valid = False
                number = ''

        if is_valid:
            valid_nums.append(number)

    return sum([int(num) for num in valid_nums])


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


# print(part_one())   # 551094
