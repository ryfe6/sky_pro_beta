import os

import pytest

from src.data_read import get_read_file_csv_or_xlsx


@pytest.mark.parametrize(
    "filename, expected_result", [("transactions.csv", (1000, 1)), ("transactions_excel.xlsx", (1000, 9))]
)
def test_get_read_file_csv_or_xlsx(filename, expected_result):
    file = os.path.join(f"../data/{filename}")
    assert_func = get_read_file_csv_or_xlsx(file)
    assert assert_func.shape == expected_result

