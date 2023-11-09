def dictionary_list_filter(dict_list: list, state: str = "EXECUTED") -> list:
    """
    Функция принимает список словарей, сортирует его по нужному ключу
    и возвращает обратно отсортированный словарь.
    :param dict_list: Полученный список.
    :param state: Полученный ключ, по которому будет сортироваться словарь.
    :return: Отсортированный по правилу словарь.
    """
    new_dict_list = []
    for diction in dict_list:
        if state == "EXECUTED":
            if diction["state"] == "EXECUTED":
                new_dict_list.append(diction)
        elif state == "CANCELED":
            if diction["state"] == "CANCELED":
                new_dict_list.append(diction)
    return new_dict_list


def dictionary_list_filter_time(dict_list: list, filter_: str = "low") -> list[dict] | str:
    """
     Функция принимает список словарей, который надо отсортировать и фильтр по котору будет отсортирован.
     Возвращает отсортированный список словарей.
    :param dict_list: Список словарей.
    :param filter_: Фильтр для сортировки. 'Low' -> по убыванию, 'high' -> по возрастанию.
    :return: Отсортированный по правилу список словарей
    """
    if filter_ == "low":
        return sorted(dict_list, key=lambda data: data['date'], reverse=True)
    elif filter_ == "high":
        return sorted(dict_list, key=lambda data: data['date'])
    return "Что то пошло не так..."
