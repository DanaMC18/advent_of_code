"""Binary Boarding."""

import os


LOWER_CODES = ['F', 'L']
PASSES_TXT = 'passes.txt'
SEAT_COLS = list(range(8))
SEAT_ROWS = list(range(128))


def get_seats():
    """Determine seat using binary space partitioning."""
    seats = []
    boarding_passes = _load_passes()

    for boarding_code in boarding_passes:
        col_code = boarding_code[7:]
        row_code = boarding_code[:7]
        seat = {
            'col': _decode(col_code, SEAT_COLS),
            'row': _decode(row_code, SEAT_ROWS)
        }
        seats.append(seat)

    return seats


def highest_seat_id():
    """Get highest seat_id."""
    seats = get_seats()
    highest_seat_id = 0

    for seat in seats:
        seat_id = _seat_id(**seat)
        if seat_id > highest_seat_id:
            highest_seat_id = seat_id

    return highest_seat_id


def _decode(code: str, seats=[]):
    """Determine seat based on boarding pass seat code."""
    if len(code) == 0:
        return seats[0]

    letter = code[:1]
    partition_point = int(len(seats) / 2)

    new_code = code[1:]
    new_seats = \
        seats[:partition_point] if letter in LOWER_CODES else seats[partition_point:]

    return _decode(new_code, new_seats)


def _load_passes():
    """Load boarding pass codes from txt file."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), PASSES_TXT)
    f = open(filepath, 'r')
    passes = f.read()
    f.close()
    return passes.strip().split('\n')


def _seat_id(col: int, row: int):
    """Determine seat_id from seat col and row."""
    return row * 8 + col


# print(get_seats())
# print(highest_seat_id())
