"""Main solution file: Day 8."""

import os
from typing import List

INPUT_FILE = 'input.txt'


def part_1() -> int:
    """Return num of output values with a unique length."""
    outputs = _load_input()
    lengths = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    unique_lengths = [ln for ln in lengths if lengths.count(ln) == 1]
    segment_count = 0

    for segment in outputs:
        segment_list = segment.split(' ')
        filtered = [s for s in segment_list if len(s) in unique_lengths]
        segment_count += len(filtered)

    return segment_count


def _load_input() -> List[str]:
    """Load input data from txt file."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), INPUT_FILE)
    f = open(filepath, 'r')
    data = f.read()
    f.close()

    raw_input = data.strip().split('\n')
    outputs = [item.split(' | ')[1] for item in raw_input]
    return outputs


# print(part_1())     # 534
