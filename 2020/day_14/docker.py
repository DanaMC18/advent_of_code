"""Docking program module."""

import os


BIT_FORMAT = '{0:036b}'
PROGRAM_TXT = 'program.txt'


def run_program():
    """Run program."""
    raw_program = _load_program()
    program = _parse_program(raw_program)
    memory = dict()

    for mem_dict in program:
        memory.update(_decode_mask(mem_dict))

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
# print(run_program())
