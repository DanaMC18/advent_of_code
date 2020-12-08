"""Luggage module."""

import os

CONTAIN = ' contain '
NO_OTHER_BAGS = 'no other'
RULES_TXT = 'rules.txt'
SHINY_GOLD = 'shiny gold'


def get_bag_colors():
    """Get all bag colors that can eventually contain a shiny gold bag."""
    all_bag_rules = _load_rules()
    color_bag_map = _color_bag_map(all_bag_rules)

    result_bags = []
    for bag in color_bag_map.keys():
        bags = _outer_bags(color_bag_map, bag.strip())
        result_bags = result_bags + bags

    return set(result_bags)


def _color_bag_map(all_rules: list):
    """Create map of bags."""
    bags = {}
    for rule in all_rules:
        clean_rule = _clean_rule_text(rule)
        key, values = [color.strip() for color in clean_rule.split(CONTAIN)]

        if NO_OTHER_BAGS in values:
            bags[key] = {}
            continue

        split_vals = [val.strip() for val in values.split(', ')]
        val_matrix = [val.split(' ', 1) for val in split_vals]
        bags[key] = {color_num[1]: int(color_num[0]) for color_num in val_matrix}

    return bags


def _clean_rule_text(rule: str):
    """Remove "bag", "bags", and "." from rule string."""
    return rule.replace('bags', '').replace('bag', '').replace('.', '')


def _load_rules():
    """Load bag rules from txt file."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), RULES_TXT)
    f = open(filepath, 'r')
    rules = f.read()
    f.close()
    return rules.strip().split('\n')


def _outer_bags(color_bag_map: dict, color: str):
    """Get all bags that can contain the specified color."""
    outer_bags = list()
    for key in color_bag_map[color].keys():
        if key.strip() == SHINY_GOLD:
            outer_bags.append(color)
        _outer_bags(color_bag_map, key.strip())

    return outer_bags


# SOLUTION 1
# print(get_bag_colors())
# print(len(get_bag_colors()))
# 29
