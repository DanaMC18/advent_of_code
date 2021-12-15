"""Main solution file: day 13."""

import os
from typing import Dict, List, Tuple

INPUT_FILE = 'input.txt'


def main(part: int = 1) -> List[List[str]]:
    """Return graph paper after folding.

    Args:
        part (int): 1 or 2; if 1, fold graph only once; defaults to 1
    """
    input, all_folds = _load_input()

    rows = max([coord[1] for coord in input])
    cols = max([coord[0] for coord in input])

    blank_line = ['.' for _ in range(cols + 1)]
    blank_graph = [blank_line.copy() for _ in range(rows + 1)]

    clean_coords = list()

    for coord in input:
        col = coord[0]
        row = coord[1]
        blank_graph[row][col] = '#'
        clean_coords.append([row, col])

    folded_coords = clean_coords.copy()
    folded_graph = blank_graph.copy()
    folds = all_folds[:1] if part == 1 else all_folds

    for fold in folds:
        x = fold.get('x')
        y = fold.get('y')

        if x:
            new_coords, new_graph = _fold_left(folded_coords, folded_graph, x)

            folded_coords = new_coords
            folded_graph = [line[:x] for line in new_graph]

        if y:
            new_coords, new_graph = _fold_up(folded_coords, folded_graph, y)

            folded_coords = new_coords
            folded_graph = new_graph[:y]

    return folded_graph


def _fold_left(
    coords: List[List[int]],
    graph: List[List[str]],
    x: int
) -> Tuple[List[List[int]], List[List[str]]]:
    """Fold in half along x axis.

    Args:
        coords (martix): current list coordinates
        graph (matrix): current iteration of graph
        x (int): the col on which to fold the graph

    Returns:
        new_coords (matrix): new coordinates after fold
        new_graph (matrix): updated/marked graph after fold
    """
    rows = len(graph)
    cols = len(graph[0])

    new_coords = list()
    new_graph = graph.copy()

    for coord in coords:
        row, col = coord
        new_col = (cols - col - 1) if col > x else col

        if 0 <= row < rows:
            new_coords.append([row, new_col])
            new_graph[row][new_col] = '#'

    return new_coords, new_graph


def _fold_up(
    coords: List[List[int]],
    graph: List[List[str]],
    y: int
) -> Tuple[List[List[int]], List[List[str]]]:
    """Fold in half along the y axis.

    Args:
        coords (matrix): current list coordinates
        graph (matrix): current iteration of graph
        y (int): the row on which to fold the graph

    Returns:
        new_coords (matrix): new coordinates after fold
        new_graph (matrix): updated/marked graph after fold
    """
    rows = len(graph)
    cols = len(graph[0])

    new_coords = list()
    new_graph = graph.copy()

    for coord in coords:
        row, col = coord
        new_row = (rows - row - 1) if row > y else row

        if 0 <= col < cols:
            new_coords.append([new_row, col])
            new_graph[new_row][col] = '#'

    return new_coords, new_graph


def _load_input() -> Tuple[List[List[int]], List[Dict[str, int]]]:
    """Load input data from text file."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), INPUT_FILE)
    f = open(filepath, 'r')
    data = f.read()
    f.close()

    raw_coords, raw_folds = data.strip().split('\n\n')

    coords = [raw_coord.split(',') for raw_coord in raw_coords.split('\n')]
    input = [[int(c) for c in coord] for coord in coords]

    folds = raw_folds.split('\n')
    fold_dicts = list()

    for f in folds:
        key, value = f.split('fold along ')[1].split('=')
        fold_dicts.append({key: int(value)})

    return input, fold_dicts


# PART 1       # 814
# print(sum([line.count('#') for line in main()]))


# PART 2        # PZEHRAER
# for line in main(part=2):
#     print(line)
