"""Navigate module."""

import os


DIRS = ['N', 'E', 'S', 'W']
INSTRUCTIONS_TXT = 'instructions.txt'


def manhattan_dist():
    """Get manhattan distance."""
    instructions = _load_instructions()
    curr_dir = 'E'
    east_west = 0
    north_south = 0

    for ins in instructions:
        direction = ins[:1]
        val = int(ins[1:])

        pos_neg = -1 if \
            direction in ['S', 'W'] or (direction == 'F' and curr_dir in ['S', 'W']) \
            else 1

        if direction in ['N', 'S'] or (direction == 'F' and curr_dir in ['N', 'S']):
            north_south += (val * pos_neg)
        elif direction in ['W', 'E'] or (direction == 'F' and curr_dir in ['W', 'E']):
            east_west += (val * pos_neg)
        elif direction in ['R', 'L']:
            index = DIRS.index(curr_dir)
            rotation = int(val / 90) if direction == 'R' else int((360 - val) / 90)
            new_index = (index + rotation) % len(DIRS)
            curr_dir = DIRS[new_index]
        # print(f'{ins}: NS: {north_south}, WE: {east_west}, curr_dir: {curr_dir}')

    manhattan_distance = abs(east_west) + abs(north_south)
    print(f'abs({east_west}) + abs({north_south}) = {manhattan_distance}')

    return manhattan_distance


def _load_instructions():
    """Load instructions from text file."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), INSTRUCTIONS_TXT)
    f = open(filepath, 'r')
    instructions = f.read()
    f.close()
    return instructions.strip().split('\n')


# SOLUTION 1 | 508
# manhattan_dist()
