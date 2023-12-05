"""Main solution file: day 03."""

import os
from functools import reduce
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


def part_two() -> int:
    """Return the sum of the gear ratios."""
    data = _load_data()
    max_row = len(data) - 1
    part_numbers = []

    for row, line in enumerate(data):
        max_col = len(line) - 1

        for col, char in enumerate(line):
            numbers = set()
            if char == '*':
                for dr in DIRECTIONS.values():
                    next_row = row + dr[0]
                    next_col = col + dr[1]

                    if next_row < 0 or next_row > max_row:
                        continue
                    if next_col < 0 or next_col > max_col:
                        continue

                    next_char = data[next_row][next_col]

                    if next_char.isnumeric():
                        loc = [next_row, next_col]
                        number = _get_number(data, loc, max_col)
                        numbers.add(int(number))

                if len(numbers) == 2:
                    part_numbers.append(numbers)

    gear_ratios = [reduce((lambda x, y: x * y), list(nums)) for nums in part_numbers]
    return sum(gear_ratios)


def _get_number(data: List[str], loc: List[int], max_col: int):
    """Return full number based on location of one of the digits.

    Args:
        data (list): the input data
        loc (list): coordinates of the current location where a digit was found
        max_col (int): the max column width
    """
    row, col = loc
    digit = data[row][col]
    left = DIRECTIONS['left']
    right = DIRECTIONS['right']

    number = char = digit

    next_col = col + left[1]
    char = data[row][next_col] if next_col >= 0 else ''
    while char.isnumeric():
        number = char + number
        next_col = next_col + left[1]
        if next_col < 0:
            char = ''
        else:
            char = data[row][next_col]

    next_col = col + right[1]
    char = data[row][next_col] if next_col <= max_col else ''
    while char.isnumeric():
        number = number + char
        next_col = next_col + right[1]
        if next_col > max_col:
            char = ''
        else:
            char = data[row][next_col]

    return number


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
# print(part_two())   # 80179647
