"""Main solution file: Day 1."""

import os
from typing import List

INPUT_FILE = 'input.txt'


def part_1() -> int:
    """Part 1: Find how quickly depth increases."""
    input = _load_data()
    return _increase_count(input)


def part_2() -> int:
    """Part 2: Find how quickly depth increases on sliding scale."""
    windows = _create_windows()
    totals = list()

    for window in windows:
        totals.append(sum(window))

    return _increase_count(totals)


def _create_windows() -> List[list]:
    """Create three-measurement sliding windows from input."""
    input = _load_data()
    loc_1 = 0
    loc_2 = 3
    windows = list()

    for _ in input:
        window = input[loc_1:loc_2]
        windows.append(window)
        loc_1 += 1
        loc_2 += 1

    return windows


def _increase_count(input: List[int]) -> int:
    """Find number of increases in given list."""
    increase_count = 0

    for i in range(len(input))[1:]:  # skip first item
        prev = input[i - 1]
        curr = input[i]

        if prev < curr:
            increase_count += 1

    return increase_count


def _load_data() -> List[int]:
    """Load data from text file."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), INPUT_FILE)
    f = open(filepath, 'r')
    data = f.read()
    f.close()
    input = data.strip().split('\n')
    return [int(depth) for depth in input]


# print(part_1())   # 1121
# print(part_2())   # 1065
