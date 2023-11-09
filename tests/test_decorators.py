import datetime

import pytest

from src.decorators import log


@pytest.mark.parametrize(
    "a, b, expected_result",
    [(1, 0, " my_function error: <division by zero>. Inputs: (1, 0)"), (2, 1, " my_function ok")],
)
def test_log_to_file(a, b, expected_result):
    """Тест логирования в файл."""
    filename = "mylog.txt"

    @log(filename=filename)
    def my_function(x, y):
        return x / y

    my_function(a, b)  # вызвали декорированную функцию

    with open(filename, "r") as file:  # открыли файл и прочитали что в него записалось
        for line in file:
            pass
        log_info = line.strip()

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    expected_log_info = f"{now}{expected_result}"
    assert log_info == expected_log_info  # сверили результат с ожидаемым


@pytest.mark.parametrize("a, b, expected_result", [(2, "1", None), (2, 2, 1.0)])
def test_log_to_file_2(a, b, expected_result):
    """Тест логирования в файл."""

    @log()
    def my_function(x, y):
        return x / y

    log_info = my_function(a, b)  # вызвали декорированную функцию

    expected_log_info = expected_result
    assert log_info == expected_log_info  # сверили результат с ожидаемым
