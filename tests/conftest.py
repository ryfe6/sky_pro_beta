import pytest


@pytest.fixture
def test_data_widget():
    return [
        "Maestro 1596837868705199",
        "Счет 64686473678894779589",
        "Счет 3538303347444789556",
        "чет 73654108430135874305",
    ]


@pytest.fixture
def test_data_processing():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}]
