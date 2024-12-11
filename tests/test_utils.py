import os
import json
from src.utils import get_transactions
from unittest.mock import patch, mock_open


def test_get_transactions():
    """Тест на успешную загрузку операций из файла json"""
    mock_data = '[{"id": "1109090", "amount": 0.998}, {"id": "122123", "amount": 9090}]'
    with patch("builtins.open", mock_open(read_data=mock_data)): #https://docs.python.org/3/library/unittest.mock.html
        result = get_transactions("hier_should_be_path_.json")
    assert result == [{"id": "1109090", "amount": 0.998}, {"id": "122123", "amount": 9090}]







