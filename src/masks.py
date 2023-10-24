import os


def mask_card(num_card: str) -> str:
    """
    Функция принимает номер карты, маскирует его и
    возвращает замаскированный номер с отступами после 4 символов.
    :param num_card: Номер для маскирования
    :return: Маскированный по правилу номер
    """
    num_list = list(num_card.replace(" ", ""))
    if len(num_list) != 16 or len(num_list) > 16:
        return "Неправильный номер карты"
    elif len(num_list) == 16:
        num_list[6:11] = "******"
        return (
            f'{"".join(num_list[0:4])} {"".join(num_list[4:8])} ' f'{"".join(num_list[8:12])} {"".join(num_list[12:])}'
        )


print(mask_card("7000792289606361"))


def score_mask(num_score: str) -> str:
    """
    Функция принимает номер счета и возвращает последние 4 цифры номера счета.
    :param num_score: Номер счета для маскирования
    :return: Маскированный по правилу номер счета
    """
    score_list = list(num_score)
    return f'**{"".join(score_list[-4:])}'


# def direct(way, counting=None):
#     directory_count = 0
#     file_count = 0
#     if counting is not None:
#         ls = os.walk(way)
#         # way = os.listdir('C:/Users/ryfe/PycharmProjects/pythonProject4/src')
#     else:
#         ls = os.listdir(way)
#
#     for file in ls:
#         for i in file:
#             if i[0] in '.':
#                 directory_count += 1
#                 break
#             elif i == ".":
#                 file_count += 1
#                 break
#             else:
#                 directory_count += 1
#                 break
#
#     dictionary = {"Файлы": directory_count, "Папки": directory_count}
#      return dictionary
#
#
# way_os = ('C:/Users/ryfe/PycharmProjects/pythonProject4')
#
# print(direct(way_os))
