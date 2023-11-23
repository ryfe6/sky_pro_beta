from src.logger import setup_logging


def mask_card(num_card: str) -> str:
    """
    Функция принимает номер карты, маскирует его и
    возвращает замаскированный номер с отступами после 4 символов.
    :param num_card: Номер для маскирования
    :return: Маскированный по правилу номер
    """
    logger.info("mask_card started")
    num_list = list(num_card.replace(" ", ""))
    if len(num_list) == 16:
        num_list[6:11] = "******"
        logger.info("mask_card finished true")
        return (
            f'{"".join(num_list[0:4])} {"".join(num_list[4:8])} ' f'{"".join(num_list[8:12])} {"".join(num_list[13:])}'
        )
    logger.info("mask_card finished false")
    return "Неправильный номер карты"


def score_mask(num_score: str) -> str:
    """
    Функция принимает номер счета и возвращает последние 4 цифры номера счета.
    :param num_score: Номер счета для маскирования
    :return: Маскированный по правилу номер счета
    """
    logger.info("Score mask started")
    if len(num_score) != 20:
        logger.info("Score_mask finished false")
        return "Неправильный номер счета"
    else:
        score_list = list(num_score)
        logger.info("score_mask finished true")
        return f'**{"".join(score_list[-4:])}'


logger = setup_logging()
