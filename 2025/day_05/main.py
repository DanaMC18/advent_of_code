"""Day 05: Main solution file."""

import os
from typing import List

INPUT_FILE = 'input.txt'

def part_one() -> int:
    """Return the number of fresh ingredient IDs."""
    data = _load_data()
    idx = data.index('')

    fresh_ranges = data[:idx]
    ingredient_ids = data[idx+1:]
    count = 0

    for ingredient_id in ingredient_ids:
        for r in fresh_ranges:
            start, end = r.split('-')
            if int(ingredient_id) >= int(start) and int(ingredient_id) <= int(end):
                count += 1
                break

    return count


def part_two() -> int:
    """Return the number of ingredient IDs considered to be fresh."""
    data = _load_data()
    idx = data.index('')
    fresh_ranges = data[:idx]

    ranges = []

    for r in fresh_ranges:
        start, end = r.split('-')
        ranges.append((int(start), int(end)))

    sorted_ranges = sorted(ranges)

    merged_ranges = []

    for start, end in sorted_ranges:
        if merged_ranges and start <= merged_ranges[-1][1] + 1:
            max_end = max(end, merged_ranges[-1][1])
            merged_ranges[-1] = (merged_ranges[-1][0], max_end)      
        else:
            merged_ranges.append((start, end))

    total_ids = 0

    for start, end in merged_ranges:
        total_ids += (end - start) + 1

    return total_ids


# # # # # # # #
# LOAD INPUT  #
# # # # # # # #

def _load_data() -> List[str]:
    """Load data from text file. Returns a list strings."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), INPUT_FILE)
    f = open(filepath, 'r')
    data = f.read()
    f.close()

    return data.strip().split('\n')

# print(part_one()) # 607
# print(part_two()) # 342433357244012
