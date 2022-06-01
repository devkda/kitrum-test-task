"""
This module contains the api to perform calculations on csv files with sales data.
"""

import csv
from pathlib import Path

from .settings import settings
from .domain import SalesMap
from .loaders import chunked_entries_generator


def calculate_total_sales(filepath: Path) -> SalesMap:
    """Counts total sales.

    :param filepath: full path to csv file with sale entries
    :return: <SalesMap> mapping with total sales per each department
    """
    entry_chunks = chunked_entries_generator(filepath, settings.chunk_size)
    total_sales = SalesMap()

    for entries in entry_chunks:
        total_sales.add_entries(entries)

    return total_sales


def save_sales_to_csv(salesmap: SalesMap, dest: Path):
    """Saves salesmap data as csv to file.

    :param salesmap: <SalesMap> object with data
    :param dest: destination path to save
    :return:
    """
    with open(dest, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(salesmap.field_names)
        writer.writerows(salesmap.values_as_list())
