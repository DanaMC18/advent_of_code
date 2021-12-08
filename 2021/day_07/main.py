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


# NOTES:
# Apparently the most efficient position in part 1 is the median of the list.
# For part 2, the most effefient position is the mean of the list.
# Part 2 also makes use of triangular numbers: n * (n + 1) / 2
# All the work done above to find the right position isn't necessary or effecient.

# PART 1:
def part_1_median() -> int:
    """Use median to find fuel total."""
    input = _load_input()
    length = len(input)
    sorted_input = sorted(input)
    median = sorted_input[length // 2]

    return sum([abs(x - median) for x in input])


# print(part_1_median())


# PART 2:
def part_2_mean() -> int:
    """Use mean and triangular numbers to find fuel total."""
    input = _load_input()
    length = len(input)
    mean = sum(input) // length

    return sum(_triangulate_fuel(abs(x - mean)) for x in input)


def _triangulate_fuel(pos: int) -> int:
    """Use trianguluar numbers to get fuel from position."""
    return pos * (pos + 1) // 2


# print(part_2_mean())
