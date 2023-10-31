from src import masks
import pytest


@pytest.mark.parametrize(
    "num_card, expected_result",
    [("7000792289606361", "7000 79** **** 6361"), ("73654108430135874305", "Неправильный номер карты")],
)
def test_mask_card(num_card, expected_result):
    assert masks.mask_card(num_card) == expected_result


@pytest.mark.parametrize(
    "num_score, expected_results",
    [("73654108430135874305", "**4305"), ("7000792289606361", "Неправильный номер счета")],
)
def test_mask_score(num_score, expected_results):
    assert masks.score_mask(num_score) == expected_results
