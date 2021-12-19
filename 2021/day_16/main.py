"""Main solution file: day 16."""

from numpy import prod
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
    _, versions = _decode_binary(binary, [], [])
    return sum(versions)


def part_2() -> int:
    """Return result of performing operation on values of subpackets."""
    input = _load_input()
    binary = ''.join([HEX_MAP[char] for char in input])
    values, versions = _decode_binary(binary, [], [])
    return values
    # return packets


def _decode_binary(
    binary: str,
    values: list,
    versions: list,
) -> Tuple[List[int], List[int]]:
    """Decode binary to get list of packet values and packet versions

    Args:
        binary (str): a binary string
        values (list): list of subpacket values
        versions (list): list of versions
    """
    if not binary or not int(binary, 2):
        return values, versions

    binary_version = binary[:3]
    binary_type = binary[3:6]
    version_num = int(binary_version, 2)
    operator_id = int(binary_type, 2)

    new_versions = versions + [version_num]

    if operator_id == LITERAL:
        val, new_binary = _decode_literal(binary)

        new_values = values + [val]
        return _decode_binary(new_binary, new_values, new_versions)
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
            return _decode_binary(new_binary, values, new_versions)
            # vals, _ = _decode_binary(new_binary, values, new_versions)
            # new_values = _execute_op(operator_id, vals)
            # return [new_values], versions


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


def _load_input() -> str:
    """Load input data from text file."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), INPUT_FILE)
    f = open(filepath, 'r')
    data = f.read()
    f.close()
    return data.strip()


print(part_1())   # 886
# print(part_2())
