import json
import logging
from typing import Generator, Any


def get_load_json_file(filename: str) -> Any:
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


def get_operations_sum_in_rub(operation: Any) -> Any:
    """
    Функция принимает данные о банковской операции
     и возвращает сумму транзакции в рублях или выбрасывает исключение.
    :param operation: Данные банковской операции.
    :return: Сумма в рублях
    """

    amount = operation["amount"]
    code = operation["currency"]["code"]
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
        yield i["operationAmount"]


logging.basicConfig(
    level=logging.DEBUG,
    filename="my_logging.log",
    format="%(levelname)s, (%(asctime)s): %(message)s " "Line %(lineno)d) [%(filename)s]",
    datefmt="%d/%m/%Y %I:%M:%S",
    encoding="utf-8",
    filemode="w",
)

logging.debug("test")
