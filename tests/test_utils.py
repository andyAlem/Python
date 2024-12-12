import json
import os
from unittest.mock import mock_open, patch

import pytest

from src.external_api import convert_to_rub
from src.utils import get_transactions, transaction_amount_in_rub


def test_get_transactions(mock_data):
    """Тест на успешную загрузку операций из файла json. Используем фикстуру mock_data"""
    with patch(
        "builtins.open", mock_open(read_data=mock_data)
    ):  # https://docs.python.org/3/library/unittest.mock.html
        result = get_transactions("hier_should_be_path_.json")
    assert result == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    ]


def test_get_transactions_file_not_found():
    """Файл отсутствует"""
    with patch(
        "builtins.open", side_effect=FileNotFoundError
    ):  # https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch
        result = get_transactions("file_does_not_exist.json")
    assert result == []


def test_transactions_file_invalid_json():
    """Тест на поврежденный файл, или который не может быть прочитан"""
    with patch("builtins.open", mock_open(read_data="Currepted JSON")):
        result = get_transactions("path_to_file.json")
    assert result == []


#############
def test_transaction_amount_in_rub_with_rub(transactions_for_test):
    """Тестируем обработку транзакции в рублях. Не должно быть конвертации"""
    transactions = transactions_for_test
    result = transaction_amount_in_rub(transactions, 441945886)
    assert result == 31957.58


def test_transaction_amount_in_rub_transaction_not_found(transactions_for_test):
    """Транзакция отсутствует"""
    transactions = transactions_for_test
    result = transaction_amount_in_rub(transactions, 7009)
    assert result == "Tранзакция не найдена"


@patch("src.external_api.convert_to_rub", side_effect=Exception("API Error"))
def test_transaction_amount_in_rub_conversion_error(mock_convert_to_rub, transactions_for_test):
    """Тест на ошибку API"""
    transactions = transactions_for_test
    result = transaction_amount_in_rub(transactions, 41428829)
    assert result == "Конвертация невозможна"


@patch("src.utils.convert_to_rub", side_effect=Exception("API Error"))
def test_transaction_amount_in_rub_conversion_error(mock_convert_to_rub, transactions_for_test):
    """Тест на обработку исключения при вызове convert_to_rub"""

    result = transaction_amount_in_rub(transactions_for_test, 41428829)
    assert result == "Конвертация невозможна"
    mock_convert_to_rub.assert_called_once_with(transactions_for_test[0])


@patch("src.utils.convert_to_rub", return_value=895)
def test_transaction_amount_in_rub_with_usd_currency(mock_convert_to_rub, transactions_for_test):
    """Тестируем функцию на работу с валютой USD"""
    transactions = transactions_for_test

    print(f"Testing transaction with ID 41428829:")
    print(f"Transactions: {transactions}")

    result = transaction_amount_in_rub(transactions, 41428829)

    print(f"Result: {result}")
    mock_convert_to_rub.assert_called_once_with(transactions[0])
    assert result == 895




