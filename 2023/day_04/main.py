"""Main solution file: day 04."""

import os
from typing import List

INPUT_FILE = 'input.txt'


def part_one() -> int:
    """Return the total points from all winning scratchcards."""
    data = _format_data()
    card_points = []

    for card in data.values():
        numbers, winners = card
        count = 0
        for num in numbers:
            if num in winners:
                count += 1

        if count > 0:
            exp = count - 1
            card_points.append(2**exp)

    return sum(card_points)


def part_two() -> int:
    """Return the total number of scratchcards."""
    data = _format_data()
    card_counts = {}

    for id in data.keys():
        card_counts[id] = 1

    for id, card in data.items():
        copies = card_counts[id]
        numbers, winners = card
        count = 0
        for num in numbers:
            if num in winners:
                count += 1

        while count > 0:
            card_id = id + count
            current_count = card_counts[card_id]
            card_counts[card_id] = current_count + copies
            count -= 1

    return sum(card_counts.values())


# # # # # # # #
# LOAD INPUT  #
# # # # # # # #

def _format_data() -> dict:
    """Format data into a dict of lists."""
    raw_data = _load_data()
    cards = {}

    for line in raw_data:
        card, raw_winners = line.split('|')
        card_id = card.split(':')[0].replace('Card ', '')
        numbers = card.split(':')[1].strip().split(' ')
        winners = raw_winners.strip().split(' ')

        clean_numbers = [int(num) for num in numbers if num.isnumeric()]
        clean_winners = [int(num) for num in winners if num.isnumeric()]
        cards[int(card_id)] = [clean_numbers, clean_winners]

    return cards


def _load_data() -> List[str]:
    """Load data from text file. Returns a list strings."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), INPUT_FILE)
    f = open(filepath, 'r')
    data = f.read()
    f.close()

    return data.strip().split('\n')


# print(part_one())   # 28750
# print(part_two())   # 10212704
