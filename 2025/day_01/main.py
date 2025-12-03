"""Day 01: Main solution file."""

import os
from typing import List

INPUT_FILE = 'input.txt'

def part_one() -> int:
    """Return the number of times the dial passes 0."""
    count = 0
    current_position = 50
    dial = list(range(100))
    rotations = _load_data()

    for rotation in rotations:
        direction = rotation[0]
        amount = int(rotation[1:])

        if direction == 'L':
            current_position = (current_position - amount) % 100
        else:
            current_position = (current_position + amount) % 100

        if current_position == 0:
            count += 1

    return count


def part_two() -> int:
    """Return the number of times the dial equals 0."""
    count = 0
    current_position = 50
    dial = list(range(100))
    rotations = _load_data()

    for rotation in rotations:
        direction = rotation[0]
        amount = int(rotation[1:])

        if direction == 'L':
            new_position = current_position - amount

            if current_position == 0:
                count += amount // 100
            elif amount >= current_position:
                count += 1 + (amount - current_position) // 100

        else:   
            new_position = current_position + amount
            count += new_position // 100

        current_position = new_position % 100

    return count


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


# print(part_one()) # 1086
print(part_two()) # 1086
