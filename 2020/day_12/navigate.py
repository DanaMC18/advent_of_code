"""Navigate module."""

import os


DIRS = ['N', 'E', 'S', 'W']
OPPS = {'N': 'S', 'S': 'N', 'W': 'E', 'E': 'W'}
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

        pos_neg = -1 if direction in ['S', 'W'] or \
            (direction == 'F' and curr_dir in ['S', 'W']) else 1

        if direction in ['N', 'S'] or (direction == 'F' and curr_dir in ['N', 'S']):
            north_south += (val * pos_neg)
        elif direction in ['W', 'E'] or (direction == 'F' and curr_dir in ['W', 'E']):
            east_west += (val * pos_neg)
        elif direction in ['R', 'L']:
            index = DIRS.index(curr_dir)
            rotation = int(val / 90) if direction == 'R' else int((360 - val) / 90)
            new_index = (index + rotation) % len(DIRS)
            curr_dir = DIRS[new_index]

    manhattan_distance = abs(east_west) + abs(north_south)
    print(f'abs({east_west}) + abs({north_south}) = {manhattan_distance}')

    return manhattan_distance


def waypoint_manhattan():
    """Get waypoint manhattan distance."""
    instructions = _load_instructions()
    curr_dirs = ['E', 'N']
    east_west = 0
    north_south = 0
    waypoint = {'N': 1, 'E': 10, 'S': 0, 'W': 0}

    for ins in instructions:
        direction = ins[:1]
        val = int(ins[1:])

        if direction in DIRS and direction in curr_dirs:
            waypoint[direction] += val
        elif direction in DIRS and direction not in curr_dirs:
            opp_dir = OPPS[direction]
            waypoint[opp_dir] -= val
        elif direction == 'F':
            for key in waypoint.keys():
                pos_neg = -1 if key in ['S', 'W'] else 1

                if key in ['N', 'S']:
                    north_south += (val * waypoint[key] * pos_neg)
                elif key in ['W', 'E']:
                    east_west += (val * waypoint[key] * pos_neg)
        elif direction in ['R', 'L']:
            new_dirs = []
            new_waypoint = {x: 0 for x in DIRS}
            for d in curr_dirs:
                index = DIRS.index(d)
                rotation = int(val / 90) if direction == 'R' else int((360 - val) / 90)
                new_index = (index + rotation) % len(DIRS)
                new_dir = DIRS[new_index]
                new_dirs.append(new_dir)
                new_waypoint[new_dir] = waypoint[d]
            curr_dirs = new_dirs
            waypoint = new_waypoint

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


# SOLUTION 2 | 30761
# waypoint_manhattan()
