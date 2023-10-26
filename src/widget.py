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
            num_cards = list(num_card)  # Превращаем строку в список, чтобы изменить ее содержимое
            num_cards[6:11] = "******"
            return (
                f'{"".join(name_card)} '
                f'{"".join(num_cards[0:4])} {"".join(num_cards[4:8])} '
                f'{"".join(num_cards[8:12])} {"".join(num_cards[12:])}'
            )
        else:
            return "Введен некорректный номер карты"
    return "yps"


def filter_date(data: str) -> str:
    """
    Функция принимает на вход строку, вида '2018-07-11T02:26:18.671407.'
    Возвращает строку с датой в виде "11.07.2018."
    :param data: Принимает дату в формате строки.
    :return Возвращает Отформатированную строку с датой.
    """
    date = data[0:10].replace("-", "")
    return f"{''.join(date[-2:])}.{''.join(date[-4:-2])}.{''.join(date[-8:-4])}"


def dlc_task_1(user_list: list) -> list:
    """
    Функция принимает список, проверяет его на совпадение первой и последней буквы.
    :param user_list: Принимает пользовательский список.
    :return Возвращает список со совпадениями.
    """
    sort_list = []
    for words in user_list:
        if words == "":
            sort_list.append(words)
        elif words[0] == words[-1]:
            sort_list.append(words)
        else:
            pass
    return sort_list


def dlc_task_2(user_list: list) -> int:
    """
    Функция принимает список чисел, и возвращает наибольшую сумму составленную из двух чисел имеющихся в списке.
    :param user_list:
    :return: Максимальная сумма состоящая из двух чисел или 0, если передано 1 или 0 чисел.
    """
    if len(user_list) < 2:
        return 0
    else:
        max_sum = 0
        for num in user_list:
            for num_2 in user_list:
                if num == num_2:
                    pass
                else:
                    two_sum = num * num_2
                    if two_sum > max_sum:
                        max_sum = two_sum
                    else:
                        pass
        return max_sum
