from typing import Iterable, List

from src.entities import Entry, Entries
from src.settings import settings


def chunked_entries_generator(filepath: str, chunk_size: int) -> Iterable[Entries]:
    """Generator that yields serialized Entries objects with size of chunks.

    :param filepath: full path to csv file to read
    :param chunk_size: size of chunks to read per iteration
    :return: iterable with <Entries> objects
    """

    with open(filepath) as content:
        rows = content.readlines(chunk_size)
        while rows:
            entries = _parse_entries(rows)
            yield Entries(data=entries)
            rows = content.readlines(chunk_size)


def _parse_entries(lines: List) -> Entries:
    """Parses each line as <Entry> objects.

    :param lines: list of strings from csv file
    :return: <Entries> object
    """
    if settings.csv_header_part in lines[0]: # skipping header
        lines = lines[1:]

    return [
        _parse_entry(line) for line in lines
    ]


def _parse_entry(line: str) -> Entry:
    """Parses single line as <Entry> object.

    :param line: single line string from csv file
    :return: <Entry> object
    """
    row = line[:-1].split(settings.csv_delimiter)
    return Entry(
        city=row[0],
        date=row[1],
        sales=row[2],
    )
