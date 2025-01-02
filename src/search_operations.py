import re

def transactions_search(word, transactions):
    """Функция для поиска в списке словарей операций по заданной строке"""
    return [
        transaction for transaction in transactions
        if re.search(word, transaction['description'], re.IGNORECASE)
    ]