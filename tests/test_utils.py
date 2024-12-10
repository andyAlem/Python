from src.utils import get_transactions


def test_get_transactions_operations(path_to_file):
    """Тестирует корректность обработки operations.json, сравниваем с первым элементом"""
    result = get_transactions(path_to_file)
    assert result[0] == {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


def test_get_transactions_path_error(path_is_not_valid):
    """Тестируем функцию, если указан неверный путь к файлу"""
    assert get_transactions(path_is_not_valid) == []



