from collections import Counter

# from src.transactions_csv import get_transactions_csv


def get_counter_operations_by_description(dictionaries, operations):
    """Функция для подсчета количества банковских операций определенного типа"""
    operations_list = []
    operations = [op.strip().lower() for op in operations]

    for dictionary in dictionaries:
        description = dictionary.get("description", "").lower()

        if any(op in description for op in operations):
            operations_list.append(description)

    return Counter(operations_list)


# if __name__ == "__main__":
#     dictionaries_1 = get_transactions_csv("../data/transactions.csv")
#     list_for_search = ["Открытие вклад"]
#     result = get_counter_operations_by_description(dictionaries_1, list_for_search)
#     print(dict(result))
