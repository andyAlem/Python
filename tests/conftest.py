import pytest

from src.utils import get_transactions


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
    return (
        [
            ("888888888888888888888888888333232"),
            ("9999999"),
            ("12325"),
            ("1"),
            ("0"),
        ],
    )


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


@pytest.fixture
def list_of_dicts_with_same_dates():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def inputs_mask_account():
    return "Счет 64686473678894779589"


@pytest.fixture
def inputs_mask_account_card():
    return "Visa Platinum 7000792289606361"


@pytest.fixture
def transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def path_to_file():
    return "data/operations.json"


@pytest.fixture
def path_is_not_valid():
    return "/home/andrej/data/operations.json"


@pytest.fixture
def get_transactions_data(path_to_file):
    return get_transactions(path_to_file)


@pytest.fixture
def transactions_for_test():
    """Пример реальных транзакций для тестов"""
    return [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
    ]


@pytest.fixture
def mock_data():
    return """
    [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        }
    ]
    """


@pytest.fixture
def example_csv():
    return """id;state;date;amount;currency_name;currency_code;from;to;description
650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации
3598919;EXECUTED;2020-12-06T23:00:58Z;29740;Peso;COP;Discover 3172601889670065;Discover 0720428384694643;Перевод с карты на карту
593027;CANCELED;2023-07-22T05:02:01Z;30368;Shilling;TZS;Visa 1959232722494097;Visa 6804119550473710;Перевод с карты на карту
"""

@pytest.fixture
def excel_data():
    return {
        "id": [650703, 3598919, 593027],
        "state": ["EXECUTED", "EXECUTED", "CANCELED"],
        "date": ["2023-09-05T11:30:32Z", "2020-12-06T23:00:58Z", "2023-07-22T05:02:01Z"],
        "amount": [16210, 29740, 30368],
        "currency_name": ["Sol", "Peso", "Shilling"],
        "currency_code": ["PEN", "COP", "TZS"],
        "from": ["Счет 58803664561298323391", "Discover 3172601889670065", "Visa 1959232722494097"],
        "to": ["Счет 39745660563456619397", "Discover 0720428384694643", "Visa 6804119550473710"],
        "description": ["Перевод организации", "Перевод с карты на карту", "Перевод с карты на карту"],
    }