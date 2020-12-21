"""Ticket module."""

import os

from itertools import chain

NEARBY_TIX = 'nearby_tickets'
NOTES_TXT = 'notes.txt'
YOUR_TICKET = 'your_ticket'


def error_rate():
    """Get the 'ticket scanning error rate'."""
    notes = _parse_notes(_load_notes())

    fields = [k for k in notes.keys() if k not in [NEARBY_TIX, YOUR_TICKET]]
    flat_tix = list(chain(*notes.get(NEARBY_TIX)))

    invalid_vals = flat_tix.copy()

    for field in fields:
        flat_field = list(chain(*notes.get(field)))
        not_in_field = [val for val in invalid_vals if val not in flat_field]
        invalid_vals = not_in_field.copy()

    return sum(invalid_vals)


def _load_notes():
    """Load notes from txt file."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), NOTES_TXT)
    f = open(filepath, 'r')
    raw_notes = f.read()
    f.close()
    notes = raw_notes.strip().split('\n\n')
    return [n.split('\n') for n in notes]


def _parse_notes(notes: list):
    """Parse notes matrix into usable dict."""
    notes_dict = dict()

    categories = [n.split(': ') for n in notes[0]]
    for cat in categories:
        key = cat[0]
        ranges_str = [nums.split('-') for nums in cat[1].split(' or ')]
        ranges = list()

        for r in ranges_str:
            start = int(r[0])
            end = int(r[1]) + 1
            ranges.append(list(range(start, end)))

        notes_dict.update({key: ranges})

    ticket = [int(num) for num in notes[1][1].split(',')]
    notes_dict.update({YOUR_TICKET: ticket})

    nearby_tix_str = [n.split(', ') for n in notes[2][1:]]
    nearby_tix = list()
    for num_list in nearby_tix_str:
        tix = [int(num) for num in num_list[0].split(',')]
        nearby_tix.append(tix)

    notes_dict.update({NEARBY_TIX: nearby_tix})
    return notes_dict


# SOLUTION 1 | 20091
# print(error_rate())
