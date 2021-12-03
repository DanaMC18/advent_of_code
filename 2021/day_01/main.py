"""Main solution file: day 1."""

import os

INPUT_FILE = 'input.txt'


def part_1():
    """Part 1: Find how quickly depth increases."""
    input = _load_data()
    increase_count = 0

    for i in range(len(input))[1:]:
        prev_depth = input[i - 1]
        curr_depth = input[i]

        if prev_depth < curr_depth:
            increase_count = increase_count + 1

    return increase_count


def _load_data():
    """Load data from text file."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), INPUT_FILE)
    f = open(filepath, 'r')
    data = f.read()
    f.close()
    input = data.strip().split('\n')
    return [int(depth) for depth in input]


print(part_1())
