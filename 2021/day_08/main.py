"""Main solution file: Day 8."""

import os
from typing import List

INPUT_FILE = 'input.txt'


def part_1() -> int:
    """Return num of output values with a unique length."""
    input = _load_input()
    outputs = [item.split(' | ')[1] for item in input]
    lengths = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    unique_lengths = [ln for ln in lengths if lengths.count(ln) == 1]
    segment_count = 0

    for segment in outputs:
        segment_list = segment.split(' ')
        filtered = [s for s in segment_list if len(s) in unique_lengths]
        segment_count += len(filtered)

    return segment_count


def part_2() -> int:
    """Return sum of all output values."""
    input = _load_input()
    outputs = list()

    for item in input:
        left, right = item.split(' | ')
        patterns = left.split(' ')
        decoded_patterns = _decode_patterns(patterns)

        pattern_list = [''.join(sorted(list(dp))) for dp in decoded_patterns]
        decoded_output = ''

        for output in right.split(' '):
            sorted_output = ''.join(sorted(output))
            num = pattern_list.index(sorted_output)
            decoded_output += str(num)

        outputs.append(int(decoded_output))

    return sum(outputs)


def _decode_patterns(patterns: List[str]) -> List[str]:
    """Decode patterns to get numbers."""
    lengths = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

    # unique numbers
    one = [p for p in patterns if len(p) == lengths[1]].pop()
    four = [p for p in patterns if len(p) == lengths[4]].pop()
    seven = [p for p in patterns if len(p) == lengths[7]].pop()
    eight = [p for p in patterns if len(p) == lengths[8]].pop()

    # list of patterns of lenghts 5 and 6
    fives = [p for p in patterns if len(p) == 5]
    sixes = [p for p in patterns if len(p) == 6]

    three = [f for f in fives if len(set(f) - set(seven)) == 2].pop()
    six = [s for s in sixes if len(set(one) - set(s))].pop()

    top_left = (set(four) - set(three)).pop()
    top_right = (set(one) - set(six)).pop()
    bottom_right = (set(one) - set(top_right)).pop()

    nine = [s for s in sixes if set(s) == set(three + top_left)].pop()
    bottom_left = (set(six) - set(nine)).pop()

    zero = [s for s in sixes if s not in [six, nine]].pop()
    two = ''.join(set(eight) - set(top_left) - set(bottom_right))
    five = ''.join(set(eight) - set(top_right) - set(bottom_left))

    return [zero, one, two, three, four, five, six, seven, eight, nine]


def _load_input() -> List[str]:
    """Load input data from txt file."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), INPUT_FILE)
    f = open(filepath, 'r')
    data = f.read()
    f.close()

    return data.strip().split('\n')


print(part_1())     # 534
print(part_2())     # 1070188
