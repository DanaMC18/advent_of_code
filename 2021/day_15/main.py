"""Main solution file: day 15."""

from heapq import heappop, heappush
import os
from typing import List

INPUT_FILE = 'input.txt'

DIRECTIONS = {
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
    'up': [-1, 0]
}


def part_1() -> int:
    """Return total of least risky path."""
    input = _load_input()
    risk = _find_path(input)
    return risk


def _find_path(input):
    rows = len(input)
    cols = len(input[0])
    start = (0, 0)
    end = (rows - 1, cols - 1)
    risks = [(0, start)]
    seen = set()

    while risks:
        risk, curr_coord = heappop(risks)

        if curr_coord == end:
            return risk

        row, col = curr_coord

        for coord in DIRECTIONS.values():
            new_row = row + coord[0]
            new_col = col + coord[1]
            new_coord = (new_row, new_col)

            if 0 <= new_row < rows and 0 <= new_col < cols and new_coord not in seen:
                new_risk = risk + input[new_row][new_col]

                heappush(risks, (new_risk, new_coord))
                seen.add(new_coord)

    return risk


def _load_input() -> List[List[int]]:
    """Load input data from text file."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), INPUT_FILE)
    f = open(filepath, 'r')
    data = f.read()
    f.close()

    raw_input = data.strip().split('\n')
    return [[int(i) for i in line] for line in raw_input]


print(part_1())   # 429
