"""Map traverser."""

import os


MAP_TXT = 'tree_map.txt'
TREE = '#'

# movements = {
#     'right': [0, 1],
#     'down': [1, 0]
# }


def get_tree_count(pattern: list):
    """Get number of trees when traversing the given map."""
    tree_matrix = _load_map()
    right_count = pattern[0]
    # down_count = pattern[1]
    index = 0
    tree_count = 0

    for row in tree_matrix[1:]:
        index = (index + right_count) % len(row)
        print(row[index])

        if row[index] == TREE:
            tree_count += 1

    return tree_count


def _load_map():
    """Load map from txt file, return matrix."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), MAP_TXT)
    f = open(filepath, 'r')
    raw_map = f.read()
    f.close()
    return raw_map.strip().split('\n')


# print(get_tree_count([3, 1]))
