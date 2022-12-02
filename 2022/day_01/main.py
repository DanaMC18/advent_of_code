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
    three_highest_totals = []

    for elf_rations in input:
        total = sum(elf_rations)

        if len(three_highest_totals) < 3:
            three_highest_totals.append(total)
            continue

        all_totals = three_highest_totals + [total]
        all_totals.remove(min(all_totals))
        three_highest_totals = all_totals

    return sum(three_highest_totals)


# # # # # # # #
# LOAD INPUT  #
# # # # # # # #

def _load_data() -> List[int]:
    """Load data from text file."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), INPUT_FILE)
    f = open(filepath, 'r')
    data = f.read()
    f.close()

    input = [i.split('\n') for i in data.strip().split('\n\n')]

    return [[int(item) for item in elf] for elf in input]


# print(part_1()) # 72070
# print(part_2()) # 211805
