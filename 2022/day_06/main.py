"""Main solution file: day 06."""

from input import INPUT


def main(packet_size: int) -> int:
    """Return position of start-of-packet marker.

    Args:
        packet_size (int): size of the packet to look for
    """
    marker = ''

    for i in range(len(INPUT)):
        marker = marker + INPUT[i]

        if len(marker) < packet_size:
            continue

        if len(set(marker)) == packet_size:
            return i + 1

        marker = marker[1:]


# print(main(4))  # 1080
# print(main(14))  # 3645
