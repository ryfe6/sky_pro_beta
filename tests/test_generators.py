from src import generators


def test_get_id_transactions(test_data_generators):
    gen = generators.get_id_transactions(test_data_generators, "USD")
    first_assert = next(gen)
    second_assert = next(gen)
    assert first_assert == 939719570
    assert second_assert == 142264268


def test_transaction_descriptions(test_data_generators):
    gen = generators.transaction_descriptions(test_data_generators)
    first_assert = next(gen)
    second_assert = next(gen)
    assert first_assert == 'Перевод организации'
    assert second_assert == 'Перевод со счета на счет'


def test_card_number_generator():
    gen = generators.card_number_generator(88888888, 88888890)
    first_num = next(gen)
    second_num = next(gen)
    third_num = next(gen)
    assert first_num == "0000 0000 8888 8888"
    assert second_num == "0000 0000 8888 8889"
    assert third_num == "0000 0000 8888 8890"
