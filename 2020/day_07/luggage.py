"""Luggage module."""

import os


CONTAIN = ' contain'
RULES_TXT = 'rules.txt'
SHINY_GOLD = 'shiny gold bag'


def get_bag_colors():
    """Get all bag colors that can eventually contain a shiny gold bag."""
    all_bag_rules = _load_rules()
    gold_containers = _filter_rules_by_color(all_bag_rules, SHINY_GOLD)

    outer_bag_colors = gold_containers.copy()

    for color in gold_containers:
        color_rules = _filter_rules_by_color(all_bag_rules, color)
        outer_bag_colors += color_rules

    return set(outer_bag_colors)


def _filter_rules_by_color(all_rules: list, color: str):
    """Get all bags that can directly contain a specified color bag."""
    gold_rules = [rule for rule in all_rules if color in rule]
    outer_bag_rules = [rule.split(CONTAIN)[0] for rule in gold_rules]
    return [rule for rule in outer_bag_rules if color not in rule]


def _load_rules():
    """Load bag rules from txt file."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), RULES_TXT)
    f = open(filepath, 'r')
    rules = f.read()
    f.close()
    return rules.strip().split('\n')


# SOLUTION 1
# print(get_bag_colors())
# print(len(get_bag_colors()))
# 29

# MIGHT HAVE TO DO THIS RECURSIVELY TO GET DEEPLY NESTED BAGS?
# put lines 18 - 22 in it's own recursive method? break point = count stays the same?
