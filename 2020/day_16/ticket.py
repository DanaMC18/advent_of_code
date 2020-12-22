"""Ticket module."""

import os

from functools import reduce
from itertools import chain


DEPARTURE = 'departure'
NEARBY_TIX = 'nearby_tickets'
NOTES_TXT = 'notes.txt'
YOUR_TICKET = 'your_ticket'


def departure_prod(field_map: dict, ticket: list):
    """Apply field map to "your_ticket" and multiply departure values."""
    indicies = [v for k, v in field_map.items() if DEPARTURE in k]
    departures = [ticket[i] for i in indicies]
    return reduce((lambda x, y: x * y), departures)


def error_rate():
    """Get the 'ticket scanning error rate'."""
    notes = _parse_notes(_load_notes())

    fields = [k for k in notes.keys() if k not in [NEARBY_TIX, YOUR_TICKET]]
    flat_tix = list(chain(*notes.get(NEARBY_TIX)))

    invalid_vals = flat_tix.copy()

    for field in fields:
        flat_field = list(chain(*notes.get(field)))
        vals_not_in_field = [val for val in invalid_vals if val not in flat_field]
        invalid_vals = vals_not_in_field.copy()

    return sum(invalid_vals)


def identify_fields():
    """Identify which fields are which based on the valid tickets."""
    notes = _parse_notes(_load_notes())
    fields = [k for k in notes.keys() if k not in [NEARBY_TIX, YOUR_TICKET]]

    valid_tix = [t for t in notes.get(NEARBY_TIX) if _is_ticket_valid(fields, notes, t)]

    index = 0
    field_indicies = {field: [] for field in fields}

    while index < len(fields):
        vals = [num_list[index] for num_list in valid_tix]

        for field in fields:
            flat_field = list(chain(*notes.get(field)))

            if all(val in flat_field for val in vals):
                field_indicies[field].append(index)

        index += 1

    field_index = dict()
    length = 1

    while length <= len(fields):
        for field in fields:
            indicies = field_indicies.get(field)
            filtered = [idx for idx in indicies if idx not in field_index.values()]

            if len(filtered) == 1:
                field_index.update({field: filtered[0]})

        length += 1

    return field_index, notes


def _is_ticket_valid(fields: list, notes: dict, ticket: list):
    """Determine if given ticket is valid."""

    valid_map = {num: False for num in ticket}

    for field in fields:
        flat_field = list(chain(*notes.get(field)))
        valid_vals = [num for num in ticket if num in flat_field]
        for val in valid_vals:
            valid_map[val] = True

    return all(val for val in valid_map.values())


def _load_notes():
    """Load raw notes from txt file."""
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

# SOLUTION 2 | 2325343130651
# field_map, notes = identify_fields()
# prod = departure_prod(field_map, notes.get(YOUR_TICKET))
# print(prod)
