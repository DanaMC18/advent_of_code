"""Main solution file day 03."""

import os
from typing import List

INPUT_FILE = 'input.txt'
LOWER_MODIFIER = -96
UPPER_MODIFIER = -38


def part_1() -> int:
    """Return priority sum of duplicate items in rucksacks."""
    input = _load_data()
    priorities = []

    for contents in input:
        mid = int(len(contents) / 2)
        first, second = contents[:mid], contents[mid:]
        dupe = set(first).intersection(second).pop()

        if dupe.islower():
            priority = ord(dupe) + LOWER_MODIFIER
        else:
            priority = ord(dupe) + UPPER_MODIFIER

        priorities.append(priority)

    return sum(priorities)

# # # # # # # #
# LOAD INPUT  #
# # # # # # # #


def _load_data() -> List[str]:
    """Load data from txt file. Return a list of strings"""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), INPUT_FILE)
    f = open(filepath, 'r')
    data = f.read()

    return data.strip().split('\n')


print(part_1())  # 7903
