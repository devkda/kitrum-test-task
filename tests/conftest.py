import pytest

from salescalc.domain import SalesMap


@pytest.fixture
def tmp_salesmap():
    data = {
        'New-York': 123,
        'Boston': 456,
    }
    salesmap = SalesMap()
    salesmap.sales = data
    return salesmap


@pytest.fixture
def tmp_csv(tmp_path):
    CONTENT = (
        "Department Name,Date,Number of sales\n"
        "New-York,2020-01-01,10\n"
        "New-York,2020-01-01,10\n"
        "Boston,2020-01-01,10\n"
    )

    filedir = tmp_path / __name__
    filedir.mkdir()
    path = filedir / "test.csv"
    path.write_text(CONTENT)
    return path
