import pytest

from src.processing import filter_by_state, sort_by_date

def test_filter_by_state(list_of_dicts):
    """Тестирование фильтрации списка словарей по заданному статусу state: Executed"""
    assert filter_by_state(list_of_dicts) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_without_state():
    """Проверка работы функции при отсутствии словарей с указанным статусом state в списке."""
    inputs = [
        {"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "test": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    ]
    result = filter_by_state(inputs, state="EXECUTED")
    expected = [{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}]
    assert result == expected

@pytest.mark.parametrize(
    "state, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
    ],
)
def test_filter_by_state_parameterized(list_of_dicts, state, expected):
    """Параметризация тестов для различных возможных значений статуса state"""
    result = filter_by_state(list_of_dicts, state=state)
    assert result == expected



def test_filter_by_state_non_dict(invalid_list):
    """Тестирование функции, если передается не словарь, а строка"""
    with pytest.raises(AttributeError):
        filter_by_state(invalid_list, state="EXECUTED")




