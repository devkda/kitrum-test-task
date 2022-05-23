from __future__ import annotations
from collections import defaultdict
from pprint import pformat

from src.entities import Entries, Entry


class SalesMap:
    """Representation of total sales table for each city.
    Supports addition between instances with arithmetic operator.
    Ex: SalesMap() + SalesMap()
    """

    __slots__ = ['_dict']

    def __init__(self, entries: Entries = None):
        """
        """
        self._dict = defaultdict(int)

        if entries is not None:
            for entry in entries.data:
                self.add_entry(entry)

    def add_entry(self, entry: Entry):
        """
        """
        self._dict[entry.city] += entry.sales

    def __add__(self, other: SalesMap):
        """
        """
        new_map = SalesMap()
        cities = set(self._dict.keys()).union(other._dict.keys())
        for city in cities:
            new_map._dict[city] += self._dict[city] + other._dict[city]
        return new_map

    def __repr__(self):
        return '<SalesMap>: ' + pformat(self._dict)
