"""Main solution file day 07."""

import os
from typing import List

INPUT_FILE = 'input.txt'


def part_1() -> int:
    """For directories less than 100000, sum their sizes."""
    input = _load_data()
    dir_path = ['/']
    dir_sizes = {'/': 0}

    for cmd in input:
        if cmd.startswith('$'):
            if cmd.startswith('$ cd'):
                dir = cmd.split(' ')[2]

                if dir == '..' and len(dir_path) > 1:
                    dir_path.pop()
                    continue

                if dir == '/':
                    dir_path = ['/']
                    continue

                if dir not in dir_sizes:
                    dir_sizes[dir] = 0

                dir_path.append(dir)
            continue

        if cmd.startswith('dir'):
            dir = cmd.split(' ')[1]
            if dir not in dir_sizes:
                dir_sizes[dir] = 0
            continue

        curr_dir = dir_path[-1]
        size = cmd.split(' ')[0]
        dir_sizes[curr_dir] = dir_sizes[curr_dir] + int(size)

        for d in dir_path:
            if d != curr_dir:
                dir_sizes[d] = dir_sizes[d] + int(size)

    small_sizes = [v for v in dir_sizes.values() if v <= 100000]
    return sum(small_sizes)


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


print(part_1())
# 1151021 too low
