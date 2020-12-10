"""Handheld module."""

import os


BOOT_TXT = 'boot.txt'

# Operations:
ACC = 'acc'
JMP = 'jmp'
NOP = 'nop'


def _load_boot():
    """Load instructions from boot.txt."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), BOOT_TXT)
    f = open(filepath, 'r')
    instructions = f.read()
    f.close()
    return instructions.strip().split('\n')


# SOLUTION 01 | 1832
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

# print(get_last_value())


# SOLUTION 02 | 662
def fix_bug():
    """Find and fix the wrong instruction."""
    orig_instructions = _load_boot()

    for index in range(len(orig_instructions)):
        dupe = orig_instructions.copy()
        instruction = dupe[index]
        new_instruction = ''

        if ACC in instruction:
            continue

        if JMP in instruction:
            new_instruction = instruction.replace(JMP, NOP)
        elif NOP in instruction:
            new_instruction = instruction.replace(NOP, JMP)

        dupe[index] = new_instruction
        acc_val = _test_fix(dupe)

        if acc_val:
            return acc_val


def _test_fix(instructions: list):
    """Test new set of instructions."""
    acc_val = 0
    curr_index = 0
    last_index = len(instructions) - 1
    visited = list()

    while curr_index != last_index:
        if curr_index in visited:
            return False

        visited.append(curr_index)
        instruction = instructions[curr_index]
        op, val = instruction.split(' ')

        if op == ACC:
            acc_val += int(val)
            curr_index += 1
        elif op == JMP:
            curr_index += int(val)
        elif op == NOP:
            curr_index += 1

    return acc_val

# print(fix_bug())
