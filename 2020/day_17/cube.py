"""Cube module."""

from itertools import product

ACTIVE = '#'
INACTIVE = '.'
INITIAL_COORDS = [3, 3, 1]
INITIAL_STATE = [
    ['.', '#', '.'],
    ['.', '.', '#'],
    ['#', '#', '#']
]

DIRECTIONS = {
    'right': [0, 1, 0],
    'left': [0, -1, 0],
    'down': [1, 0, 0],
    'up': [-1, 0, 0],
    'forward': [0, 0, 1],
    'backward': [0, 0, -1]
}


def part_one():
    """Part one."""
    x = 3
    y = 3
    z = 1
    dimensions = {0: INITIAL_STATE}
    new_dimensions = dict()

    combos = list(product(range(x), range(y)))
    neighbor_matrix = list()

    for combo in combos:
        x_coord = combo[0]
        y_coord = combo[1]
        neighbor_matrix.append(_neighbor_coords([x_coord, y_coord, z]))

    for c in combos:
        x_coord = combo[0]
        y_coord = combo[1]
        neighbor_coords = neighbor_matrix[x_coord][y_coord]


def _get_new_val(current_val: str, dimension: list, neighbor_coords: list):
    """Determine new value based on neighbors."""
    values = _neighbor_vals(neighbor_coords, dimension)
    actives = [v for v in values if v == ACTIVE]

    if current_val == ACTIVE:
        return ACTIVE if len(actives) in [2, 3] else INACTIVE

    if current_val == INACTIVE:
        return ACTIVE if len(actives) == 3 else INACTIVE


def _neighbor_coords(coord: list):
    """Get neighbor coordinates of specified coordinate."""
    x = coord[0]
    y = coord[1]
    z = coord[2]

    x_coords = [x + 1] + [x - 1]
    y_coords = [y + 1] + [y - 1]
    z_coords = [z + 1] + [z - 1]

    return list(product(x_coords, y_coords, z_coords))


def _neighbor_vals(coords: list, dimension: list):
    """Get values from coordinates."""
    values = list()
    for coord in coords:
        x = coord[0]
        y = coord[1]
        values.append(dimension[x][y])
    return values
