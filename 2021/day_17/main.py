"""Main solution file: Day 17."""

import os
from typing import Dict, List

INPUT_FILE = 'input.txt'

# abs(y) * (abs(y) - 1) / 2


def part_1():
    """Return highest y position to hit target area with highest arc."""
    input = _load_input()
    y = input.get('y')

    # triangulate
    min_y = min(y)
    highest_y = abs(min_y) * (abs(min_y) - 1) / 2
    return int(highest_y)


def _load_input() -> Dict[str, List[int]]:
    """Load input data from text file."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), INPUT_FILE)
    f = open(filepath, 'r')
    data = f.read()
    f.close()

    raw_input = data.strip().split('target area: ')[1]
    raw_x, raw_y = raw_input.split(', ')
    data_x = raw_x.split('=')[1].split('..')
    data_y = raw_y.split('=')[1].split('..')

    x = [int(num) for num in data_x]
    y = [int(num) for num in data_y]

    return {'x': x, 'y': y}


# print(part_1())   # 13203
