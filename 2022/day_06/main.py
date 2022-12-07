"""Main solution file: day 06."""

from input import INPUT


def part_1() -> int:
    """Return position of start-of-packet marker."""
    marker = ''

    for i in range(len(INPUT)):
        marker = marker + INPUT[i]

        if len(marker) < 4:
            continue

        if len(set(marker)) == 4:
            return i + 1

        marker = marker[1:]


# print(part_1())  # 1080
