"""Customs module."""

import os
from functools import reduce


YES_TXT = 'answers.txt'


def yes_count():
    """Get number of unique questions that have been answered "yes"."""
    answer_list = _load_answers()
    group_answers = [answer.replace('\n', '') for answer in answer_list]
    yes_counts = [len(set(group)) for group in group_answers]
    return reduce((lambda x, y: x + y), yes_counts)


def _load_answers():
    """Load each group's yes answers from txt file."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), YES_TXT)
    f = open(filepath, 'r')
    answers = f.read()
    f.close()
    return answers.strip().split('\n\n')


# SOLUTION 1
# print(yes_count())
