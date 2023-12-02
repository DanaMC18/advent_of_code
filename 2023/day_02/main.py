"""Main solution file: day 02."""

import os
from functools import reduce
from typing import List

INPUT_FILE = 'input.txt'
COLOR_CONFIG = {'red': 12, 'green': 13, 'blue': 14}


def part_one() -> int:
    """Return the sum of the valid game IDs."""
    games = _format_games()
    valid_game_ids = []

    for id, pulls in games.items():
        is_valid = True
        for pull in pulls:
            for color in pull.keys():
                if pull[color] > COLOR_CONFIG[color]:
                    is_valid = False
        if is_valid:
            valid_game_ids.append(int(id))

    return sum(valid_game_ids)


def part_two() -> int:
    """Return the sum of the power of each set."""
    games = _format_games()
    power_of_sets = []

    for pulls in games.values():
        max_color_count = {'red': 1, 'green': 1, 'blue': 1}
        for pull in pulls:
            for color in pull.keys():
                if pull[color] > max_color_count[color]:
                    max_color_count[color] = pull[color]

        product = reduce((lambda x, y: x * y), max_color_count.values())
        power_of_sets.append(product)

    return sum(power_of_sets)


# # # # # # #
#  HELPERS  #
# # # # # # #

def _format_games() -> dict:
    """Return a formatted dict of games."""
    data = _load_data()
    games = {}

    for raw_game in data:
        i = raw_game.index(':')
        game_id = raw_game[:i].replace('Game', '').strip()
        sets = raw_game[i + 2:].split('; ')

        game = []

        for s in sets:
            color_dict = {}

            for pull in s.split(', '):
                for color in COLOR_CONFIG.keys():
                    if color in pull:
                        color_num = pull.replace(color, '').strip()
                        color_dict[color] = int(color_num)

            game.append(color_dict)

        games[game_id] = game

    return games


def _load_data() -> List[str]:
    """Load data from text file. Returns a list strings."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), INPUT_FILE)
    f = open(filepath, 'r')
    data = f.read()
    f.close()

    return data.strip().split('\n')


# print(part_one())   # 2285
# print(part_two())   # 77021
