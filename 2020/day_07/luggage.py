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


# SOLUTION 01 | 177
def _bag_ception(color_map_key, bag=None):
    """Bags in bags in bags."""
    for k in color_map[color_map_key].keys():
        if k == SHINY_GOLD:
            result.add(bag)
            break
        _bag_ception(k, bag)


def get_outer_bags():
    for bag in color_map.keys():
        _bag_ception(bag, bag)
    return result

# print(len(get_outer_bags()))


# SOLUTION 02 | 34988
bag_sums = list()


def get_bag_count(color_map_key=SHINY_GOLD):
    """Get number of bags inside a shiny gold bag."""
    children = color_map[color_map_key]
    bag_sums.append(sum(children.values()))

    for child in children.keys():
        for i in range(children[child]):
            get_bag_count(child)

    return sum(bag_sums)


# print(get_bag_count(SHINY_GOLD))
