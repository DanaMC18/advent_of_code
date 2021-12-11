"""Main soultion file: day 10."""

import os
from typing import List

BRACKET_PAIRS = {
    '(': ')',
    '{': '}',
    '[': ']',
    '<': '>'
}
INPUT_FILE = 'input.txt'


def part_1() -> int:
    """Find syntax error score of corrupted input lines using a stack."""
    input = _load_input()
    point_map = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    score = 0

    for line in input:
        stack = list()

        for char in line:
            if char in BRACKET_PAIRS.keys():
                stack.append(char)
            elif not stack:
                score += point_map[char]
                break
            else:
                last_char = stack.pop()
                if BRACKET_PAIRS[last_char] != char:
                    score += point_map[char]
                    break

    return score


def part_2() -> int:
    """Find autocomplete score after completing incorrect input lines using a stack."""
    input = _load_input()
    point_map = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    scores = list()

    for line in input:
        stack = list()

        for char in line:
            if char in BRACKET_PAIRS.keys():
                stack.append(char)
            elif not stack:
                break
            else:
                last_char = stack.pop()
                if BRACKET_PAIRS[last_char] != char:
                    stack = list()
                    break

        if stack:
            score = 0
            for bracket in reversed(stack):
                match = BRACKET_PAIRS[bracket]
                score = (score * 5) + point_map[match]
            scores.append(score)

    sorted_scores = sorted(scores)
    median = sorted_scores[len(scores) // 2]
    return median


def _load_input() -> List[str]:
    """Load input data from text file."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), INPUT_FILE)
    f = open(filepath, 'r')
    data = f.read()
    f.close()

    return data.strip().split('\n')


# print(part_1())   # 394647
# print(part_2())   # 2380061249
