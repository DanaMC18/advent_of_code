"""Luggage module."""

import os

CONTAIN = ' contain '
NO_OTHER_BAGS = 'no other'
RULES_TXT = 'rules.txt'
SHINY_GOLD = 'shiny gold'


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


all_rules = _load_rules()
bag = None
color_map = _color_bag_map(all_rules)
result = set()


# SOLUTION 1
def _gather_bags(color_map_key, bag=None):
    """Bags in bags in bags."""
    for k in color_map[color_map_key].keys():
        if k == SHINY_GOLD:
            result.add(bag)
            break
        _gather_bags(k, bag)


def get_outer_bags():
    for bag in color_map.keys():
        _gather_bags(bag, bag)
    return result
