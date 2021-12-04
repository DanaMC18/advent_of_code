"""Main solution file: day 04."""

import os
from typing import List, Tuple

INPUT_FILE = 'input.txt'


def part_1():
    """Get score of winning board."""
    board, number, coords = _find_winning_values()
    unmarked_nums = _unmarked_numbers(board, coords)

    return sum(unmarked_nums) * number


def _find_winning_values() -> Tuple[List[List[int]], int]:
    """Return the winning board and winning number."""
    numbers, boards = _load_input()

    for i in range(len(numbers)):
        for board in boards:
            coords = _matching_coords(board, numbers[:i + 1])
            if _has_winner(coords):
                return board, numbers[i], coords


def _matching_coords(
    board: List[List[int]],
    numbers_called: List[int]
) -> List[List[int]]:
    """Get coordinates of matching numbers on given board."""
    coords = list()

    for line in board:
        for num in line:
            if num in numbers_called:
                col = line.index(num)
                row = board.index(line)
                coord = [row, col]

                if coord not in coords:
                    coords.append(coord)

    return coords


def _has_winner(coords: List[List[int]]):
    """Check coords for five of the same col or row."""
    for num in range(5):
        vert_matches = [coord for coord in coords if coord[0] == num]
        hor_matches = [coord for coord in coords if coord[1] == num]

        if len(vert_matches) == 5 or len(hor_matches) == 5:
            return True

    return False


def _unmarked_numbers(
    board: List[List[int]],
    coords: List[List[int]]
) -> List[int]:
    """Find all unmarked numbers on given board."""
    cols = list(range(5))
    rows = list(range(5))
    unmarked_list = list()

    # cartesian product of all possible coords
    all_coords = [[col, row] for col in cols for row in rows]

    for coord in all_coords:
        if coord not in coords:
            row = coord[0]
            col = coord[1]
            num = board[row][col]
            unmarked_list.append(num)

    return unmarked_list


# # # # # # # # # # # #
# LOAD AND CLEAN INPUT:
# # # # # # # # # # # #


def _load_input() -> Tuple[List[str], List[List[str]]]:
    """Load input from text file."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), INPUT_FILE)
    f = open(filepath, 'r')
    data = f.read()
    f.close()

    input = data.strip().split('\n\n')
    numbers = input[0].split(',')
    boards = [board.split('\n') for board in input[1:]]

    clean_boards = [_transform_board(board) for board in boards]
    clean_nums = [int(num) for num in numbers]
    return clean_nums, clean_boards


def _transform_board(board: List[str]) -> List[List[int]]:
    """Turn each line in board from str to a list of ints."""
    new_board = list()

    for line in board:
        line_as_list = line.replace('  ', ' ').strip().split(' ')
        new_line = [int(num) for num in line_as_list]
        new_board.append(new_line)

    return new_board


# print(part_1())   # 63552
