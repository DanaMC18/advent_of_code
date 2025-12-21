"""Day 06: Main solution file."""

import math
import os
from typing import List

INPUT_FILE = 'input.txt'

OPERATION_MAP = {
  '+': sum,
  '*': math.prod,
}

def part_one() -> int:
    """Return the grand total found by adding together all of the answers to the individual problems."""
    data = _load_data()
    totals = []
    formatted_data = _format_data(data)

    rotated_data = [list(row) for row in zip(*formatted_data)]

    for row in rotated_data:
      operation = row[-1]
      subtotal = OPERATION_MAP[operation](row[:-1])
      totals.append(subtotal)

    return sum(totals)


def _format_data(data: List[str]) -> List[List[str]]:
    """Format data into a list of lists."""
    rows = data[:-1]
    raw_numbers = [row.split(' ') for row in rows]
    formatted_data = []

    for row in raw_numbers:
      formatted_data.append([int(num) for num in row if num != ''])

    raw_operations = data[-1].split(' ')
    operations = [op for op in raw_operations if op != '']
    formatted_data.append(operations)

    return formatted_data


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


# print(part_two()) # 3785892992137
