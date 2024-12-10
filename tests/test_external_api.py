from unittest.mock import patch
from src.external_api import convert_to_rub, API_KEY
import pytest


@patch("requests.get")
def test_convert_to_rub(mock_get):
    """Тестируем успешный ответ от API"""
    mock_get.return_value.json.return_value = {"result": 1200}
    result = convert_to_rub(400, "USD")
    assert result == 1200
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert",
        headers={"apikey": API_KEY},
        params={"to": "RUB", "from": "USD", "amount": 400}
    )

@patch("requests.get")
def test_convert_to_rub_invalid_currency(mock_get):
    """Тестируем неподдерживаемую валюту"""

    mock_get.return_value.json.return_value = {"result": 0}
    with pytest.raises(ValueError, match="We could convert only EUR or USD"):
        convert_to_rub(100, "JPY")