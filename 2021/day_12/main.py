"""Main solution file: day 12."""

from collections import defaultdict
import os
from typing import Dict, List

INPUT_FILE = 'input.txt'


def part_1() -> int:
    """Get number of paths in cave system, visiting small caves at most once."""
    input = _load_input()
    path_count = _path_count('start', input, set())
    return path_count


def _path_count(current_cave: str, input: Dict[str, List[str]], seen: set) -> int:
    """Recursicely traverse cave system and return number of paths."""
    if current_cave == 'end':
        return 1

    if current_cave.islower() and current_cave in seen:
        return 0

    seen = seen.union({current_cave})

    count = 0
    for cave in input[current_cave]:
        count += _path_count(cave, input, seen)

    return count


def _load_input() -> Dict[str, List[str]]:
    """Load input data from text file."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), INPUT_FILE)
    f = open(filepath, 'r')
    data = f.read()
    f.close()

    raw_input = data.strip().split('\n')
    input = defaultdict(list)
    for line in raw_input:
        x, y = line.split('-')
        input[x].append(y)
        input[y].append(x)

    return input


print(part_1())   # 4241
