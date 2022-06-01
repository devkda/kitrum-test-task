"""
This module contains the domain logic.
"""

from __future__ import annotations
from collections import defaultdict

from prettytable import PrettyTable

from .structures import Entries, Entry


class SalesMap:
    """Representation of total sales data of all the departments.

    Sales data is stored in dictionary, where the keys are department names and
    values are total salaes of dept.

    Example::
        {
            'New-York': 123,
            'Boston': 456,
        }

    Supports addition between instances with arithmetic operator.

    Example::
      >>> SalesMap() + SalesMap()
    """

    __slots__ = ['sales']
    field_names = ['Department Name', 'Sales']  # key, value labels

    def __init__(self, entries: Entries | None = None):
        """
        :param entries: list of <Entries> to evaluate and store in current instance.
        """
        self.sales = defaultdict(int)

        if entries is not None:
            for entry in entries.data:
                self.add_entry(entry)

    def add_entry(self, entry: Entry):
        """Adds single sales entry to current instance.
        :param entry: single sales <Entry> to add for corresponding department.
        """
        self.sales[entry.department] += entry.sales

    def add_entries(self, entries: Entries):
        """Adds all the sales entries to current instance.
        :param entries: sales <Entries> to add for corresponding department.
        """
        for entry in entries.data:
            self.add_entry(entry)

    def __add__(self, other: SalesMap) -> SalesMap:
        """Dunder method to add SalesMap objects.
        Makes the union of keys from both SalesMap objects and
        stores sum of sales count from both objects.

        :param other: SalesMap object to add
        """
        new_map = SalesMap()
        cities = set(self.sales.keys()).union(other.sales.keys())

        for department in cities:
            new_map.sales[department] += self.sales[department] + other.sales[department]

        return new_map

    def values_as_list(self):
        """Returns the sales data as a list, consisting of pairs (department, sales_count).

        Example::
            [
                ('New-York', 123),
                ('Boston', 456),
            ]
        """
        return [(department, sales) for department, sales in self.sales.items()]

    def __str__(self):
        """Returns the string representation of sales data as a
        table with pretty layout.

        Example::
            +-----------------+-------+
            | Department Name | Sales |
            +-----------------+-------+
            |     New-York    |  123  |
            |      Boston     |  456  |
            +-----------------+-------+
        """
        table = PrettyTable()
        table.field_names = self.field_names

        for department, sales in self.sales.items():
            table.add_row([department, sales])

        return str(table)
