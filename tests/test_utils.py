import pytest

from src.utils import generator_data_operations, get_load_json_file, get_operations_sum_in_rub


def test_get_load_json_file():
    assert len(get_load_json_file("tests/operations.json")) > 0
    assert len(get_load_json_file(None)) == 0


def test_generator_data_operations():
    gen = generator_data_operations(get_load_json_file("tests/operations.json"))
    assert_first = next(gen)
    assert assert_first == {"amount": "31957.58", "currency": {"code": "RUB", "name": "руб."}}


def test_get_operation_sum_in_rub():
    gen = generator_data_operations(get_load_json_file("tests/operations.json"))
    assert_first = next(gen)
    assert_second = next(gen)
    assert get_operations_sum_in_rub(assert_first) == 31957.58
    with pytest.raises(ValueError):
        get_operations_sum_in_rub(assert_second)
