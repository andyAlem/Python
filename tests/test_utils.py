import os
import json
from src.utils import get_transactions, transactions_amount_in_rub
from src.external_api import convert_to_rub
from unittest.mock import patch
import pytest
from dotenv import load_dotenv
load_dotenv(".env")
API_KEY = os.getenv("API_KEY")

# from tests.conftest import path_to_file
#
# API_KEY = os.getenv("API_KEY")
# print(f"All environment variables: {os.environ}")
# if not API_KEY:
#     print("Error: API_KEY not found in .env file.")
# else:
#     print(f"API_KEY loaded: {API_KEY}")
#
#
# def test_get_transactions_operations(path_to_file):
#     """Тестирует корректность обработки operations.json, сравниваем с первым элементом"""
#     result = get_transactions(path_to_file)
#     assert result[0] == {
#         "id": 441945886,
#         "state": "EXECUTED",
#         "date": "2019-08-26T10:50:58.294041",
#         "operationAmount": {
#             "amount": "31957.58",
#             "currency": {"name": "руб.", "code": "RUB"},
#         },
#         "description": "Перевод организации",
#         "from": "Maestro 1596837868705199",
#         "to": "Счет 64686473678894779589",
#     }
#
#
# def test_get_transactions_path_error(path_is_not_valid):
#     """Тестируем функцию, если указан неверный путь к файлу"""
#     assert get_transactions(path_is_not_valid) == []
# #############################################################################
#
# @pytest.fixture
# def transactions_for_test():
#     """Пример реальных транзакций для тестов"""
#     return [
#         {
#             "id": 41428829,
#             "state": "EXECUTED",
#             "date": "2019-07-03T18:35:29.512364",
#             "operationAmount": {
#                 "amount": "224",  # Значение как строка
#                 "currency": {
#                     "name": "EUR",
#                     "code": "EUR"
#                 }
#             },
#             "description": "Перевод организации",
#             "from": "MasterCard 7158300734726758",
#             "to": "Счет 35383033474447895560"
#         }
#     ]
#
# def test_transactions_amount_in_rub_eur(transactions_for_test):
#     """Тестирует конвертацию суммы из EUR в рубли с реальным API"""
#     transaction_id = 41428829  # ID транзакции, которая в EUR
#
#     # Получаем данные из реальной функции
#     result = transactions_amount_in_rub(transactions_for_test, transaction_id)
#
#     # Печатаем результат для отладки
#     print(f"Test Result: {result}")
#
#     # Ожидаемый результат из API
#     expected_result = 24294.682272  # Мы видели это в ответе от API
#
#     # Проверяем результат функции
#     assert result == expected_result






