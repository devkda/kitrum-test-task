from salescalc.usecases import (
    calculate_total_sales,
    save_sales_to_csv,
)


def test_calculate_total_sales(tmp_csv):
    result = calculate_total_sales(tmp_csv)
    assert result.sales['Boston'] == 12
    assert result.sales['New-York'] == 6


def test_save_sales_to_csv(tmp_salesmap, tmp_path):
    CONTENT = (
        "Department Name,Sales\n"
        "New-York,123\n"
        "Boston,456\n"
    )
    filedir = tmp_path / __name__
    filedir.mkdir()
    path = filedir / "test.csv"

    save_sales_to_csv(tmp_salesmap, path)

    assert path.read_text() == CONTENT
