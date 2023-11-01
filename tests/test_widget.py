import pytest
from src import widget


def test_mask_card_and_score(test_data_widget):
    assert widget.mask_card_and_score(test_data_widget[0]) == "Maestro  1596 83** **** 5199"
    assert widget.mask_card_and_score(test_data_widget[1]) == "Счет **9589"
    assert widget.mask_card_and_score(test_data_widget[-1]) == "Введен некорректный номер карты"
    assert widget.mask_card_and_score(test_data_widget[-2]) == "Введен некорректный номер счета"


def test_filter_date():
    assert widget.filter_date("2018-07-11T02:26:18.671407") == "11.07.2018"


@pytest.mark.parametrize(
    "list_word, filter_result",
    [
        (["hello", "world", "apple", "pear", "banana", "pop"], ["pop"]),
        (["", "madam", "racecar", "noon", "level", ""], ["", "madam", "racecar", "noon", "level", ""]),
        ([], []),
    ],
)
def test_dlc_task_1(list_word, filter_result):
    assert widget.dlc_task_1(list_word) == filter_result


@pytest.mark.parametrize(
    "list_num, expected_result", [([2, 3, 5, 7, 11], 77), ([-5, -7, -9, -13], 117), ([1, 2], 2), ([4], 0)]
)
def test_dlc_task_2(list_num, expected_result):
    assert widget.dlc_task_2(list_num) == expected_result
