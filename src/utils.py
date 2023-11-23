import json
from src.logger import setup_logging
from typing import Generator, Any


def get_load_json_file(filename: str) -> Any:
    """
    Функция принимает json файл, обрабатывает его и возвращает список с данными.
    :param filename: Json файл.
    :return: Список обработанных данных.
    """
    logger.info("get_load_json_file started")
    try:
        with open(filename, "r", encoding="utf-8") as file:
            json_file = json.load(file)
            logger.info("get_load_json_file finished")
            return json_file
    except Exception as e:
        logger.exception(e)
        return []


def get_operations_sum_in_rub(operation: Any) -> Any:
    """
    Функция принимает данные о банковской операции
     и возвращает сумму транзакции в рублях или выбрасывает исключение.
    :param operation: Данные банковской операции.
    :return: Сумма в рублях
    """
    logger.info("get_operations_sum_in_rub start")
    amount = operation["amount"]
    code = operation["currency"]["code"]
    if code == "RUB":
        logger.info("get_operations_sum_in_rub finished")
        return float(amount)
    else:
        logger.exception(ValueError("Транзакция выполнена не в рублях. Укажите транзакцию в рублях."))
        raise ValueError("Транзакция выполнена не в рублях. Укажите транзакцию в рублях.")


def generator_data_operations(list_operations: list) -> Generator:
    """
    Функция-генератор принимает данные о банковских операциях
     и возвращает данные об одной операции, когда ее запросит пользователь.
    :param list_operations: Список с данными о банковских операциях.
    :return: Данные об одной операции.
    """
    logger.info("generator_data_operations start")
    for i in list_operations:
        logger.info("generator_data_operations finished")
        yield i["operationAmount"]


logger = setup_logging()

# if __name__ == "__main__":
#     gen = generator_data_operations(get_load_json_file("../data/operations.json"))
#     assert_first = next(gen)
#     print(get_operations_sum_in_rub(assert_first))

