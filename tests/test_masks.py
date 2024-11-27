import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1596837868705199", "1596 83** **** 5199"),
        ("7158300734726758", "7158 30** **** 6758"),
        ("6831982476737658", "6831 98** **** 7658"),
        ("8990922113665229", "8990 92** **** 5229"),
    ],
)
def test_get_mask_card_number(card_number, expected):
    """Тестирование правильности маскирования номера карты"""
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_empty(card_number_empty):
    """Проверка, что функция корректно обрабатывает входные строки, где отсутствует номер карты."""
    assert get_mask_card_number(card_number_empty)


def test_get_mask_card_number_nonstandard(nonstandard_cards):
    """""Проверка, функции на нестандартные карты"""
    assert get_mask_card_number(nonstandard_cards)


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("64686473678894779589", "**9589"),
        ("35383033474447895560", "**5560"),
        ("73654108430135874305", "**4305"),
    ],
)
def test_get_mask_account(account_number, expected):
    """Тестирование правильности маскирования номера счета."""
    assert get_mask_account(account_number) == expected


def test_get_mask_account_empty(mask_account_empty):
    """Тестирование на пустое поле для ввода номера счета"""
    assert get_mask_account(mask_account_empty)


def test_get_mask_account_number_nonstandard(nonstandard_accounts):
    """""Проверка, функции на нестандартные аккаунты"""
    assert get_mask_card_number(nonstandard_accounts)
