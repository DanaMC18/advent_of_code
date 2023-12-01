"""Main solution file: Day 1."""

import os
from typing import List

INPUT_FILE = 'input.txt'


def part_one() -> int:
    """Return sum of all calibration values in input."""
    calibration_data = _load_data()
    calibration_values = []

    for line in calibration_data:
        numbers = [char for char in line if char.isnumeric()]
        value = f'{numbers[0]}{numbers[-1]}'
        calibration_values.append(value)

    return sum([int(num) for num in calibration_values])


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


print(part_one()) # 55971
