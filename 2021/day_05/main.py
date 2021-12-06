"""Main solution file: Day 5."""

import os
from typing import List

INPUT_FILE = 'input.txt'


def part_1() -> int:
    """Find number of overlapping points (points greater than 1)."""
    input = _load_input()
    vent_map = _blank_vent_map(input)
    populated_map = _plot_points(vent_map, input)

    overlap_count = 0

    for line in populated_map:
        overlaps = [p for p in line if p > 1]
        overlap_count += len(overlaps)

    return overlap_count


def _blank_vent_map(input: List[List[int]]) -> List[List[int]]:
    """Create blank vent_map matrix.

    Find highest coordinate number. Use number to determine size of matrix.

    Args:
        input (matrix): coordinates of all line termini
    """
    max_length = 0

    for coords in input:
        combo = coords[0] + coords[1]
        max_num = max(combo)
        if max_length < max_num:
            max_length = max_num

    blank_line = [0 for _ in range(max_length + 1)]
    return [blank_line.copy() for _ in range(max_length + 1)]


def _plot_points(blank_map: List[List[int]], input: List[List[int]]):
    """Create lines from coords and plot them on map.

    For each set of coords in input:
        1. Use coords to determine direction of line.
        2. Create line of plot points using termini in coordinates.
        3. Mark each point in line on the 'blank_map'.

    Args:
        blank_map (matrix): map made of coords with all points as 0
        input (matrix): coordinates of all line termini
    """
    for coords in input:
        if coords[0][1] == coords[1][1]:
            constant = coords[0][1]
            size = coords[1][0] - coords[0][0]
            dir = 'W' if size < 0 else 'E'
        elif coords[0][0] == coords[1][0]:
            constant = coords[0][0]
            size = coords[1][1] - coords[0][1]
            dir = 'N' if size < 0 else 'S'
        else:
            continue  # skip diagonals

        if dir == 'N':
            line = [[_, constant] for _ in range(coords[1][1], coords[0][1] + 1)]
        elif dir == 'E':
            line = [[constant, _] for _ in range(coords[0][0], coords[1][0] + 1)]
        elif dir == 'S':
            line = [[_, constant] for _ in range(coords[0][1], coords[1][1] + 1)]
        elif dir == 'W':
            line = [[constant, _] for _ in range(coords[1][0], coords[0][0] + 1)]

        for point in line:
            blank_map[point[0]][point[1]] += 1

    return blank_map


def _load_input() -> List[List[int]]:
    """Load input data from text file."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), INPUT_FILE)
    f = open(filepath, 'r')
    data = f.read()
    f.close()

    raw_input = data.strip().split('\n')
    input = [item.split(' -> ') for item in raw_input]

    new_input = list()

    for item in input:
        new_item = list()
        for coords in item:
            new_coords = [int(coord) for coord in coords.split(',')]
            new_item.append(new_coords)
        new_input.append(new_item)

    return new_input


# print(part_1())   # 5774
