"""Customs module."""

import os
from functools import reduce


YES_TXT = 'answers.txt'


def all_yes_count():
    """Get number of questions to which everyone in a group answered yes."""
    answer_list = _load_answers()
    group_answers = [answer.split('\n') for answer in answer_list]
    yes_counts = []

    for group in group_answers:
        if len(group) == 1:
            yes_counts.append(len(set(group[0])))
            continue
        yes_map = _group_yes_map(group)
        common_answers = [ans for ans in yes_map if yes_map[ans] == len(group)]
        yes_counts.append(len(common_answers))

    return reduce((lambda x, y: x + y), yes_counts)


def unique_yes_count():
    """Get number of unique questions that have been answered "yes"."""
    answer_list = _load_answers()
    group_answers = [answer.replace('\n', '') for answer in answer_list]
    yes_counts = [len(set(group)) for group in group_answers]
    return reduce((lambda x, y: x + y), yes_counts)


def _group_yes_map(group: list):
    """Create dict where key is a question and value is the number of "yes" answers."""
    yes_map = {}
    for indiv in group:
        for char in indiv:
            if not yes_map.get(char):
                yes_map[char] = 0
            yes_map[char] += 1
    return yes_map


def _load_answers():
    """Load each group's yes answers from txt file."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), YES_TXT)
    f = open(filepath, 'r')
    answers = f.read()
    f.close()
    return answers.strip().split('\n\n')


# SOLUTION 1
# print(unique_yes_count())

# SOLUTION 2
# print(all_yes_count())
