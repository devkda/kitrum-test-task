from src.settings import settings
from src.domain import SalesMap
from src.loaders import chunked_entries_generator


def calculate_total_sales(filepath: str) -> SalesMap:
    """Counts total sales.

    :param filepath: full path to csv file with sale entries
    :return: <SalesMap> mapping with total sales per each city
    """
    total_sales = SalesMap()
    entry_chunks = chunked_entries_generator(filepath, settings.chunk_size)
    
    for entries in entry_chunks:
        total_sales += SalesMap(entries)

    return total_sales
