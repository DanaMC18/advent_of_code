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

    for id, card in data.items():
        # copies = card_counts.get(id, 1)
        numbers, winners = card
        count = 0
        for num in numbers:
            if num in winners:
                count += 1

        if count > 0:
            card_counts[id] = card_counts.get(id, 0) + 1

        while count > 0:
            card_id = id + count
            current_count = card_counts.get(card_id, 0)
            card_counts[card_id] = current_count + 1
            count -= 1

    return card_counts


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
print(part_two())
