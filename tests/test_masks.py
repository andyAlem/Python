import pytest

from src.masks import get_mask_account, get_mask_card_number
from tests.conftest import card_nonstandard_cards, card_number_empty


@pytest.mark.parametrize("card_number, expected",
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

def test_get_mask_card_number_nonstandard(card_nonstandard_cards):
    assert get_mask_card_number(card_nonstandard_cards)