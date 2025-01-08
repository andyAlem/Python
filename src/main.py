import os

from src.counter import get_counter_operations_by_description
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.search_operations import transactions_search
from src.transactions_csv import get_transactions_csv
from src.transactions_excel import get_transactions_excel
from src.utils import get_transactions
from src.widget import get_date, mask_account_card

JSON_FILE_PATH = "../data/operations.json"
CSV_FILE_PATH = "../data/transactions.csv"
EXCEL_FILE_PATH = "../data/transactions_excel.xlsx"

os.makedirs("logs", exist_ok=True)


def main():
    """Функция выводит банковский транзакции после запроса пользователя"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    user_input = input("Введите номер выбранного пункта меню: ")
    transactions = []

    if user_input == "1":
        print(f"Загружаем данные из JSON файла: {JSON_FILE_PATH}")
        transactions = get_transactions(JSON_FILE_PATH)
    elif user_input == "2":
        print(f"Загружаем данные из CSV файла: {CSV_FILE_PATH}")
        transactions = get_transactions_csv(CSV_FILE_PATH)
    elif user_input == "3":
        print(f"Загружаем данные из XLSX файла: {EXCEL_FILE_PATH}")
        transactions = get_transactions_excel(EXCEL_FILE_PATH)
    else:
        print("Неверный выбор. Завершаю программу.")
        return

    if not transactions:
        print("Не удалось загрузить транзакции. Завершаю программу.")
        return

    filters = {}

    while True:
        status = input("Введите статус для фильтрации (EXECUTED, CANCELED, PENDING): ").upper()
        if status in ["EXECUTED", "CANCELED", "PENDING"]:
            if status:
                filters["status"] = status
            break
        else:
            print(f"Статус операции '{status}' недоступен.")

    sort_choice = input("Отсортировать операции по дате? Да/Нет: ").lower()
    if sort_choice == "да":
        sort_order = input("Отсортировать по возрастанию или по убыванию? ").lower()
        filters["sort"] = sort_order

    currency_filter = input("Выводить только рублевые транзакции? Да/Нет: ").lower()
    if currency_filter == "да":
        filters["currency"] = "RUB"

    description_filter = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").lower()
    if description_filter == "да":
        word = input("Введите слово для поиска: ")
        filters["description"] = word

    filtered_transactions = transactions

    if "status" in filters:
        print(f"Фильтрую по статусу: {filters['status']}")
        filtered_transactions = filter_by_state(filtered_transactions, filters["status"])

    if "sort" in filters:
        print(f"Сортирую по дате: {filters['sort']}")
        reverse = filters["sort"] == "по убыванию"
        filtered_transactions = sort_by_date(filtered_transactions, reverse)

    if "currency" in filters:
        print(f"Фильтрую по валюте: {filters['currency']}")
        filtered_transactions = filter_by_currency(filtered_transactions, filters["currency"])

    if "description" in filters:
        print(f"Фильтрую по слову в описании: {filters['description']}")
        filtered_transactions = list(transactions_search(filters["description"], filtered_transactions))

    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    print("Распечатываю итоговый список транзакций...")
    filtered_transactions = list(filtered_transactions)
    print(f"\nВсего банковских операций в выборке: {len(filtered_transactions)}")

    for transaction in filtered_transactions:
        transaction_date = get_date(transaction["date"])
        description = transaction["description"]

        # JSON!
        if "operationAmount" in transaction:
            amount = transaction.get("operationAmount", {}).get("amount")
            currency = transaction.get("operationAmount", {}).get("currency", {}).get("code", "неизвестно")
            if (
                not amount
                or (isinstance(amount, str) and not amount.replace(".", "", 1).isdigit())
                or (isinstance(amount, float) and not amount.is_integer())
            ):
                amount_display = "Данные отсутствуют в файле"
            else:
                amount_display = str(amount)
            # CSV EXCEL!
        else:
            amount = transaction.get("amount")
            currency = transaction.get("currency_code", "неизвестно")
            if not amount or (isinstance(amount, str) and not amount.replace(".", "", 1).isdigit()):
                amount_display = "Данные отсутствуют в файле"
            else:
                amount_display = str(int(float(amount)))

        if currency == "неизвестно" or currency == "":
            currency_display = "неизвестно"
        else:
            currency_display = currency

        print(f"{transaction_date} {description}")
        if "from" in transaction and "to" in transaction:
            print(f"{mask_account_card(transaction['from'])} -> {mask_account_card(transaction['to'])}")
        elif "from" in transaction:
            print(mask_account_card(transaction["from"]))
        elif "to" in transaction:
            print(mask_account_card(transaction["to"]))

        print(f"Сумма: {amount_display} {currency_display}\n")

    operation_count = input("Подсчитать количество операций определенного типа? Да/Нет: ").lower()
    if operation_count == "да":
        description_list = input("Введите типы операций через запятую: ").split(",")
        counter = get_counter_operations_by_description(filtered_transactions, description_list)
        print("Распечатываю итоговый список транзакций...:")
        print(dict(counter))


if __name__ == "__main__":
    main()
