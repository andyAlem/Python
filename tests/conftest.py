import pytest

@pytest.fixture
def card_number_empty():
    return ""

@pytest.fixture
def nonstandard_cards():
    return [
        ("3434344444444444444433"),
        ("-44444444443rr"),
        ("3398"),
    ]


@pytest.fixture
def mask_account_empty():
    return ""

@pytest.fixture
def nonstandard_accounts():
    return  [
        ("888888888888888888888888888333232"),
        ("9999999"),
        ("12325"),
        ("1"),
        ("0"),
    ],


@pytest.fixture
def list_of_dicts():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
@pytest.fixture
def invalid_list():
    return ["invalid_str_for_test"]