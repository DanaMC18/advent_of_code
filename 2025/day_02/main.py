"""Day 2: Main solution file."""

import os
from typing import List

INPUT_FILE = 'input.txt'

def part_one() -> int:
    """Return the sum of all invalid IDs."""
    data = _load_data()
    invalid_ids = []

    for id_range in data:
        start, end = id_range.split('-')
        start = int(start)
        end = int(end)

        for id in range(start, end + 1):
            if not _is_valid(str(id)):
                invalid_ids.append(id)

    return sum(invalid_ids)


# TODO: logic here is wrong -- need to account for twice-repeated sequences, which this isn't doing
def _is_valid(id: str) -> bool:
    """Return whether ID is valid or not"""
    char_map = {}

    for char in id:
        if char in char_map:
            char_map[char] += 1
        else:
            char_map[char] = 1

    return len(set(char_map.values())) > 1


# # # # # # # #
# LOAD INPUT  #
# # # # # # # #

def _load_data() -> List[str]:
    """Load data from text file. Returns a list strings."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), INPUT_FILE)
    f = open(filepath, 'r')
    data = f.read()
    f.close()

    return data.strip().split(',')

print(part_one())
