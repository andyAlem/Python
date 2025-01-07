import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_card_or_account,expected_mask",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 ** **** 6361"),
        ("MasterCard 7158300734726758", "MasterCard 7158 ** **** 6758"),
        ("Maestro 1596837868705199", "Maestro 1596 ** **** 5199"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 ** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Счет 35383033474447895560", "Счет **5560"),
    ],
)
def test_mask_account_card(input_card_or_account, expected_mask):
    """Тестирование функции для разных типов карт и номеров счетов"""
    assert mask_account_card(input_card_or_account) == expected_mask


def test_mask_account_wrong_length():
    """Проверка, что функция корректно обрабатывает входные данные, где номер счета меньше ожидаемой длины"""
    assert mask_account_card("Счет 007") == "Счет **007"


def test_get_date_correct_format():
    """Тестирование правильности преобразования даты"""
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024 02:26:18"


def test_get_date_no_input():
    """Тестирование обработки неправильного формата даты"""
    with pytest.raises(ValueError):
        get_date("test_get_date_no_input")
