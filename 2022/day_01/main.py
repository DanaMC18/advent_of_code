"""Main solution file: Day 1."""

import os
from typing import List

INPUT_FILE = 'input.txt'


def part_1() -> int:
    """Part 1: Find total calories of the elf carrying the most calories."""
    input = _load_data()
    most_total_calories = 0

    for elf_rations in input:
        total = sum(elf_rations)
        most_total_calories = max(total, most_total_calories)

    return most_total_calories


def part_2() -> int:
    """Part 2: Find total calories of three elves carrying the most calories."""
    input = _load_data()
    highest_totals = []

    for elf_rations in input:
        total = sum(elf_rations)
        highest_totals.append(total)

        if len(highest_totals) > 3:
            highest_totals.remove(min(highest_totals))

    return sum(highest_totals)


# # # # # # # #
# LOAD INPUT  #
# # # # # # # #

def _load_data() -> List[List[int]]:
    """Load data from text file. Returns a list of lists of integers."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), INPUT_FILE)
    f = open(filepath, 'r')
    data = f.read()
    f.close()

    input = [i.split('\n') for i in data.strip().split('\n\n')]

    return [[int(item) for item in elf] for elf in input]


# print(part_1())  # 72070
# print(part_2())  # 211805
