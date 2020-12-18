"""Docking program module."""

import os
from itertools import product


BIT_FORMAT = '{0:036b}'
PROGRAM_TXT = 'program.txt'


def run_program(ver: str):
    """Run program."""
    raw_program = _load_program()
    program = _parse_program(raw_program)
    memory = dict()

    for mem_dict in program:
        if ver == 1:
            memory.update(_decode_mask(mem_dict))
        else:
            memory.update(_decode_mask_v2(mem_dict))

    return sum(memory.values())


def _decode_mask(mask: dict):
    """Decode mask and return new dict of memory values."""
    bitmask = mask.get('mask')
    mem_dict = {key: val for key, val in mask.items() if not key == 'mask'}
    new_mem_dict = dict()

    for mem in mem_dict.items():
        bit_str = BIT_FORMAT.format(mem[1])
        result_str = ''

        for i in range(len(bit_str)):
            new_bit = bit_str[i] if bitmask[i] == 'X' else bitmask[i]
            result_str += new_bit

        new_mem_dict[mem[0]] = int(result_str, 2)

    return new_mem_dict


def _decode_mask_v2(mask: dict):
    """Decode mask and return new dict of memory values."""
    bitmask = mask.get('mask')
    mem_dict = {key: val for key, val in mask.items() if not key == 'mask'}
    new_mem_dict = dict()

    for mem in mem_dict.items():
        address = BIT_FORMAT.format(mem[0])
        raw_result = ''

        for i in range(len(address)):
            new_bit = address[i] if bitmask[i] == '0' else bitmask[i]
            raw_result += new_bit

        indicies = [idx for idx in range(len(raw_result)) if raw_result[idx] == 'X']
        cart_prod = list(product('01', repeat=len(indicies)))

        for combo in cart_prod:
            count = 0
            result_str = raw_result

            for index in indicies:
                result_str = result_str[:index] + combo[count] + result_str[index + 1:]
                count += 1

            new_mem = int(result_str, 2)
            new_mem_dict[new_mem] = mem[1]

    return new_mem_dict


def _load_program():
    """Load program data from txt file."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), PROGRAM_TXT)
    f = open(filepath, 'r')
    program = f.read()
    f.close()
    return program.strip().split('\n')


def _parse_program(raw_program: list):
    """Parse raw program data a dict."""
    curr_mask = dict()
    masks = list()
    splitter = ' = '

    for p in raw_program:
        if 'mask' in p:
            split_pea = p.split(splitter)
            mask = split_pea[1]
            if curr_mask:
                masks.append(curr_mask)
                curr_mask = dict()
            curr_mask['mask'] = mask
        else:
            split_memory = p.split(splitter)
            mem = int(split_memory[0][4:-1])
            val = int(split_memory[1])
            curr_mask[mem] = val

    if curr_mask:
        masks.append(curr_mask)

    return masks


# SOLUTION 1 | 4297467072083
# print(run_program(1))


# SOLUTION 2 | 5030603328768
# print(run_program(2))
