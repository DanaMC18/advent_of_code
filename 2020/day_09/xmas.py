"""XMAS module."""

import json
import os
from itertools import product

DATA_JSON = 'data.json'


def find_corruption(data: list):
    """Find the corrupt number in the XMAS data set."""
    preamble = data[:25]

    for num in data[25:]:
        pairs = list(product(preamble, preamble))
        unequal_pairs = [pair for pair in pairs if pair[0] != pair[1]]
        complementary_pairs = [pair for pair in unequal_pairs if sum(pair) == num]

        if not complementary_pairs:
            return num

        preamble.append(num)
        preamble = preamble[1:]


def find_weakness(corrupt_num: int, data: list):
    """Find the encryption weakness in XMAS data set."""
    curr_index = 0
    start_index = 0
    weak_list = list()

    while start_index < len(data):
        num = data[curr_index]
        weak_list.append(num)

        if sum(weak_list) == corrupt_num and corrupt_num not in weak_list:
            return weak_list

        if sum(weak_list) > corrupt_num:
            start_index += 1
            curr_index = start_index
            weak_list = list()
        else:
            curr_index += 1


def _load_data():
    """Load data json file."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), DATA_JSON)
    f = open(filepath, "r")
    return json.load(f)


# SOLUTION 01 | 90433990
# xmas_data = _load_data()
# corrupt_number = find_corruption(xmas_data)
# print(corrupt_number)

# SOLUTION 2 | 3289338 + 8402308 = 11691646
# weakness_list = find_weakness(corrupt_number, xmas_data)
# print(min(weakness_list) + max(weakness_list))
