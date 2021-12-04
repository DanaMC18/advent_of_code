"""Main solution file: day 03."""

import os
from typing import List, Tuple

INPUT_FILE = 'input.txt'


def part_1():
    """Determine the 'power consumption'."""
    epsilon, gamma = _get_epsilon_gamma_rates()

    epsilon_decimal = int(epsilon, 2)
    gamma_decimal = int(gamma, 2)

    return epsilon_decimal * gamma_decimal


def _get_epsilon_gamma_rates() -> Tuple[str, str]:
    """Determine epsilon (min) and gamma (max) rates from input."""
    epsilon = gamma = ''
    input = _load_input()
    size = len(input[0])

    for i in range(size):
        bit_list = list()

        for num in input:
            bit = num[i]
            bit_list.append(bit)

        zero_count = bit_list.count('0')
        one_count = bit_list.count('1')

        epsilon += '1' if zero_count > one_count else '0'
        gamma += '0' if zero_count > one_count else '1'

    return epsilon, gamma


def _load_input() -> List[str]:
    """Load input data from text file."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), INPUT_FILE)
    f = open(filepath, 'r')
    data = f.read()
    return data.strip().split('\n')


print(part_1())   # 4160394
