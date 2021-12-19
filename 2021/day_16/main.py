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
    packets = _decode_binary(binary, [])
    versions = [packet.get('version') for packet in packets]
    return sum(versions)


def _decode_binary(binary: str, packets: list) -> List[Dict[str, int]]:
    """Decode binary to get list of packet dicts.

    Args:
        binary (str): a binary string
        packets (list): a list of packet dicts: [{'version': num, 'value': num}]
    """
    if not int(binary, 2):
        return packets

    binary_version = binary[:3]
    binary_type = binary[3:6]

    if int(binary_type, 2) == LITERAL:
        val, new_binary = _decode_literal(binary)

        packet_dict = {'version': int(binary_version, 2), 'value': val}
        new_packets = packets + [packet_dict]
        return _decode_binary(new_binary, new_packets)
    else:
        mode = int(binary[6])
        mode_length = MODE_LENGTHS[mode]
        start = 7
        end = 7 + mode_length
        sub_packet_count = int(binary[start:end], 2)
        count = 1
        new_binary = binary[end:]

        while count <= sub_packet_count:
            count += 1
            packet_dict = {'version': int(binary_version, 2), 'value': None}
            new_packets = packets + [packet_dict]
            return _decode_binary(new_binary, new_packets)


def _decode_literal(binary: str) -> Tuple[int, str]:
    """Decode literal value from binary string.

    Returns a tuple of the binary value and remaining chars of binary string.

    Args:
        binary (str): a binary string
    """
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

    remaining_binary = binary[end:]
    return int(binary_num, 2), remaining_binary


def _load_input() -> str:
    """Load input data from text file."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), INPUT_FILE)
    f = open(filepath, 'r')
    data = f.read()
    f.close()
    return data.strip()


print(part_1())   # 886
