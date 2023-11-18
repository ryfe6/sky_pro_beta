import json
from typing import Generator


def get_load_json_file(filename: str) -> list:
    """
    Функция принимает json файл, обрабатывает его и возвращает список с данными.
    :param filename: Json файл.
    :return: Список обработанных данных.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            json_file = json.load(file)
            return json_file
    except Exception:
        return []


def get_operations_sum_in_rub(operation: list) -> float:
    """
    Функция принимает данные о банковской операции
     и возвращает сумму транзакции в рублях или выбрасывает исключение.
    :param operation: Данные банковской операции.
    :return: Сумма в рублях
    """
    for data in operation:
        amount = data["operationAmount"]["amount"]
        code = data["operationAmount"]["currency"]["code"]
        if code == "RUB":
            return float(amount)
        else:
            raise ValueError("Транзакция выполнена не в рублях. Укажите транзакцию в рублях.")


def generator_data_operations(list_operations: list) -> Generator:
    """
    Функция-генератор принимает данные о банковских операциях
     и возвращает данные об одной операции, когда ее запросит пользователь.
    :param list_operations: Список с данными о банковских операциях.
    :return: Данные об одной операции.
    """
    for i in list_operations:
        yield [i]
