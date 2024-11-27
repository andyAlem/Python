dictionaries_to_filter = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

dictionaries_to_sort = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(dictionaries_to_filter: list, state: str = "EXECUTED") -> list:
    """Функция возвращает список словарей по фильтру значения state"""

    return [i for i in dictionaries_to_filter if i.get("state") == state]


def sort_by_date(dictionaries_to_sort: list, reverse_sorted: bool = True) -> list:
    """Функция возвращает список словарей, отсортированный по дате."""

    return sorted(dictionaries_to_sort, key=lambda x: x["date"], reverse=reverse_sorted)
