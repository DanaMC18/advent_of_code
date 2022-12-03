"""Main solution file day 03."""

import os
from typing import List

INPUT_FILE = 'input.txt'
LOWER_MODIFIER = -96
UPPER_MODIFIER = -38


def part_1() -> int:
    """Return priority sum of duplicate items in each rucksack."""
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


def part_2() -> int:
    """Return priority sum of each group's badge."""
    input = _load_data()
    groups = _create_groups(input)
    priorities = []

    for group in groups:
        first, second, third = group
        badge = set(first).intersection(second).intersection(third).pop()

        if badge.islower():
            priority = ord(badge) + LOWER_MODIFIER
        else:
            priority = ord(badge) + UPPER_MODIFIER

        priorities.append(priority)

    return sum(priorities)


def _create_groups(rucksacks: List[str]) -> List[List[str]]:
    """Create groups of rucksacks.

    Args:
        rucksacks (list): list of strings; each string is a rucksack

    Returns:
        a matrix of groups of rucksacks
        example:
            [
                ['abc', 'def', 'ghi'],
                ['jkl', 'mno', 'pqr']
            ]
    """
    num = len(rucksacks) + 1
    groups = []
    start = 0
    stop = 3

    for i in range(num):
        if i % 3 == 0 and i > 0:
            groups.append(rucksacks[start:stop])
            start = i
            stop = i + 3

    return groups

# # # # # # # #
# LOAD INPUT  #
# # # # # # # #


def _load_data() -> List[str]:
    """Load data from txt file. Return a list of strings"""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), INPUT_FILE)
    f = open(filepath, 'r')
    data = f.read()

    return data.strip().split('\n')


# print(part_1())  # 7903
# print(part_2())  # 2548
