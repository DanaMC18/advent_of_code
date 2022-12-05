"""Solution file: day 04."""

import os
from typing import List

INPUT_FILE = 'input.txt'


def part_1() -> int:
    """Find number of assignments that fully overlap."""
    input = _load_data()
    overlaps = 0

    for pair in input:
        sect_1, sect_2 = pair[0], pair[1]

        sect_1_min, sect_1_max = [int(i) for i in sect_1.split('-')]
        sect_2_min, sect_2_max = [int(i) for i in sect_2.split('-')]

        section_1 = list(range(sect_1_min, sect_1_max + 1))
        section_2 = list(range(sect_2_min, sect_2_max + 1))

        dupes = set(section_1).intersection(section_2)

        if len(dupes) == len(section_1) or len(dupes) == len(section_2):
            overlaps += 1

    return overlaps


def part_2() -> int:
    """Find number of assignments that partially overlap."""
    input = _load_data()
    overlaps = 0

    for pair in input:
        sect_1, sect_2 = pair[0], pair[1]

        sect_1_min, sect_1_max = [int(i) for i in sect_1.split('-')]
        sect_2_min, sect_2_max = [int(i) for i in sect_2.split('-')]

        section_1 = list(range(sect_1_min, sect_1_max + 1))
        section_2 = list(range(sect_2_min, sect_2_max + 1))

        dupes = set(section_1).intersection(section_2)

        if dupes:
            overlaps += 1

    return overlaps


# # # # # # # #
# LOAD INPUT  #
# # # # # # # #

def _load_data() -> List[List]:
    """Load data from txt file. Return list."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), INPUT_FILE)
    f = open(filepath, 'r')
    data = f.read()

    input = data.strip().split('\n')
    pairs = [[i for i in pair.split(',')] for pair in input]
    return pairs


# print(part_1())  # 562
# print(part_2())  # 924
