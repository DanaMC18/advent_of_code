"""Main solution file: Day 2."""

import os
from typing import List

INPUT_FILE = 'input.txt'
DEPTH_CALC = {
    'down': 1,
    'up': -1
}


def part_1() -> int:
    """Find planned sub destination."""
    instructions = _load_input()
    depth = hor = 0

    for step in instructions:
        command, val = step.split(' ')
        val = int(val)

        if command in DEPTH_CALC:
            depth += (val * DEPTH_CALC[command])
        else:
            hor += val

    return depth * hor


def part_2() -> int:
    """Find planned sub destination but better."""
    instructions = _load_input()
    aim = depth = hor = 0

    for step in instructions:
        command, val = step.split(' ')
        val = int(val)

        if command in DEPTH_CALC:
            aim += (val * DEPTH_CALC[command])
        else:
            hor += val
            depth += (aim * val)

    return depth * hor


def _load_input() -> List[str]:
    """Load input data from text file."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), INPUT_FILE)
    f = open(filepath, 'r')
    data = f.read()
    f.close()
    return data.strip().split('\n')


# print(part_1())   # 1728414
# print(part_2())   # 1765720035
