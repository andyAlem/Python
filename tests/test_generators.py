import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "currency, expected_result",
    [
        (
            "USD",
            [
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
                    "id": 895315941,
                    "state": "EXECUTED",
                    "date": "2018-08-19T04:27:37.904916",
                    "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод с карты на карту",
                    "from": "Visa Classic 6831982476737658",
                    "to": "Visa Platinum 8990922113665229",
                },
            ],
        ),
        (
            "RUB",
            [
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
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                    "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Visa Platinum 1246377376343588",
                    "to": "Счет 14211924144426031657",
                },
            ],
        ),
    ],
)
def test_filter_by_currency(transactions, currency, expected_result):
    """Tест проверяющий, что функция корректно фильтрует транзакции по заданной валюте."""

    result = list(filter_by_currency(transactions, currency))
    assert result == expected_result


def test_filter_by_currency_eur(transactions):
    """Тест на отсутствующую валюту"""

    currency = "EUR"
    result = list(filter_by_currency(transactions, currency))
    assert result == []


def test_filter_by_currency_transactions_empty():
    """Тестируем обработку пустого списка"""

    transactions = []
    result = list(filter_by_currency(transactions, "USD"))
    assert result == []


def test_transaction_descriptions(transactions):
    """Тестируем генератор на работу для корректного ввода."""

    generator = transaction_descriptions(transactions)

    expected_descriptions = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]

    for expected in expected_descriptions:
        assert next(generator) == expected


@pytest.mark.parametrize(
    "transactions, expected_descriptions",
    [
        (
            [
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                    "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "",
                    "from": "Visa Platinum 1246377376343588",
                    "to": "Счет 14211924144426031657",
                }
            ],
            [""],
        )
    ],
)
def test_transaction_descriptions_empty(transactions, expected_descriptions):
    """Тестируем генератор на обработку пустого описания"""

    descriptions = list(transaction_descriptions(transactions))
    assert descriptions == expected_descriptions


def test_card_number_generator():
    """Тест правильного диапазона"""

    start = 1000000000000000
    stop = 1000000000000003
    expected = ["1000 0000 0000 0000", "1000 0000 0000 0001", "1000 0000 0000 0002", "1000 0000 0000 0003"]

    result = list(card_number_generator(start, stop))
    assert result == expected


def test_card_number_generator_range_invalid():
    """Тестирование с диапазоном больше заданного предела"""

    with pytest.raises(ValueError, match="Некорректный диапазон"):
        list(card_number_generator(10000000000000000, 10000000000000001))
