"""Main solution file: day 16."""

from numpy import prod
import os
from typing import List, Tuple

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


# # # # # #
# PART 1  #
# # # # # #

def part_1() -> int:
    """Get total version value of input."""
    input = _load_input()
    binary = ''.join([HEX_MAP[char] for char in input])
    versions = _decode_binary(binary, [])
    return sum(versions)


def _decode_binary(binary: str, versions: list) -> List[int]:
    """Recursively decode binary to get list of packet versions

    Args:
        binary (str): a binary string
        versions (list): list of versions
    """
    if not binary or not int(binary, 2):
        return versions

    binary_version = binary[:3]
    binary_type = binary[3:6]
    version_num = int(binary_version, 2)
    operator_id = int(binary_type, 2)

    new_versions = versions + [version_num]

    if operator_id == LITERAL:
        _, new_binary = _decode_literal(binary)

        return _decode_binary(new_binary, new_versions)
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
            return _decode_binary(new_binary, new_versions)


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


# # # # # #
# PART 2  #
# # # # # #


def part_2() -> int:
    """Return result of performing operation on values of subpackets."""
    input = _load_input()
    binary = ''.join([HEX_MAP[char] for char in input])
    _, val = _parse(binary)
    return val


def _parse(binary: str):
    """Decode binary to get value."""
    binary = binary[3:]

    type_id = int(binary[:3], 2)
    binary = binary[3:]

    if type_id == LITERAL:
        bit = ""
        while True:
            bit += binary[1:5]
            prefix = int(binary[0])
            binary = binary[5:]
            if not prefix:
                break

        val = int(bit, 2)
        return (binary, val)
    else:
        mode = int(binary[0])
        mode_len = MODE_LENGTHS[mode]
        binary = binary[1:]
        subpackets = []

        if mode:
            sub_length = binary[:mode_len]
            binary = binary[11:]
            subpacket_count = int(sub_length, 2)
            for _ in range(subpacket_count):
                new_binary, val = _parse(binary)
                binary = new_binary
                subpackets.append(val)
        else:
            sub_length = binary[:mode_len]
            sub_length = int(sub_length, 2)

            binary = binary[mode_len:]
            sub_binary = binary[:sub_length]

            while sub_binary:
                new_binary, val = _parse(sub_binary)
                sub_binary = new_binary
                subpackets.append(val)

            binary = binary[sub_length:]

        new_val = _execute_op(type_id, subpackets)
        return binary, new_val


def _execute_op(type_id: int, values: List[int]):
    """Execute operation on list of values."""
    if type_id == 0:
        return sum(values)

    if type_id == 1:
        return prod(values)

    if type_id == 2:
        return min(values)

    if type_id == 3:
        return max(values)

    if type_id == 4:
        return values

    if type_id == 5:
        is_greater_than = values[0] > values[1]
        return int(is_greater_than)

    if type_id == 6:
        is_less_than = values[0] < values[1]
        return int(is_less_than)

    if type_id == 7:
        is_equal = values[0] == values[1]
        return int(is_equal)


# # # # # # # #
# LOAD INPUT  #
# # # # # # # #


def _load_input() -> str:
    """Load input data from text file."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), INPUT_FILE)
    f = open(filepath, 'r')
    data = f.read()
    f.close()
    return data.strip()


# print(part_1())   # 886
# print(part_2())   # 184487454837
