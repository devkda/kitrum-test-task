"""
This module contains the functions that loads objects as domain objects
from input files.

Supported formats:
    - csv
"""

from pathlib import Path
from typing import Iterable, List

from .structures import Entry, Entries
from .settings import settings


def chunked_entries_generator(filepath: Path, chunk_size: int) -> Iterable[Entries]:
    """Generator that yields serialized <Entries> objects with size of chunks.

    :param filepath: full path to csv file to read
    :param chunk_size: size of chunks to read per generation
    :return: iterable of <Entries> objects
    """
    with open(filepath) as content:
        next(content)  # skipping header line
        rows = content.readlines(chunk_size)
        while rows:
            entries = _parse_entries(rows)
            yield Entries(data=entries)
            rows = content.readlines(chunk_size)


def _parse_entries(lines: List[str]) -> List[Entry]:
    """Parses csv lines as <Entries> objects.

    :param lines: list of strings from csv file
    :return: <Entries> object
    """

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
        department=row[0],
        date=row[1],
        sales=row[2],
    )
