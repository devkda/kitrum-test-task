from salescalc.loaders import chunked_entries_generator
from salescalc.structures import Entries, Entry


def test_chunked_entries_generator(tmp_csv):
    chunks = chunked_entries_generator(tmp_csv, 1000)
    entries = next(chunks)
    assert len(entries.data) == 3


def test_chunked_entries_generator_return_type(tmp_csv):
    chunks = chunked_entries_generator(tmp_csv, 1000)
    entries = next(chunks)
    assert isinstance(entries, Entries)


def test_chunked_entries_generator_entry_type(tmp_csv):
    chunks = chunked_entries_generator(tmp_csv, 1000)
    entries = next(chunks)
    assert isinstance(entries.data[0], Entry)


def test_chunked_entries_generator_entry_content(tmp_csv):
    chunks = chunked_entries_generator(tmp_csv, 1000)
    entries = next(chunks)
    assert entries.data[0].department == 'New-York'
    assert entries.data[0].sales == 10
