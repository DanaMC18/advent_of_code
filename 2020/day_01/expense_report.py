"""Expense Report class."""

import itertools
import json
import os

from functools import reduce


EXPENSE_JSON = 'expense_report.json'


class ExpenseReport:
    """Expense Report class."""

    def __init__(self, n: int):
        """Init expense report."""
        self._set_expenses()
        self.n = n

    def find_2020(self):
        """Find n number of expenses that equal 2020 when added together."""
        for combo in self._combos():
            if reduce((lambda x, y: x + y), combo) == 2020:
                return combo

    def product(self, expenses: list):
        """Multiply together all expenses in given list."""
        return reduce((lambda x, y: x * y), expenses)

    def _combos(self):
        """Get every combo of items in list."""
        combinations = itertools.combinations(self.expenses, self.n)
        return list(combinations)

    def _set_expenses(self):
        """Read expense_report json and set expenses."""
        filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), EXPENSE_JSON)
        with open(filepath) as f:
            self.expenses = json.load(f)
