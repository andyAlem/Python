def filter_by_currency(transactions, currency):
    """Функция принимает на вход список словарей, представляющих транзакции.
    Функция должна возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)."""
    # https://sky.pro/media/ispolzovanie-dict-getkey-vmesto-dictkey-v-python/
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions):
    """Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""

    for transaction in transactions:
        description = transaction.get("description", "Описание транзакции отсутствует ")
        yield description


def card_number_generator(start, stop):
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты."""

    if not (1 <= start <= stop <= 9999_9999_9999_9999):
        raise ValueError("Некорректный диапазон")

    for number in range(start, stop + 1):
        card_number = f"{number:016d}"
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
