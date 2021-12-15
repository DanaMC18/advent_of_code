"""Main solution file: day 14."""

from collections import Counter
import os
from typing import Dict, Tuple

INPUT_FILE = 'input.txt'


def main(step_count: int) -> int:
    """Return diff of most and least common polymer after N steps."""
    template, rules = _load_input()
    pair_counts = Counter()

    for start in range(len(template)):
        end = start + 2
        key = template[start:end]
        if len(key) == 2:
            pair_counts[key] += 1

    new_pair_counts = _execute_steps(
        pair_counts,
        rules,
        step_count,
        1
    )

    char_counts = Counter(template[0])

    for pair, count in new_pair_counts.items():
        char = pair[1]
        char_counts[char] += count

    return max(char_counts.values()) - min(char_counts.values())


def _execute_steps(
    pair_counts: Dict[str, int],
    rules: Dict[str, str],
    step_count: int,
    step: int
):
    """Recursively count pair of chars after N steps of polymer insertion.

    Args:
        pair_counts (dict): map of pair counts (ex: {'AX': 10})
        rules (dict): insertion rules (ex: {'AB': 'X'})
        step_count (int): number of steps to execute
        step (int): number of current step

    Returns:
        pair_counts (dict): updated map of pair counts
    """
    if step > step_count:
        return pair_counts

    pair_counts_copy = pair_counts.copy()
    new_pair_counts = Counter()

    for k in pair_counts_copy.keys():
        ax = k[0] + rules[k]
        xb = rules[k] + k[1]
        new_pair_counts[ax] += pair_counts_copy[k]
        new_pair_counts[xb] += pair_counts_copy[k]

    return _execute_steps(new_pair_counts, rules, step_count, step + 1)


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


# print(main(10))   # 2170
# print(main(40))   # 2422444761283
