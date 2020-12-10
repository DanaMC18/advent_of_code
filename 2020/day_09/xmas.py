"""XMAS module."""

import json
import os
from itertools import product

DATA_JSON = 'data.json'


def find_corruption():
    """Find the corrupt number in the XMAS data set."""
    data = _load_data()
    preamble = data[:25]

    for num in data[25:]:
        pairs = list(product(preamble, preamble))
        unequal_pairs = [pair for pair in pairs if pair[0] != pair[1]]
        complementary_pairs = [pair for pair in unequal_pairs if sum(pair) == num]

        if not complementary_pairs:
            return num

        preamble.append(num)
        preamble = preamble[1:]


def _load_data():
    """Load data json file."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), DATA_JSON)
    f = open(filepath, "r")
    return json.load(f)


# SOLUTION 01 | 90433990
# print(find_corruption())
