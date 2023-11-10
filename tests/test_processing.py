from src import processing


def test_dictionary_list_filter(test_data_processing):
    assert processing.dictionary_list_filter(test_data_processing, "CANCELED") == var_3
    assert processing.dictionary_list_filter(test_data_processing) == var_4


def test_dictionary_list_filter_time(test_data_processing):
    assert processing.dictionary_list_filter_time(test_data_processing) == var
    assert processing.dictionary_list_filter_time(test_data_processing, "high") == var_2
    assert processing.dictionary_list_filter_time(test_data_processing, "None") == "Что то пошло не так..."


var = [
    {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
    {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
    {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
]

var_2 = [
    {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
    {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
    {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
]

var_3 = [{"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"}]

var_4 = [
    {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
    {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
]
