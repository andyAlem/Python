import csv
import os
import logging

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("transactions_csv")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "../logs", "transactions_csv.log"), mode="w"
)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

def get_transactions_csv(file_path):

    if not os.path.isfile(file_path):
        logger.error(f"CSV файл не найден: {file_path}")
        raise FileNotFoundError(f"CSV файл '{file_path}' не найден.")

    if not file_path.endswith('.csv'):
        logger.error("Неверный формат файла")
        raise ValueError("Неверный формат файла")

    try:
        transaction_list = []
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")

            if not reader.fieldnames:
                logger.error("CSV файл не содержит заголовков или пустой")
                raise ValueError("CSV файл не содержит заголовков или пустой")

            required_columns = {"id", "state", "date", "amount", "currency_name", "currency_code", "from", "to",
                                "description"}
            if not required_columns.issubset(reader.fieldnames):
                logger.error("CSV файл имеет некорректную структуру")
                raise ValueError("Некорректная структура CSV файла")
            for row in reader:
                transaction_list.append(row)

        if not transaction_list:
            logger.warning(f"CSV файл пустой")
            raise ValueError("CSV файл пустой.")

        logger.info(f"Успешно считано {len(transaction_list)} транзакций")
        return transaction_list

    except csv.Error as ex:
        logger.error(f"Ошибка при чтении CSV-файла: {ex}")
        raise ValueError(f"Ошибка при чтении CSV-файла: {ex}")
    except Exception as ex:
        logger.exception(f"Неизвестная ошибка при чтении CSV-файла")
        raise ValueError(f"Ошибка при чтении CSV-файла: {ex}")


#if __name__ == "__main__":
#    csv_file = "../data/transactions.csv"
#
#    try:
#        transactions = get_transactions_csv(csv_file)
#        print("Транзакции из CSV файла:")
#        for transaction in transactions:
#            print(transaction)
#    except Exception as e:
#         print(f"Ошибка: {e}")