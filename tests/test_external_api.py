import pytest
from unittest.mock import patch

from src.external_api import convert_to_rub


@patch("src.external_api.requests.get")
def test_convert_to_rub_api_failure(mock_get):
    """Проверяем некорректный API"""
    mock_get.return_value.status_code = 500

    result = convert_to_rub(100, "USD")

    assert result == 0
    mock_get.assert_called_once()



@pytest.mark.parametrize("amount, currency, mock_result, expected", [
    (1, "USD", {"result": 101}, 101),
    (2, "EUR", {"result": 202}, 202),
    (3, "USD", {"result": 303}, 303),
])
@patch("src.external_api.requests.get")
def test_convert_to_rub_success(mock_get, amount, currency, mock_result, expected):
    """Тестируем корректную работу функии"""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_result

    result = convert_to_rub(amount, currency)

    assert result == expected
    mock_get.assert_called_once()





