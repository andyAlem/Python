import csv
import os

def get_transaction_csv(file_path):

    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"CSV файл '{file_path}' не найден.")

    if not file_path.endswith('.csv'):
        raise ValueError("Неверный формат файла")

    try:
        transaction_list = []
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                transaction_list.append(row)

        if not transaction_list:
            raise ValueError("CSV файл пустой.")

        return transaction_list

    except csv.Error as ex:
        raise ValueError(f"Ошибка при чтении CSV-файла: {ex}")
    except Exception as ex:
        raise ValueError(f"Ошибка при чтении CSV-файла: {ex}")


if __name__ == "__main__":
    csv_file = "../data/transactions.csv"

    try:
        transactions = get_transaction_csv(csv_file)
        print("Транзакции из CSV файла:")
        for transaction in transactions:
            print(transaction)
    except Exception as e:
        print(f"Ошибка: {e}")