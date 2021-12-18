"""Main solution file: day 16."""

import os
from typing import Dict, List, Tuple

HEX_MAP = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}
INPUT_FILE = 'input.txt'
LITERAL = 4
MODE_LENGTHS = [15, 11]


def part_1() -> int:
    """Get total version value of input."""
    input = _load_input()
    binary = ''.join([HEX_MAP[char] for char in input])
    return _decode_binary(binary, [])


def _decode_binary(binary: str, packets: list) -> List[Dict[str, int]]:
    """Decode binary string."""
    if not binary:
        return packets

    binary_version = binary[:3]
    binary_type = binary[3:6]

    if int(binary_type, 2) == LITERAL:
        val, end_index = _decode_literal(binary)
        zero_count = 4 - (end_index % 4)
        end_index += zero_count
    else:
        mode = binary[6]
        mode_length = MODE_LENGTHS[mode]

    new_binary = binary[end_index:]

    packet_dict = {'version': int(binary_version, 2), 'value': val}
    new_packets = packets + [packet_dict]

    return _decode_binary(new_binary, new_packets)


def _decode_literal(binary: str) -> Tuple[int, int]:
    """Decode literal value from binary string."""
    binary_num = ''
    is_last = False
    start = 6

    while not is_last:
        end = start + 5
        bit = binary[start:end]
        prefix = int(bit[0])
        is_last = not prefix
        num = bit[1:]
        binary_num += num
        start = end

    return int(binary_num, 2), end - 1


def _decode_operator(binary: str) -> Tuple[int, int]:
    """Decode operator value from binary string."""
    mode = binary[6]
    mode_length = MODE_LENGTHS[mode]
    start = 7
    end = 7 + mode_length
    sub_packet_length = int(binary[start:end], 2)


def _load_input() -> str:
    """Load input data from text file."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), INPUT_FILE)
    f = open(filepath, 'r')
    data = f.read()
    f.close()
    return data.strip()


print(part_1())
