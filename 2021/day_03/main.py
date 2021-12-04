"""Main solution file: day 03."""

import os
from typing import List, Tuple

INPUT_FILE = 'input.txt'


def part_1() -> int:
    """Determine the 'power consumption'."""
    input = _load_input()
    epsilon, gamma = _get_epsilon_gamma_rates(input)

    epsilon_decimal = int(epsilon, 2)
    gamma_decimal = int(gamma, 2)

    return epsilon_decimal * gamma_decimal


def part_2() -> int:
    """Determine the 'life support rating'."""
    input = _load_input()
    co2_scrubber_rating = _life_support_rate_binary(input, 0, 'epsilon')
    oxygen_gen_rating = _life_support_rate_binary(input, 0, 'gamma')

    co2_decimal = int(co2_scrubber_rating, 2)
    oxygen_decimal = int(oxygen_gen_rating, 2)

    return co2_decimal * oxygen_decimal


def _life_support_rate_binary(input: List[str], index: int, rate_type: str) -> str:
    """Recursively determine 'CO2 scrubber rating' or 'oxygen generator rating'.

    Returns a binary num.

    Args:
      input (list): list of binary numbers
      index (int): position at which to check a bit value of binary number
      rate_type (str): either 'epsilon' or 'gamma'
        - if 'epsilon', get 'CO2 scrubber rating'
        - if 'gamma', get 'oxygen generator rating'
    """
    if len(input) == 1:
        return input[0]

    epsilon, gamma = _get_epsilon_gamma_rates(input)

    bit = gamma[index] if rate_type == 'gamma' else epsilon[index]

    new_input = [num for num in input if num[index] == bit]
    index += 1

    return _life_support_rate_binary(new_input, index, rate_type)


def _get_epsilon_gamma_rates(input: List[str]) -> Tuple[str, str]:
    """Determine epsilon (min) and gamma (max) rates from input."""
    epsilon = gamma = ''
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


# print(part_1())   # 4160394
# print(part_2())     # 4125600
