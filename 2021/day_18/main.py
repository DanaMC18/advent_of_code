"""Main solution file: day 18."""

from functools import reduce
import json
import os

INPUT_FILE = 'input.txt'


def part_1():
    """Return the magnitude of the snailfish addition."""
    input = _load_input()
    added_input = reduce(_add, input)

    # left_num, exploded, right_num = _explode(added_input)
    return added_input


def _add(left, right):
    """Add left and right lists together."""
    new_num = [left, right]

    # reduce
    while True:
        left_num, exploded, right_num = _explode(new_num)
        if exploded:
            new_num = exploded
            continue

        split = _split(new_num)
        if split:
            new_num = split
            continue

        if not exploded and not split:
            break

    return new_num


def _is_num(val):
    """Check if value is a number or not."""
    return isinstance(val, int)


def _explode(input):
    """Explode snailfish number."""
    depth = 0
    nested = input.copy()
    prev_nest = input.copy()

    # this check might need to happen during addition step above
    while depth < 4:
        if _is_num(nested):
            break
        prev_nest = nested.copy()
        nested = nested[0]
        depth += 1

    exploded = []
    left_num = None
    right_num = None

    if not _is_num(nested):
        idx = prev_nest.index(nested)
        left = [item for item in prev_nest[:idx] if _is_num(item)]
        right = [item for item in prev_nest[idx:] if _is_num(item)]

        if not left:
            exploded.append(0)
        else:
            left_num = left_num[-1]
            new_num = left_num + nested[0]
            exploded.append(new_num)

        if not right:
            exploded.append(0)
        else:
            right_num = right_num[0]
            new_num = right_num + nested[1]
            exploded.append(new_num)

    # prob don't need to change left_num and right_num and return them
    # if this is done during the addition step above
    return left_num, exploded, right_num


def _split(num):
    """Split number into a new list."""
    if not _is_num(num) or num < 10:
        return []

    left_num = num // 2
    right_num = num // 2

    if num % 2:
        right_num += 1

    return [left_num, right_num]


def _load_input():
    """Load input data from text file."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), INPUT_FILE)
    f = open(filepath, 'r')
    data = list(map(json.loads, f.read().splitlines()))
    f.close()
    return data


print(part_1())
