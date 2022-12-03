"""Main solution file: day 02."""

import os
from typing import List

INPUT_FILE = 'input.txt'
PART_1_STRAT = {
    'X': {'A': 4, 'B': 1, 'C': 7},
    'Y': {'A': 8, 'B': 5, 'C': 2},
    'Z': {'A': 3, 'B': 9, 'C': 6}
}
PART_2_STRAT = {
    'A': {'X': 3, 'Y': 4, 'Z': 8},
    'B': {'X': 1, 'Y': 5, 'Z': 9},
    'C': {'X': 2, 'Y': 6, 'Z': 7}
}


def part_1() -> int:
    """Get total score according to strategy guide."""
    input = _load_data()
    score = 0

    for round in input:
        opponent, player = round.split(' ')
        score += PART_1_STRAT[player][opponent]

    return score


def part_2() -> int:
    """Get total score according to strategy guide."""
    input = _load_data()
    score = 0

    for round in input:
        opponent, result = round.split(' ')
        score += PART_2_STRAT[opponent][result]

    return score


# # # # # # # #
# LOAD INPUT  #
# # # # # # # #


def _load_data() -> List[str]:
    """Load data from text file."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), INPUT_FILE)
    f = open(filepath, 'r')
    data = f.read()

    return data.strip().split('\n')


# print(part_1())  # 15523
# print(part_2())  # 15702
