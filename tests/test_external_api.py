
from unittest.mock import patch

from src.external_api import convert_to_rub


@patch("src.external_api.requests.get")
def test_convert_to_rub_api_failure(mock_get):
    """Проверяем некорректный API"""
    mock_get.return_value.status_code = 500

    result = convert_to_rub(100, "USD")

    assert result == 0
    mock_get.assert_called_once()






