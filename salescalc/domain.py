from __future__ import annotations
from collections import defaultdict

from prettytable import PrettyTable

from salescalc.entities import Entries, Entry


class SalesMap:
    """Representation of total sales table for each city.
    Supports addition between instances with arithmetic operator.
    Ex: 
        SalesMap() + SalesMap()
    """

    __slots__ = ['sales']
    field_names = ['Department Name', 'Sales']  # key, value labels

    def __init__(self, entries: Entries = None):
        """
        """
        self.sales = defaultdict(int)

        if entries is not None:
            for entry in entries.data:
                self.add_entry(entry)

    def add_entry(self, entry: Entry):
        """
        """
        self.sales[entry.city] += entry.sales

    def __add__(self, other: SalesMap):
        """
        """
        new_map = SalesMap()
        cities = set(self.sales.keys()).union(other.sales.keys())
        for city in cities:
            new_map.sales[city] += self.sales[city] + other.sales[city]
        return new_map

    def values_as_list(self):
        return [(city, sales) for city, sales in self.sales.items()]

    def __str__(self):
        table = PrettyTable()
        table.field_names = self.field_names

        for city, sales in self.sales.items():
            table.add_row([city, sales])

        return str(table)
