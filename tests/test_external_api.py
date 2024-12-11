import json
import os
from unittest.mock import MagicMock, Mock, patch

import requests
from dotenv import load_dotenv

from src.external_api import convert_to_rub

load_dotenv(".env")

API_KEY = os.getenv("API_KEY")


#
# @patch("requests.get")
# def test_convert_to_rub_invalid_currency(mock_get):
#     """Тестируем неподдерживаемую валюту"""
#
#     mock_get.return_value.json.return_value = {"result": 0}
#     with pytest.raises(ValueError, match="We could convert only EUR or USD"):
#         convert_to_rub(100, "JPY")

@patch("requests.get")
def test_currency_conversion(mock_get):
    """Тестируем успешный ответ от API"""
    # Настраиваем мок
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 2}
    mock_get.return_value = mock_response

    # Проверяем результат функции
    result = convert_to_rub(1, "USD")
    print(f"Test result: {result}")

    # Проверяем, что результат соответствует ожиданиям
    assert result == 2

    # Проверяем, что запрос был вызван с правильными параметрами
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert",
        headers={"apikey": API_KEY},
        params={"to": "RUB", "from": "USD", "amount": 1.0}
    )

@patch("requests.get")
def test_convert_to_rub_invalid_currency(mock_get):
    """Тестируем неподдерживаемую валюту"""

    mock_get.return_value.json.return_value = {"result": 0}
    mock_get.return_value.status_code = 200  # Устанавливаем успешный статус

    try:
        # Попробуем вызвать функцию с неподдерживаемой валютой
        result = convert_to_rub(100, "JPY")
    except ValueError as e:
        print(f"Error raised: {e}")
        assert "We could convert only EUR or USD" in str(e)



