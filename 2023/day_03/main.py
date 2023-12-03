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

    for line in data:
        row = data.index(line)
        max_col = len(line) - 1
        number = ''
        for char in line:
            if char.isnumeric():
                number = number + char
            elif number:
                col = line.index(number)
                pos = [row, col]

                for d in DIRECTIONS.values():
                    next_row = pos[0] + d[0] if pos[0] < max_row else pos[0]
                    next_col = pos[1] + d[1] if pos[1] < max_col else pos[1]
                    next_pos = data[next_row][next_col]

                    if next_pos == '.' or next_pos.isnumeric():
                        continue
                    else:
                        valid_nums.append(number)

                number = ''

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


print(part_one())
