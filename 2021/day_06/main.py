"""Main solution file: Day 6."""

import os
from typing import List


INPUT_FILE = 'input.txt'


def main(days: int) -> int:
    """Determine how many fish will exist after N days."""
    input = _load_input()
    age_count = [0] * 9

    # list's index is the "age"
    # the value at an index is the num of fish at that age
    for age in input:
        age_count[age] += 1

    for _ in range(days):
        # age 0 = day for fish to spawn (AKA 'birthday')
        birthday = age_count.pop(0)

        # next birthday is in 7 days
        # add number of birthday fish to number of fish born 2 days ago
        age_count[6] += birthday

        # number of birthday fish == number of baby fish
        # add baby fish to end of list (index 8)
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
