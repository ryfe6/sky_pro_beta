from src import decorators
import pytest


@pytest.mark.parametrize("x, y, expected_result", [(1, 0, "ZeroDivisionError"),
                                                   (2, 1, 2.0)])
def test_my_function(x, y, expected_result):
    assert decorators.my_function(x, y) == expected_result



