"""Main solution file: Day 17."""

import os
from typing import Dict, List

INPUT_FILE = 'input.txt'


def part_1() -> int:
    """Return highest y position to hit target area with highest arc."""
    input = _load_input()
    y = input.get('y')

    # triangulate forumula using abs in case of negatives
    min_y = min(y)
    highest_y = abs(min_y) * (abs(min_y) - 1) // 2
    return highest_y


def part_2() -> int:
    """Return number of distinct initital velocity values that hit target area."""
    input = _load_input()
    x_range = input.get('x')
    y_range = input.get('y')

    end_x = x_range[1] + 1
    start_y = -abs(y_range[0])
    end_y = abs(y_range[0])

    valid_velocity_count = 0

    for x_val in range(1, end_x):
        for y_val in range(start_y, end_y):
            if _is_valid(x_range, y_range, x_val, y_val):
                valid_velocity_count += 1

    return valid_velocity_count


def _is_valid(
    x_range: List[int],
    y_range: List[int],
    x_val: int,
    y_val: int
) -> bool:
    """Return if points will fall in given target ranges.

    Args:
        x_range (list): target range on x-axis
        y_range (list): target range on y-axis
        x_val (int): point on x-axis
        y_val (int): point on y-axis
    """
    x = y = 0
    x1, x2 = x_range
    y1, y2 = y_range

    while y > -abs(y1):
        x += x_val
        y += y_val

        x_val = x_val - 1 if x_val > 0 else x_val
        y_val -= 1

        if x1 <= x <= x2 and -abs(y1) <= y <= -abs(y2):
            return True

    return False


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
# print(part_2())   # 5644
