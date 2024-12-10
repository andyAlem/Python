from src.utils import get_transactions


def test_get_transactions_operations_list():
    """Тестирует корректность обработки operations.json, сравниваем с первым элементом"""
    operations_path = "/home/andrej/Poetry_homework/Homework_2.10-1_Git/data/operations.json"
    result = get_transactions(operations_path)
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

