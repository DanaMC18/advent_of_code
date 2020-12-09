"""Handheld module."""

import os


BOOT_TXT = 'boot.txt'

# Operations:
ACC = 'acc'
JMP = 'jmp'
NOP = 'nop'


def get_last_value():
    """Get last value of accumulator before a second loop iterates."""
    accumulator_val = 0
    curr_index = 0
    instructions = _load_boot()
    visited = list()

    while curr_index not in visited:
        visited.append(curr_index)
        instruction = instructions[curr_index]
        op, val = instruction.split(' ')
        if op == ACC:
            accumulator_val += int(val)
            curr_index += 1
        elif op == JMP:
            curr_index += int(val)
        elif op == NOP:
            curr_index += 1

    return accumulator_val


def _load_boot():
    """Load instructions from boot.txt."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), BOOT_TXT)
    f = open(filepath, 'r')
    instructions = f.read()
    f.close()
    return instructions.strip().split('\n')


# SOLUTION 01 | 1832
# print(get_last_value())
