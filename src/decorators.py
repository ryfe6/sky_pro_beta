import time
from functools import wraps
from typing import Any, Callable


# def log(filename: str) -> Callable:
#     """Декоратор, принимает путь для записи данных."""
#
#     def wrapper(func: Callable) -> Callable:
#         """Декоратор, который выводит имя выполнения функции."""
#         @wraps(func)
#         def inner(a: int, b: int) -> Any:
#             """Декоратор, который выполняет функцию"""
#             try:
#                 result = func(a, b)
#             except ZeroDivisionError:
#                 result = "ZeroDivisionError"
#             now_time = time.localtime()
#             current_time = time.strftime("%Y-%m-%dT%H:%M:%S", now_time)
#
#             if filename is not None:
#                 with open(filename, "a", encoding="utf-8") as file:
#                     if result != "ZeroDivisionError":
#                         file.write(f"{current_time} my_function ok \n")
#                     else:
#                         file.write(f"{current_time} my_function error: <{result}>. Inputs: {a, b} \n")
#             else:
#                 if result != "ZeroDivisionError":
#                     print(f"{current_time} my_function ok \n")
#                 else:
#                     print(f"{current_time} my_function error: <{result}>. Inputs: {a, b} \n")
#             return result
#
#         return inner
#
#     return wrapper
#
#
# @log(filename="mylog.txt")
# def my_function(x: int, y: int) -> Any:
#     """
#     Функция принимает два числа и возвращает результат сложения двух чисел.
#     :param x: Число.
#     :param y: Число.
#     :return: Результат.
#     """
#     return x / y
#
#
# print(my_function(2, 1))

def log(filename: Any = None) -> Callable:
    """Декоратор, принимает путь для записи данных."""

    def wrapper(func: Callable) -> Callable:
        """Декоратор, который выводит имя выполнения функции."""

        @wraps(func)
        def inner(a: int, b: int) -> Any:
            """Декоратор, который выполняет функцию"""
            try:
                result = func(a, b)
            except Exception as error:
                error_try = error
                result = None
            now_time = time.localtime()
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", now_time)

            if filename is not None:
                with open(filename, "a", encoding="utf-8") as file:
                    if result is not None:
                        file.write(f"{current_time} my_function ok \n")
                    else:
                        file.write(f"{current_time} my_function error: <{error_try}>. Inputs: {a, b} \n")
            else:
                if result is not None:
                    print(f"{current_time} my_function ok \n")
                else:
                    print(f"{current_time} my_function error: <{error_try}>. Inputs: {a, b} \n")
            return result

        return inner

    return wrapper


@log()
def my_function(x: int, y: int) -> Any:
    """
    Функция принимает два числа и возвращает результат сложения двух чисел.
    :param x: Число.
    :param y: Число.
    :return: Результат.
    """
    return x / y


print(my_function(2, 0))
