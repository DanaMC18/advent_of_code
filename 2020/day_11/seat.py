"""Seat module."""

import os


EMPTY = 'L'
FLOOR = '.'
OCCUPIED = '#'
SEAT_TXT = 'seats.txt'

adjacent_moves = [
    [+1, 0], [-1, 0], [0, +1], [0, -1], [+1, +1], [+1, -1], [-1, -1], [-1, +1]
]


def count_occupied_seats():
    """Get number of occupied seats after seats no longer change."""
    prev_seats = _load_seats()
    new_seats = _get_seats(prev_seats)

    while prev_seats != new_seats:
        prev_seats = new_seats
        new_seats = _get_seats(prev_seats)

    occupied_count = 0

    for row in new_seats:
        occupied_seats = [seat for seat in row if seat == OCCUPIED]
        occupied_count += len(occupied_seats)

    return occupied_count


def _are_all_seats_empty(coords: list, seats: list):
    """Check if all seats in list of coordinates are empty."""
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


def _are_seats_occupied(coords: list, seats: list):
    """Check to see if four or more seats in cooordinates are occupied."""
    seat_values = []

    for coord in coords:
        row = coord[0]
        col = coord[1]

        if row == -1 or col == -1:
            continue
        elif row >= len(seats) or col >= len(seats[0]):
            continue

        seat_values.append(seats[row][col])

    occupied_seats = [seat for seat in seat_values if seat == OCCUPIED]

    return len(occupied_seats) > 3


def _get_adjacent_coords(seat: list):
    """Get coordinates for adjacent seats."""
    adjacent_seats = []
    row = seat[0]
    col = seat[1]

    for move in adjacent_moves:
        new_row = row + move[0]
        new_col = col + move[1]
        adjacent_seats.append([new_row, new_col])

    return adjacent_seats


def _get_seats(all_seats: list):
    """Get one round of seats."""
    new_seats = [seat.copy() for seat in all_seats]

    for row_index in range(len(all_seats)):
        row = all_seats[row_index]

        for col_index in range(len(row)):
            if all_seats[row_index][col_index] == FLOOR:
                continue

            seat = [row_index, col_index]
            adjacent_seats = _get_adjacent_coords(seat)

            if _are_all_seats_empty(adjacent_seats, all_seats):
                new_seats[row_index][col_index] = OCCUPIED

            if _are_seats_occupied(adjacent_seats, all_seats):
                new_seats[row_index][col_index] = EMPTY

    return new_seats


def _load_seats():
    """Load seats from txt file."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), SEAT_TXT)
    f = open(filepath, 'r')
    seats = f.read()
    f.close()
    return [list(seat) for seat in seats.strip().split('\n')]


# SOLUTION 1 | 2424
# print(count_occupied_seats())
