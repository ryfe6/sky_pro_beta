from src import generators


def test_get_id_transactions(test_data_generators):
    gen = generators.get_id_transactions(test_data_generators, "USD")
    first_assert = next(gen)
    second_assert = next(gen)
    assert first_assert == {
        "date": "2018-06-30T02:08:58.425572",
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "id": 939719570,
        "operationAmount": {"amount": "9824.07", "currency": {"code": "USD", "name": "USD"}},
        "state": "EXECUTED",
        "to": "Счет 11776614605963066702",
    }
    assert second_assert == {
        "date": "2019-04-04T23:20:05.206878",
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "id": 142264268,
        "operationAmount": {"amount": "79114.93", "currency": {"code": "USD", "name": "USD"}},
        "state": "EXECUTED",
        "to": "Счет 75651667383060284188",
    }


def test_transaction_descriptions(test_data_generators):
    gen = generators.transaction_descriptions(test_data_generators)
    list_assert_transaction = []
    list_test_transaction = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
    ]
    for i in range(4):
        list_assert_transaction.append(next(gen))
    assert list_assert_transaction == list_test_transaction


def test_card_number_generator():
    gen = generators.card_number_generator(88888888, 88888890)
    first_num = next(gen)
    second_num = next(gen)
    third_num = next(gen)
    assert first_num == "0000 0000 8888 8888"
    assert second_num == "0000 0000 8888 8889"
    assert third_num == "0000 0000 8888 8890"
