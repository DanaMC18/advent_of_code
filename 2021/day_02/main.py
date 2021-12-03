"""Main solution file: Day 2."""

import os
from typing import List, Tuple

INPUT_FILE = 'input.txt'
DEPTH_CALC = {
    'down': 1,
    'up': -1
}


def part_1() -> int:
    """Find planned sub destination."""
    instructions = _load_input()
    hor, depth = _find_destination(instructions)
    return hor * depth


def _find_destination(instructions: List[str]) -> Tuple[int, int]:
    """Find destination based on instructions."""
    hor = 0
    depth = 0

    for step in instructions:
        command, val = step.split(' ')
        val = int(val)

        if command in DEPTH_CALC:
            depth += (val * DEPTH_CALC[command])
        else:
            hor += val

    return hor, depth


def _load_input() -> List[str]:
    """Load input data from text file."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), INPUT_FILE)
    f = open(filepath, 'r')
    data = f.read()
    f.close()
    return data.strip().split('\n')


print(part_1())  # 1728414
