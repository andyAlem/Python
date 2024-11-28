import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("input_card_or_account,expected_mask", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ("Счет 73654108430135874305", "Счет **4305"),
    ("Счет 64686473678894779589", "Счет **9589"),
    ("Счёт 35383033474447895560", "Счет **5560"),
])
def test_mask_account_card(input_card_or_account, expected_mask):
    """  Тестирования функции для разных типов карт и номера счета.
    Учитывает разные форматы написания "Cчет или Счёт" """
    assert mask_account_card(input_card_or_account) == expected_mask

def test_mask_account_wrong_length():
    """Проверка, что функция корректно обрабатывает входные данные,
        где номер счета меньше ожидаемой длины."""
    assert mask_account_card("Счёт 007") == "Счет **007"


def test_get_date_correct_format():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"







