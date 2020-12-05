"""Map traverser."""

import os

# from functools import reduce


MAP_TXT = 'tree_map.txt'
TREE = '#'


def get_tree_count(pattern: list):
    """Get number of trees when traversing the given map."""
    tree_matrix = _load_map()
    right_count = pattern[0]
    down_count = pattern[1]
    row = down_count
    index = 0
    tree_count = 0

    while row < len(tree_matrix):
        index = (index + right_count) % len(tree_matrix[row])
        if tree_matrix[row][index] == TREE:
            tree_count += 1
        row += down_count

    return tree_count


def _load_map():
    """Load map from txt file, return matrix."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), MAP_TXT)
    f = open(filepath, 'r')
    raw_map = f.read()
    f.close()
    return raw_map.strip().split('\n')


# patterns = [[3, 1], [1, 1], [5, 1], [7, 1], [1, 2]]

# print(get_tree_count([3, 1]))
# print(get_tree_count[1, 1])
# print(get_tree_count[5, 1])
# print(get_tree_count[7, 1])
# print(get_tree_count[1, 2])

# results = [get_tree_count(pattern) for pattern in patterns]
# print(results)
# print(reduce((lambda x, y: x * y), results))
