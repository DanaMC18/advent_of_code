"""Main soultion file: day 10."""

import os
from typing import List

BRACKETS = '(){}[]<>'
BRACKET_PAIRS = {
    '(': ')',
    '{': '}',
    '[': ']',
    '<': '>'
}
INPUT_FILE = 'input.txt'
POINT_MAP = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


def part_1() -> int:
    """Find syntax error score of input using a stack."""
    input = _load_input()
    score = 0

    for line in input:
        stack = list()

        for char in line:
            if char in BRACKET_PAIRS.keys():
                stack.append(char)
            elif not stack:
                score += POINT_MAP[char]
                break
            else:
                last_char = stack.pop()
                if BRACKET_PAIRS[last_char] != char:
                    score += POINT_MAP[char]
                    break

    return score


def _load_input() -> List[str]:
    """Load input data from text file."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), INPUT_FILE)
    f = open(filepath, 'r')
    data = f.read()
    f.close()

    return data.strip().split('\n')


print(part_1())
