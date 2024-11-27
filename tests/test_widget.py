import pytest

from src.widget import mask_account_card, get_date


def test_mask_account_card_input_account(inputs_mask_account):
    """"Тест для проверки маскировки аккаунта"""
    assert mask_account_card(inputs_mask_account)

def test_mask_account_card_input_card(inputs_mask_account):
    """Тест для проверки маскировки банковской карты"""
    assert mask_account_card(inputs_mask_account)


@pytest.mark.parametrize(
    "input_card_or_account_number, mask",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Счет 35383033474447895560", "Счет **5560")
    ],
)
def test_mask_account_card(input_card_or_account_number, mask):
    """Параметризованные тесты с разными типами карт и счетов для проверки универсальности функции."""
    assert mask_account_card(input_card_or_account_number) == mask

@pytest.mark.parametrize("input_non_standard", [
    (""),
    ("asiV"),
    ("Шито"),
    ("11112")
])

def test_mask_account_card_invalid_input(input_non_standard):
    """Тестирование функции на обработку некорректных входных данных
        и проверка ее устойчивости к ошибкам."""
    with pytest.raises(ValueError):
        mask_account_card(input_non_standard)


def test_get_date():
    """Тест на правильность преобразования даты."""
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"

@pytest.mark.parametrize("date_format_not_correct", [
    "",
    "for test",
    "02/58/8888",
    "1989-1-3",
])
def test_get_date_missing_date(date_format_not_correct):
    """Проверка работы функции на различных входных форматах даты, нестандартные строки с датами.
    Проверка, что функция корректно обрабатывает входные строки, где отсутствует дата."""
    assert get_date(date_format_not_correct)

