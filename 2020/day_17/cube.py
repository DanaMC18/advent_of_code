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
    new_dimensions = {i: INITIAL_STATE for i in range(z)}

    combos = list(product(range(x), range(y), range(z)))

    for combo in combos:
        x_coord = combo[0]
        y_coord = combo[1]
        z_coord = combo[2]
        neighbor_coords = _neighbor_coords([x_coord, y_coord, z_coord])

        current_val = dimensions.get(z_coord)[x_coord][y_coord]
        neighbor_vals = _neighbor_vals(neighbor_coords, dimensions)
        new_val = _get_new_val(current_val, neighbor_vals)

        new_dimensions[z_coord][x_coord][y_coord] = new_val

    return new_dimensions


def _get_new_val(current_val: list, neighbor_vals: list):
    """Determine new value based on neighbors."""
    actives = [nv for nv in neighbor_vals if nv == ACTIVE]

    if current_val == ACTIVE:
        return ACTIVE if len(actives) in [2, 3] else INACTIVE

    if current_val == INACTIVE:
        return ACTIVE if len(actives) == 3 else INACTIVE


def _neighbor_coords(coord: list):
    """Get neighbor coordinates of specified coordinate."""
    x = coord[0]
    y = coord[1]
    z = coord[2]

    x_coords = [x] + [x + 1] + [x - 1]
    y_coords = [y] + [y + 1] + [y - 1]
    z_coords = [z] + [z + 1] + [z - 1]

    combined = list(product(x_coords, y_coords, z_coords))

    return [c for c in combined if not set(c) == set(coord)]


def _neighbor_vals(coords: list, dimensions: dict):
    """Get values from coordinates."""
    values = list()

    for coord in coords:
        x = coord[0]
        y = coord[1]
        z = coord[2]

        dim = dimensions.get(z)

        if dim and x < len(dim) and y < len(dim):
            values.append(dim[x][y])
        else:
            values.append(INACTIVE)

    return values
