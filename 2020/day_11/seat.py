"""Seat module."""

import os

from utils.enum import enum


EMPTY = 'L'
FLOOR = '.'
MOVE_NAMES = enum(
    'move_names',
    DOWN='DOWN',
    UP='UP',
    RIGHT='RIGHT',
    LEFT='LEFT',
    UP_RIGHT='UP_RIGHT',
    UP_LEFT='UP_LEFT',
    DOWN_RIGHT='DOWN_RIGHT',
    DOWN_LEFT='DOWN_LEFT'
)
MOVES = enum(
    'moves',
    DOWN=[+1, 0],
    UP=[-1, 0],
    RIGHT=[0, +1],
    LEFT=[0, -1],
    UP_RIGHT=[-1, +1],
    UP_LEFT=[-1, -1],
    DOWN_RIGHT=[+1, +1],
    DOWN_LEFT=[+1, -1]
)
OCCUPIED = '#'
RULE_TYPES = enum('rule_types', ADJ='adj', LINE='line')
SEAT_TXT = 'seats.txt'


def count_occupied_seats(rule_type: str):
    """Get number of occupied seats after seats no longer change."""
    prev_seats = _load_seats()
    new_seats = _get_seats(prev_seats, rule_type)
    print(new_seats)

    while prev_seats != new_seats:
        prev_seats = new_seats
        new_seats = _get_seats(prev_seats, rule_type)

    occupied_count = 0

    for row in new_seats:
        occupied_seats = [seat for seat in row if seat == OCCUPIED]
        occupied_count += len(occupied_seats)

    return occupied_count


def _are_adj_seats_occupied(coords: list, seats: list):
    """Check to see if four or more adj seats in coordinates are occupied."""
    seat_values = []

    for coord in coords:
        row = coord[0]
        col = coord[1]

        if row < 0 or col < 0:
            continue
        elif row >= len(seats) or col >= len(seats[0]):
            continue

        seat_values.append(seats[row][col])

    occupied_seats = [seat for seat in seat_values if seat == OCCUPIED]

    return len(occupied_seats) >= 4


def _are_all_seats_empty(coords: list, seats: list):
    """Check if all adjacent seats in list of coordinates are empty."""
    for coord in coords:
        row = coord[0]
        col = coord[1]

        if row == -1 or col == -1:
            continue
        elif row >= len(seats) or col >= len(seats[0]):
            continue

        if seats[row][col] == OCCUPIED:
            return False

    return True


def _get_adjacent_coords(seat: list):
    """Get coordinates for adjacent seats."""
    coords = []
    row = seat[0]
    col = seat[1]

    for move in MOVES:
        new_row = row + move[0]
        new_col = col + move[1]
        coords.append([new_row, new_col])

    return coords


def _get_line_coords(seat: list, all_seats: list):
    """Get all coordinates in given seat's line of sight."""
    coords = {move: [] for move in MOVE_NAMES._fields}
    row = seat[0]
    col = seat[1]

    # VERTICAL UP AND DOWN
    for index in range(row):
        new_row = row + MOVES.UP[0] - index
        coords[MOVE_NAMES.UP].append([new_row, col])

    for index in range(len(all_seats) - row)[:-1]:
        new_row = row + MOVES.DOWN[0] + index
        coords[MOVE_NAMES.DOWN].append([new_row, col])

    # HORIZONTAL LEFT AND RIGHT
    for index in range(col):
        new_col = col + MOVES.LEFT[1] - index
        coords[MOVE_NAMES.LEFT].append([row, new_col])

    for index in range(len(all_seats[row]) - col)[:-1]:
        new_col = col + MOVES.RIGHT[1] + index
        coords[MOVE_NAMES.RIGHT].append([row, new_col])

    # DIAG UP LEFT
    curr_row = row
    curr_col = col
    while curr_row != 0 and curr_col != 0:
        curr_row += MOVES.UP_LEFT[0]
        curr_col += MOVES.UP_LEFT[1]
        coords[MOVE_NAMES.UP_LEFT].append([curr_row, curr_col])

    # DIAG UP RIGHT
    curr_row = row
    curr_col = col
    while curr_row != 0 and curr_col < len(all_seats[row]):
        curr_row += MOVES.UP_RIGHT[0]
        curr_col += MOVES.UP_RIGHT[1]
        coords[MOVE_NAMES.UP_RIGHT].append([curr_row, curr_col])

    # DIAG DOWN LEFT
    curr_row = row
    curr_col = col
    while curr_row < len(all_seats) and curr_col != 0:
        curr_row += MOVES.DOWN_LEFT[0]
        curr_col += MOVES.DOWN_LEFT[1]
        coords[MOVE_NAMES.DOWN_LEFT].append([curr_row, curr_col])

    # DIAG DOWN RIGHT
    curr_row = row
    curr_col = col
    while curr_row < len(all_seats) and curr_col < len(all_seats[row]):
        curr_row += MOVES.DOWN_RIGHT[0]
        curr_col += MOVES.DOWN_RIGHT[1]
        coords[MOVE_NAMES.DOWN_RIGHT].append([curr_row, curr_col])

    return coords


def _get_nearest_seats(coords: dict, seats: list):
    """Check to see if five or more of the first seats in line of sight are occupied."""
    first_seat_in_dir = {}
    directions = coords.keys()

    for d in directions:
        dir_coords = coords.get(d)

        for coord in dir_coords:
            if first_seat_in_dir.get(d):
                continue

            row = coord[0]
            col = coord[1]

            if row < 0 or col < 0:
                continue
            elif row >= len(seats) or col >= len(seats[row]):
                continue

            seat = seats[row][col]

            if seat == FLOOR:
                continue

            first_seat_in_dir[d] = seat

    occupied_seats = [k for k, v in first_seat_in_dir.items() if v == OCCUPIED]
    empty_seats = [k for k, v in first_seat_in_dir.items() if v == EMPTY]

    if len(occupied_seats) >= 5:
        return EMPTY
    if len(empty_seats) == len(first_seat_in_dir.keys()):
        return OCCUPIED


def _get_seats(seats: list, rule_type: str):
    """Get one round of seats."""
    new_seats = [s.copy() for s in seats]

    for row_index in range(len(seats)):
        row = seats[row_index]

        for col_index in range(len(row)):
            if seats[row_index][col_index] == FLOOR:
                continue

            seat = [row_index, col_index]

            if rule_type == RULE_TYPES.ADJ:
                coords = _get_adjacent_coords(seat)

                if _are_all_seats_empty(coords, seats):
                    new_seats[row_index][col_index] = OCCUPIED

                if _are_adj_seats_occupied(coords, seats):
                    new_seats[row_index][col_index] = EMPTY

            elif rule_type == RULE_TYPES.LINE:
                coords = _get_line_coords(seat, seats)
                new_seat = _get_nearest_seats(coords, seats)

                if new_seat:
                    new_seats[row_index][col_index] = new_seat

    return new_seats


def _load_seats():
    """Load seats from txt file."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), SEAT_TXT)
    f = open(filepath, 'r')
    seats = f.read()
    f.close()
    return [list(seat) for seat in seats.strip().split('\n')]


# SOLUTION 1 | 2424
# print(count_occupied_seats(RULE_TYPES.ADJ))


# SOLUTION 2 | 2208
# Takes a long time to run
# print(count_occupied_seates(RULE_TYPES.LINE))
