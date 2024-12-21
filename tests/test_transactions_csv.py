from unittest.mock import mock_open, patch

import pytest

from src.transactions_csv import get_transactions_csv


def test_get_transactions_csv(example_csv):
    """Тестируем чтение csv файла"""
    mock_file_path = "mock_transactions.csv"
    with patch("os.path.isfile", return_value=True), patch("builtins.open", mock_open(read_data=example_csv)):
        transactions = get_transactions_csv(mock_file_path)
        assert len(transactions) == 3
        assert transactions[0]["id"] == "650703"
        assert transactions[1]["state"] == "EXECUTED"
        assert transactions[2]["currency_name"] == "Shilling"


def test_get_transactions_csv_empty():
    """Тестируем чтение пустого csv файла"""
    empty_csv = ""
    mock_file_path = "mock_transactions.csv"
    with patch("os.path.isfile", return_value=True), patch("builtins.open", mock_open(read_data=empty_csv)):
        with pytest.raises(ValueError, match="CSV файл не содержит заголовков или пустой"):
            get_transactions_csv(mock_file_path)


def test_get_transactions_csv_not_found():
    """Файл не может быть найден"""
    mock_file_path = "mock_transactions.csv"
    with patch("os.path.isfile", return_value=False):
        with pytest.raises(FileNotFoundError, match=f"CSV файл '{mock_file_path}' не найден."):
            get_transactions_csv(mock_file_path)


def test_get_transactions_csv_unsupported_files():
    """Тестируем обработку файлов с другим расширением"""
    invalid_file_path = "transactions.txt"  # Неверный формат файла
    with patch("os.path.isfile", return_value=True):
        with pytest.raises(ValueError, match="Неверный формат файла"):
            get_transactions_csv(invalid_file_path)


def test_get_transactions_csv_corrupted_file():
    """csv файл с некорректными данными"""
    invalid_csv_data = "id,state,date,amount\n1,EXECUTED"
    mock_file_path = "mock_transactions.csv"
    with patch("os.path.isfile", return_value=True), patch("builtins.open", mock_open(read_data=invalid_csv_data)):
        with pytest.raises(ValueError, match="Некорректная структура CSV файла"):
            get_transactions_csv(mock_file_path)
