from src.utils import get_transactions, transactions_amount_in_rub
from unittest.mock import patch
import pytest

from tests.conftest import path_to_file


def test_get_transactions_operations(path_to_file):
    """Тестирует корректность обработки operations.json, сравниваем с первым элементом"""
    result = get_transactions(path_to_file)
    assert result[0] == {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


def test_get_transactions_path_error(path_is_not_valid):
    """Тестируем функцию, если указан неверный путь к файлу"""
    assert get_transactions(path_is_not_valid) == []



@pytest.fixture
def operations_file_path():
    """Возвращает путь к operations.json"""
    return "/mnt/data/operations.json"  # Убедитесь, что файл доступен по этому пути

@pytest.fixture
def transactions(operations_file_path):
    """Загружает данные транзакций из operations.json"""
    return get_transactions(operations_file_path)

@patch("src.utils.transactions.convert_to_rub")
def test_transactions_amount_in_rub_rub(mock_convert_to_rub, transactions):
    """Тестирует получение суммы в рублях из реальных данных"""
    transaction_id = 441945886  # ID транзакции, которая в рублях
    result = transactions_amount_in_rub(transactions, transaction_id)
    assert result == 31957.58  # Проверяем ожидаемую сумму






