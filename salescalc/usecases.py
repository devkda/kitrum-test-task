import csv
from pathlib import Path

from concurrent.futures import ProcessPoolExecutor as Pool

from salescalc.settings import settings
from salescalc.domain import SalesMap
from salescalc.loaders import chunked_entries_generator


def calculate_total_sales(filepath: Path, workers: int=settings.workers) -> SalesMap:
    """Counts total sales.

    :param filepath: full path to csv file with sale entries
    :param workers: workers count to run in parallel
    :return: <SalesMap> mapping with total sales per each city
    """
    entry_chunks = chunked_entries_generator(filepath, settings.chunk_size)
    total_sales = SalesMap()

    with Pool(max_workers=workers) as pool:
        results = pool.map(SalesMap, entry_chunks)
    
    for salesmap in results:
        total_sales += salesmap

    return total_sales


def save_sales_to_csv(salesmap: SalesMap, dest: Path):
    """Saves salesmap data as csv to file.

    :param salesmap: SalesMap object with data
    :param dest: destination path to save
    :return:
    """
    with open(dest, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(salesmap.field_names)
        writer.writerows(salesmap.values_as_list())
