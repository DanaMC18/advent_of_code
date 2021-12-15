"""Main solution file: day 14."""

from collections import Counter
import os
from typing import Dict, Tuple

INPUT_FILE = 'input.txt'


def part_1() -> int:
    """Return diff of most and least common polymer after 10 steps."""
    initial_template, rules = _load_input()
    template = _execute_steps(rules, 10, 1, initial_template)

    char_counts = Counter(template).most_common()
    max_qty = char_counts[0][1]
    min_qty = char_counts[-1][1]

    return max_qty - min_qty


def _execute_steps(
    rules: dict,
    step_count: int,
    step: int,
    template: str
) -> str:
    """Recursively execute N steps of polymer insertion. Return new template.

    Args:
        rules (dict): insertion rules (ex: {'AB' -> 'C'})
        step_count (int): number of steps to execute
        step (int): number of current step
        template (str): string on which to execute step
    """
    if step > step_count:
        return template

    new_template = ''
    for start in range(len(template)):
        end = start + 2
        section = template[start:end]
        mid = rules.get(section)

        if start == 0:
            new_template += template[start]

        if mid:
            new_section = f'{mid}{template[start + 1]}'
            new_template += new_section

    return _execute_steps(rules, step_count, step + 1, new_template)


def _load_input() -> Tuple[str, Dict[str, str]]:
    """Load input data from text file."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), INPUT_FILE)
    f = open(filepath, 'r')
    data = f.read()
    f.close()

    template, raw_rules = data.strip().split('\n\n')
    rules = raw_rules.split('\n')
    rule_dict = {}

    for rule in rules:
        key, value = rule.split(' -> ')
        rule_dict[key] = value

    return template, rule_dict


print(part_1())   # 2170
