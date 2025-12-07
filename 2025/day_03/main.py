"""Day 3: Main solution file."""

import os
from typing import List

INPUT_FILE = 'input.txt'

def part_one() -> int:
    """Return the total output joltage."""
    data = _load_data()
    jolts = []

    for bank in data:
        max_jolt = max(bank[:-1])
        idx = bank.index(max_jolt) + 1

        second_max = max(bank[idx:])

        jolts.append(f'{max_jolt}{second_max}')

    return sum(int(jolt) for jolt in jolts)


def part_two() -> int:
    """Return the new total output joltage."""
    data = _load_data()
    jolts = []

    for bank in data:
        diff = len(bank) - 12
        bank_stack = []

        for digit in bank:
            while bank_stack and diff > 0 and bank_stack[-1] < digit:
                bank_stack.pop()
                diff -= 1
            bank_stack.append(digit)

        if diff > 0:
            bank_stack = bank_stack[:-diff]

        new_bank = bank_stack[:12]
        jolts.append(int(''.join(new_bank)))

    return sum(jolts)


# # # # # # # #
# LOAD INPUT  #
# # # # # # # #

def _load_data() -> List[str]:
    """Load data from text file. Returns a list strings."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), INPUT_FILE)
    f = open(filepath, 'r')
    data = f.read()
    f.close()

    return data.strip().split('\n')

# print(part_one()) # 17085
# print(part_two()) # 169408143086082
