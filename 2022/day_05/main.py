"""Solution file day 05."""

from copy import deepcopy
from input import PROCEDURE, STACKS


def part_1() -> str:
    """Get crates on top of each stack after rearranging."""
    new_stacks = deepcopy(STACKS)

    for proc in PROCEDURE:
        crate_num = proc['move']
        source = proc['from'] - 1
        dest = proc['to'] - 1

        source_stack = new_stacks[source]
        dest_stack = new_stacks[dest]

        for _ in range(crate_num):
            crate = source_stack.pop()
            dest_stack.append(crate)

    top_crates = [s[-1] for s in new_stacks if s]
    return ''.join(top_crates)


def part_2() -> str:
    """Get crates on top of each stack after rearranging, but different."""
    new_stacks = deepcopy(STACKS)

    for proc in PROCEDURE:
        crate_num = proc['move']
        source = proc['from'] - 1
        dest = proc['to'] - 1

        source_stack = new_stacks[source]
        dest_stack = new_stacks[dest]
        crates = []

        for _ in range(crate_num):
            crate = source_stack.pop()
            crates.append(crate)

        crates.reverse()
        dest_stack.extend(crates)

    top_crates = [s[-1] for s in new_stacks if s]
    return ''.join(top_crates)


# print(part_1())  # HNSNMTLHQ
# print(part_2())  # RNLFDJMCT
