"""Main solution file: day 11."""

import os
from typing import List, Tuple


ADJACENT_DIRS = {
    'decline_down': [1, 1],
    'decline_up': [-1, -1],
    'down': [1, 0],
    'incline_down': [1, -1],
    'incline_up': [-1, 1],
    'left': [0, -1],
    'right': [0, 1],
    'up': [-1, 0]
}
INPUT_FILE = 'input.txt'


def part_1() -> int:
    """Return number of flashes after 100 steps."""
    initial_input = _load_input()
    rows = len(initial_input)
    cols = len(initial_input[0])

    input = initial_input.copy()
    total_glow_count = 0

    for _ in range(100):
        flashed = list()
        for row in range(rows):
            for col in range(cols):
                coords = [[col, row]]
                new_input, glow_count = _get_glow_counts(coords, input, flashed)
                input = new_input
                total_glow_count += glow_count

    return total_glow_count


def part_2() -> int:
    """Return step at which all flashes happen at once."""
    initial_input = _load_input()
    rows = len(initial_input)
    cols = len(initial_input[0])

    input = initial_input.copy()
    step_num = 0

    while True:
        flashed = list()
        step_glow_count = 0

        step_num += 1

        for row in range(rows):
            for col in range(cols):
                coords = [[col, row]]
                new_input, glow_count = _get_glow_counts(coords, input, flashed)
                input = new_input
                step_glow_count += glow_count

        if step_glow_count == 100:
            break

    return step_num


def _get_glow_counts(
    coord_stack: List[List[int]],
    input: List[List[int]],
    flashed: List[List[int]],
    glow_count: int = 0
) -> Tuple[List[List[int]], int]:
    """Recursively get glow count using a stack."""
    if not coord_stack:
        return input, glow_count

    coord = coord_stack.pop()
    row = coord[0]
    col = coord[1]

    if flashed and coord in flashed:
        return _get_glow_counts(coord_stack, input, flashed, glow_count)

    if input[row][col] < 9:
        input[row][col] += 1
        return _get_glow_counts(coord_stack, input, flashed, glow_count)

    # handle a flashing octo
    glow_count += 1
    input[row][col] = 0

    if coord not in flashed:
        flashed.append(coord)

    for ad in ADJACENT_DIRS.values():
        new_row = row + ad[0]
        new_col = col + ad[1]

        if 0 <= new_row < 10 and 0 <= new_col < 10:
            coord_stack.append([new_row, new_col])

    return _get_glow_counts(coord_stack, input, flashed, glow_count)


def _load_input() -> List[List[int]]:
    """Load input data from text file."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), INPUT_FILE)
    f = open(filepath, 'r')
    data = f.read()
    f.close()

    raw_input = data.strip().split('\n')
    input = [list(ri) for ri in raw_input]
    return [[int(i) for i in line] for line in input]


# print(part_1())   # 1571
# print(part_2())   # 387
