from collections import Counter

from src.transactions_csv import get_transactions_csv


def get_counter_operations_by_description(dictionaries, operations):
    """Функция для подсчета количества банковских операций определенного типа"""
    operations_list = []
    for dictionary in dictionaries:
        if dictionary["description"] in operations:
            operations_list.append(dictionary["description"])
    return Counter(operations_list)


# if __name__ == "__main__":
#     dictionaries_1 = get_transactions_csv("../data/transactions.csv")
#     list_for_search = ["Открытие вклад"]
#     result = get_counter_operations_by_description(dictionaries_1, list_for_search)
#     print(dict(result))