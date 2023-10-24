def mask_card_and_score(info_card_or_score: str) -> str:
    """
    Функция принимает на вход строку информацией тип карты/счета и номер карты/счета.
    Возвращает эту строку с замаскированным номером карты/счета.
    :param info_card_or_score: Имя и номер карты/счета для маскирования.
    :return: Имя и номер карты/счета замаскированный по правилу.
    """
    # Если переданные данные начинаются со слова счет, то функция распознает данные как счет и номер счета
    if info_card_or_score.lower()[0:4] == "счет":
        num_score = "".join(filter(lambda score: score.isdigit(), info_card_or_score))  # Вытаскиваем из строки цифры
        if len(num_score) == 20:
            return f"Счет **{num_score[-4:]}"
        else:
            return "Введен некорректный номер счета"
    # Если переданные данные не начинаются со слова счет, то функция распознает данные как название и номер карты
    elif info_card_or_score.lower()[0:4] != "счет":
        num_card = "".join(filter(lambda card: card.isdigit(), info_card_or_score))  # Вытаскиваем из строки цифры
        if len(num_card) == 16:
            name_card = [name for name in info_card_or_score if not name.isdigit()]  # Вытаскиваем из строки имя карты
            num_card = list(num_card)  # Превращаем строку в список, чтобы изменить ее содержимое
            num_card[6:11] = "******"
            return (
                f'{"".join(name_card)} '
                f'{"".join(num_card[0:4])} {"".join(num_card[4:8])} '
                f'{"".join(num_card[8:12])} {"".join(num_card[12:])}'
            )
        else:
            return "Введен некорректный номер карты"


def filter_date(data: str) -> str:
    """
    Функция принимает на вход строку, вида '2018-07-11T02:26:18.671407.'
    Возвращает строку с датой в виде "11.07.2018."
    :param data: Принимает дату.
    :return Возвращает Отформатированную строку с датой.
    """
    date = data[0:10].replace("-", "")
    return f"{''.join(date[-2:])}.{''.join(date[-4:-2])}.{''.join(date[-8:-4])}"
