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
            if not _is_valid_part_one(str(id)):
                invalid_ids.append(id)

    return sum(invalid_ids)


def _is_valid_part_one(id: str) -> bool:
    """Return whether ID is valid or not"""
    if len(id) % 2 != 0:
        return True

    middle_index = len(id) // 2
    return id[:middle_index] != id[middle_index:]


def part_two() -> int:
    """Return the sum of all invalid IDs."""
    data = _load_data()
    invalid_ids = []

    for id_range in data:
        start, end = id_range.split('-')
        start = int(start)
        end = int(end)

        for id in range(start, end + 1):
            if not _is_valid_part_two(str(id)):
                invalid_ids.append(id)

    return sum(invalid_ids)


def _is_valid_part_two(id: str) -> bool:
    """Return whether ID is valid or not"""
    id_len = len(id)

    for idx in range(id_len // 2):
        quotient, remainder = divmod(id_len, idx + 1)
        if remainder == 0 and id[:idx + 1] * quotient == id:
            return False

    return True


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

# print(part_one()) # 15873079081
# print(part_two()) # 22617871034
