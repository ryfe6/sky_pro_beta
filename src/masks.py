import logging


def mask_card(num_card: str) -> str:
    """
    Функция принимает номер карты, маскирует его и
    возвращает замаскированный номер с отступами после 4 символов.
    :param num_card: Номер для маскирования
    :return: Маскированный по правилу номер
    """
    num_list = list(num_card.replace(" ", ""))
    if len(num_list) == 16:
        num_list[6:11] = "******"
        return (
            f'{"".join(num_list[0:4])} {"".join(num_list[4:8])} ' f'{"".join(num_list[8:12])} {"".join(num_list[13:])}'
        )
    return "Неправильный номер карты"


def score_mask(num_score: str) -> str:
    """
    Функция принимает номер счета и возвращает последние 4 цифры номера счета.
    :param num_score: Номер счета для маскирования
    :return: Маскированный по правилу номер счета
    """
    if len(num_score) != 20:
        return "Неправильный номер счета"
    else:
        score_list = list(num_score)
        return f'**{"".join(score_list[-4:])}'


logging.basicConfig(
    level=logging.DEBUG,
    filename="my_logging.log",
    format="%(levelname)s, (%(asctime)s): %(message)s " "Line %(lineno)d) [%(filename)s]",
    datefmt="%d/%m/%Y %I:%M:%S",
    encoding="utf-8",
    filemode="w",
)

logging.info("test")
