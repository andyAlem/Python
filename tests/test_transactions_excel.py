from unittest.mock import patch

import pandas as pd
import pytest

from src.transactions_excel import get_transactions_excel


def test_get_transactions_excel_valid_file(excel_data):
    """Тест успешного чтения Excel-файла"""
    df = pd.DataFrame(excel_data)
    with patch("os.path.isfile", return_value=True):
        with patch("pandas.read_excel", return_value=df) as mock_read_excel:
            result = get_transactions_excel("mock_excel.xlsx")

            assert len(result) == len(excel_data["id"])
            assert result[0]["id"] == excel_data["id"][0]
            assert result[0]["state"] == excel_data["state"][0]
            assert result[0]["amount"] == excel_data["amount"][0]

            mock_read_excel.assert_called_once()


def test_get_transactions_excel_invalid_format():
    """Тест на обработку некорректного файла"""
    with patch("os.path.isfile", return_value=True):
        with pytest.raises(ValueError, match="Неверный формат файла"):
            get_transactions_excel("invalid_file.txt")


def test_get_transactions_excel_empty_file():
    """Тест обработки пустого Excel-файла."""
    empty_df = pd.DataFrame()
    with patch("os.path.isfile", return_value=True):
        with patch("pandas.read_excel", return_value=empty_df):
            with pytest.raises(ValueError, match="Excel файл пустой"):
                get_transactions_excel("empty_file.xlsx")


def test_get_transactions_excel_file_not_found():
    """Тестируем отсутствие excel файла"""
    with patch("os.path.isfile", return_value=False):
        with pytest.raises(FileNotFoundError, match="Excel файл 'not_found.xlsx' не найден."):
            get_transactions_excel("not_found.xlsx")


def test_get_transactions_excel_corrupted_file():
    """Тест на обработку поврежденного файла"""
    with patch("os.path.isfile", return_value=True):
        with patch("pandas.read_excel", side_effect=ValueError("Некорректные данные")):
            try:
                get_transactions_excel("corrupted_file.xlsx")
            except ValueError as ex:
                assert "Некорректные данные" in str(ex)
