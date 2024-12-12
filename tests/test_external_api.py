from unittest.mock import patch

import pytest

from src.external_api import convert_to_rub


@patch("src.external_api.requests.get")
def test_convert_to_rub_api_failure(mock_get):
    """Проверяем некорректный API"""
    mock_get.return_value.status_code = 500

    transaction = {
        "operationAmount": {"amount": "100", "currency": {"code": "USD"}}
    }
    result = convert_to_rub(transaction)

    assert result == 0
    mock_get.assert_called_once()


@pytest.mark.parametrize(
    "transaction, mock_result, expected",
    [
        ({"operationAmount": {"amount": "1", "currency": {"code": "USD"}}}, {"result": 101}, 101),
        ({"operationAmount": {"amount": "2", "currency": {"code": "EUR"}}}, {"result": 202}, 202),
        ({"operationAmount": {"amount": "3", "currency": {"code": "USD"}}}, {"result": 303}, 303),
    ],
)

@patch("src.external_api.requests.get")
def test_convert_to_rub_success(mock_get, transaction, mock_result, expected):
    """Тестируем корректную работу функии"""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_result

    result = convert_to_rub(transaction)

    assert result == expected
    mock_get.assert_called_once()


def test_convert_to_rub_invalid_currency():
    """Тестируем не корректную валюту"""
    transaction = {"operationAmount": {"amount": "11", "currency": {"code": "FRK"}}}
    with pytest.raises(ValueError, match="Валюта FRK не поддерживается"):
        convert_to_rub(transaction)
