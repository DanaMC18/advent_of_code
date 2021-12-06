"""Main solution file: day 04."""

import os
from typing import List, Tuple

INPUT_FILE = 'input.txt'


def part_1() -> int:
    """Get score of winning board."""
    board, number, coords = _find_winning_values()
    unmarked_nums = _unmarked_numbers(board, coords)

    return sum(unmarked_nums) * number


def part_2() -> int:
    """Get score of board to win last."""
    board, number, coords = _find_winning_values(-1)
    unmarked_nums = _unmarked_numbers(board, coords)

    return sum(unmarked_nums) * number


def _find_winning_values(winning_index: int = 0) -> Tuple:
    """Get winning values.

    Returns a tuple of:
        1. winning board (matrix)
        2. winning number (int)
        3. coords of marked numbers on winning board (matrix)

    Args:
        winning_index (int): index from which to check for a winning set
            - if 0, find first set of values to win
            - if -1, find last set of values to win
    """
    numbers, boards = _load_input()
    winning_boards = list()
    winning_numbers = list()
    winning_coords = list()

    for i in range(len(numbers)):
        for board in boards:
            coords = _matching_coords(board, numbers[:i + 1])
            if _has_winner(coords) and board not in winning_boards:
                winning_boards.append(board)
                winning_numbers.append(numbers[i])
                winning_coords.append(coords)

    winning_board = winning_boards[winning_index]
    winning_number = winning_numbers[winning_index]
    winning_coords_set = winning_coords[winning_index]

    return winning_board, winning_number, winning_coords_set


def _matching_coords(
    board: List[List[int]],
    numbers_called: List[int]
) -> List[List[int]]:
    """Get coordinates of matching numbers on given board. Returns a matrix.

    Args:
        board (matrix): a bingo board
        numbers_called (list): list of numbers that have been called during bingo game
    """
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


def _has_winner(coords: List[List[int]]) -> bool:
    """Check coords for five of the same col or row.

    Args:
        coords (matrix): coordinates of marked numbers on bingo card
    """
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
    """Find all unmarked numbers on given board.

    Args:
        board (matrix): a bingo board
        coords (matrix): coordinates of marked numbers on bingo card
    """
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
    raw_numbers = input[0].split(',')
    raw_boards = [board.split('\n') for board in input[1:]]

    boards = [_transform_board(board) for board in raw_boards]
    numbers = [int(num) for num in raw_numbers]
    return numbers, boards


def _transform_board(board: List[str]) -> List[List[int]]:
    """Turn each line on a bingo board from a str to a list of ints."""
    new_board = list()

    for line in board:
        line_as_list = line.replace('  ', ' ').strip().split(' ')
        new_line = [int(num) for num in line_as_list]
        new_board.append(new_line)

    return new_board


# print(part_1())   # 63552
# print(part_2())   # 9020
