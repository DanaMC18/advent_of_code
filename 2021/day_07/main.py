"""Main solution file: Day 7."""

import os
from typing import List

INPUT_FILE = 'input.txt'


def part_1() -> int:
    """Align crab submarines in position using least amount of fuel."""
    input = _load_input()
    fuel_totals = list()

    for i in range(1, len(input) + 1):
        fuel_totals.append(sum([abs(position - i) for position in input]))

    return min(fuel_totals)


def part_2() -> int:
    """Align crab subarines in position using least amount of fuel."""
    input = _load_input()
    fuel_totals = list()

    for i in range(1, len(input) + 1):
        fuel = 0
        for position in input:
            diff = abs(position - i)
            fuel += sum(range(diff + 1))
        fuel_totals.append(fuel)

    return min(fuel_totals)


def _load_input() -> List[int]:
    """Load input data from text file."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), INPUT_FILE)
    f = open(filepath, 'r')
    data = f.read()
    f.close()
    input = data.strip().split(',')
    return [int(i) for i in input]


# print(part_1())   # 336701
# print(part_2())   # 95167302
