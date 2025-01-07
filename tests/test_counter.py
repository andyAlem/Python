from src.counter import get_counter_operations_by_description
from collections import Counter

def test_get_counter_operations_by_description(transactions_for_search_operations):
    """Тест функции подсчета"""
    word = ["перевод"]
    result = get_counter_operations_by_description(transactions_for_search_operations, word)
    expected = Counter({
        "перевод организации": 3,
        "перевод со счета на счет": 1
    })
    assert result == expected


def test_get_counter_operations_by_description_no_full_matching(transactions_for_search_operations):
    """Тест функции подсчета без полного совпадения"""
    word = ["вклад"]
    result = get_counter_operations_by_description(transactions_for_search_operations, word)
    expected = Counter({
        "открытие вклада": 1
    })
    assert result == expected


def test_get_counter_operations_by_description_upper(transactions_for_search_operations):
    """Тест функции с другим регистром"""
    word = ["ПЕРЕВОД"]
    result = get_counter_operations_by_description(transactions_for_search_operations, word)
    expected = Counter({
        "перевод организации": 3,
        "перевод со счета на счет": 1
    })
    assert result == expected


