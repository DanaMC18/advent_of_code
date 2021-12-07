"""Main solution file: Day 6."""

import os
from typing import List


INPUT_FILE = 'input.txt'


def part_1() -> int:
    """Determine how many fish will exist after 80 days."""
    input = _load_input()
    day = 1
    fish_list = input.copy()

    while day <= 80:
        new_fish_list = list()
        baby_fish_list = list()

        for fish in fish_list:
            if fish == 0:
                new_fish = 6
                baby_fish_list.append(8)
            else:
                new_fish = fish - 1
            new_fish_list.append(new_fish)

        fish_list = new_fish_list + baby_fish_list
        day += 1

    return len(fish_list)


def _load_input() -> List[int]:
    """Load input data from txt file."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), INPUT_FILE)
    f = open(filepath, 'r')
    data = f.read()
    f.close()

    return [int(d) for d in data.strip().split(',')]


# print(part_1())   # 351188
