"""Main solution file: Day 6."""

import os
from typing import List


INPUT_FILE = 'input.txt'


def main(days: int) -> int:
    """Determine how many fish will exist after N days."""
    input = _load_input()
    age_count = [0] * 9

    for age in input:
        age_count[age] += 1

    for _ in range(days):
        birthday = age_count.pop(0)
        age_count[6] += birthday
        age_count.append(birthday)

    # print(age_count)
    return sum(age_count)


def _load_input() -> List[int]:
    """Load input data from txt file."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), INPUT_FILE)
    f = open(filepath, 'r')
    data = f.read()
    f.close()

    return [int(d) for d in data.strip().split(',')]


# print(main(80))     # part_1 = 351188
# print(main(256))    # part_2 = 1595779846729
