import os
from src.generators import filter_by_currency
from src.transactions_csv import get_transactions_csv
from src.transactions_excel import get_transactions_excel
from src.utils import get_transactions, transaction_amount_in_rub
from src.widget import mask_account_card, get_date
from src.processing import filter_by_state, sort_by_date
from src.search_operations import transactions_search
from src.counter import get_counter_operations_by_description

JSON_FILE_PATH = "../data/operations.json"
CSV_FILE_PATH = "../data/transactions.csv"
EXCEL_FILE_PATH = "../data/transactions_excel.xlsx"

os.makedirs("logs", exist_ok=True)


def main():
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
        print(f"Для обработки выбран JSON-файл.")
    elif user_input == "2":
        print(f"Загружаем данные из CSV файла: {CSV_FILE_PATH}")
        transactions = get_transactions_csv(CSV_FILE_PATH)
        print(f"Для обработки выбран CSV-файл.")
    elif user_input == "3":
        print(f"Загружаем данные из XLSX файла: {EXCEL_FILE_PATH}")
        transactions = get_transactions_excel(EXCEL_FILE_PATH)
        print(f"Для обработки выбран XLSX-файл.")
    else:
        print("Неверный выбор. Завершаю программу.")
        return

    if not transactions:
        print("Не удалось загрузить транзакции. Завершаю программу.")
        return

    while True:
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию. \n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
        ).upper()
        if status in ["EXECUTED", "CANCELED", "PENDING"]:
            filtered_transactions = filter_by_state(transactions, status)
            print(f"Операции отфильтрованы по статусу '{status}'")
            break
        else:
            print(f"Статус операции '{status}' недоступен.")

    user_input_sort = input("Отсортировать операции по дате? Да/Нет: ").lower()
    if user_input_sort == "да":
        user_input_sort_choice = input("Отсортировать по возрастанию или по убыванию? ").lower()
        reverse = True if user_input_sort_choice == "по убыванию" else False
        filtered_transactions = sort_by_date(filtered_transactions, reverse)

    user_input_currency_filter = input("Выводить только рублевые транзакции? Да/Нет: ").lower()
    if user_input_currency_filter == "да":
        filtered_transactions = filter_by_currency(filtered_transactions, "RUB")

    user_input_description_filter = input(
        "Отфильтровать список транзакций по определенному слову в описании? Да/Нет: "
    ).lower()
    if user_input_description_filter == "да":
        word = input("Введите слово для поиска: ")
        filtered_transactions = list(transactions_search(word, filtered_transactions))

    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
    else:
        filtered_transactions = list(filtered_transactions)
        print(f"\nВсего банковских операций в выборке: {len(filtered_transactions)}")
        for transaction in filtered_transactions:
            transaction_date = get_date(transaction["date"])  # Форматируем дату в нужный вид
            description = transaction["description"]
            amount_in_rub = transaction_amount_in_rub(filtered_transactions, transaction["id"])
            currency = transaction["currency"]

            print(f"{transaction_date} {description}")
            if "from" in transaction and "to" in transaction:
                print(f"{mask_account_card(transaction['from'])} -> {mask_account_card(transaction['to'])}")
            elif "from" in transaction:
                print(mask_account_card(transaction["from"]))
            elif "to" in transaction:
                print(mask_account_card(transaction["to"]))

            print(f"Сумма: {amount_in_rub} {currency}")
            print()

    user_input_operation_count = input("Хотите подсчитать количество операций определенного типа? Да/Нет: ").lower()
    if user_input_operation_count == "да":
        description_list = input("Введите типы операций через запятую: ").split(",")
        counter = get_counter_operations_by_description(filtered_transactions, description_list)
        print("Распечатываю итоговый список транзакций...:")
        print(dict(counter))


if __name__ == "__main__":
    main()
