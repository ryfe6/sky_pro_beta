import pytest

from src.utils import generator_data_operations, get_load_json_file, get_operations_sum_in_rub


def test_get_load_json_file(data="operations.json"):
    assert len(get_load_json_file(data)) > 0
    assert len(get_load_json_file(None)) == 0


def test_generator_data_operations():
    gen = generator_data_operations(get_load_json_file("tests/operations.json"))
    assert_first = next(gen)
    assert assert_first == [
        {
            "date": "2019-08-26T10:50:58.294041",
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "id": 441945886,
            "operationAmount": {"amount": "31957.58", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 64686473678894779589",
        }
    ]


def test_get_operation_sum_in_rub():
    gen = generator_data_operations(get_load_json_file("operations.json"))
    assert_first = next(gen)
    assert_second = next(gen)
    assert get_operations_sum_in_rub(assert_first) == 31957.58
    with pytest.raises(ValueError):
        get_operations_sum_in_rub(assert_second)
