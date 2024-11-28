def filter_by_currency(transactions, currency):
    """Функция принимает на вход список словарей, представляющих транзакции.
    Функция должна возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD). """

    for transaction in transactions:
        if transaction.get('operationAmount', {}).get('currency', {}).get('code') == currency:
            yield transaction

