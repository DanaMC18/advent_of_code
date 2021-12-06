"""Main solution file: Day 5."""

import os
from typing import List

INPUT_FILE = 'input.txt'


def main() -> int:
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
    """Create lines from coords and plot them on map. Returns populated map as matrix.

    For each set of coords in input:
        1. Use coords to determine direction of line.
        2. Create line of plot points using termini in coordinates.
        3. Mark each point in line on the 'blank_map'.

    Args:
        blank_map (matrix): map made of coords with all points as 0
        input (matrix): coordinates of all line termini
    """
    for coords in input:
        combo = coords[0] + coords[1]
        constant = max(set(combo), key=combo.count)
        termini = [c for c in combo if c != constant]

        #  check if termini was removed because it was same num as constant
        if len(termini) == 1:
            termini.append(constant)

        if coords[0][1] == coords[1][1]:
            dir = 'horizontal'
        elif coords[0][0] == coords[1][0]:
            dir = 'vertical'
        else:
            # continue  # PART 1: skip diagonals
            dir = 'diag'

        if dir == 'horizontal':
            start = min(termini)
            end = max(termini)
            line = [[constant, _] for _ in range(start, end + 1)]
        elif dir == 'vertical':
            start = min(termini)
            end = max(termini)
            line = [[_, constant] for _ in range(start, end + 1)]
        else:
            # PART 2: handle diagonals
            col_termini = [coords[0][0], coords[1][0]]
            col_start = min(col_termini)
            col_end = max(col_termini)

            row_termini = [coords[0][1], coords[1][1]]
            row_start = min(row_termini)
            row_end = max(row_termini)

            cols = list(range(col_start, col_end + 1))
            rows = list(range(row_start, row_end + 1))

            if col_termini[0] > col_termini[1]:
                cols.reverse()

            if row_termini[0] > row_termini[1]:
                rows.reverse()

            line = list()
            for index in range(len(cols)):
                line.append([rows[index], cols[index]])

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


# print(main())

# part_1 = 5774
# part_2 = 18423
