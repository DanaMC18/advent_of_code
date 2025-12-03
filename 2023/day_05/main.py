"""Main solution file: day 05."""

import os
from typing import List

INPUT_FILE = 'input.txt'

# # # # # # # #
# LOAD INPUT  #
# # # # # # # #


def _format_data() -> dict:
    """Format input data."""
    raw_data = _load_data()
    formatted_data = {}

    for i, line in enumerate(raw_data):
        if i == 0:
            seeds = line.split(': ')[1].split(' ')
            formatted_data['seeds'] = [int(s) for s in seeds]
            continue

        m = line.split(' map:\n')
        source, destination = m[0].split('-to-')
        raw_ranges = m[1].split('\n')
        ranges = []

        for rr in raw_ranges:
            [ranges.append(int(r)) for r in rr.split(' ')]


def _load_data() -> List[str]:
    """Load data from text file. Returns a list strings."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), INPUT_FILE)
    f = open(filepath, 'r')
    data = f.read()
    f.close()

    return data.strip().split('\n\n')


print(_format_data())
