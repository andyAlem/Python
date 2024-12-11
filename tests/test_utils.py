import os
import json
from src.utils import get_transactions
from unittest.mock import patch, mock_open


def test_get_transactions(mock_data):
    """Тест на успешную загрузку операций из файла json"""
    with patch("builtins.open", mock_open(read_data=mock_data)): #https://docs.python.org/3/library/unittest.mock.html
        result = get_transactions("hier_should_be_path_.json")
    assert result == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        }
    ]


def test_get_transactions_file_not_found():
    """Файл отсутствует"""
    with patch("builtins.open", side_effect=FileNotFoundError): #https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch
        result = get_transactions("file_does_not_exist.json")
    assert result == []


def test_transactions_file_invalid_json():
    """Тест на поврежденный файл, или который не может быть прочитан"""
    with patch("builtins.open", mock_open(read_data="Currepted JSON")):
        result = get_transactions("path_to_file.json")
    assert result == []




