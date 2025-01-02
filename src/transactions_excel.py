import logging
import os

import pandas as pd

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("transactions_excel")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "../logs", "transactions_excel.log"), mode="w"
)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transactions_excel(file_path):
    """Функция для работы с файлами excel"""

    if not os.path.isfile(file_path):
        logger.error(f"Excel файл '{file_path}' не найден.")
        raise FileNotFoundError(f"Excel файл '{file_path}' не найден.")

    if not file_path.endswith((".xls", ".xlsx")):
        logger.error("Неверный формат файла")
        raise ValueError("Неверный формат файла.")

    try:
        logger.info(f"Чтение транзакций Excel")
        df = pd.read_excel(file_path)

        if df.empty:
            logger.info(f"Файл пустой")
            raise ValueError("Excel файл пустой.")

        logger.info(f"Файл '{file_path}' успешно прочитан. Количество записей: {len(df)}")
        return df.to_dict(
            orient="records"
        )  # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html

    except ValueError as ex:
        logger.error(f"Ошибка в содержимом файла Excel: {ex}")
        raise ValueError(f"Файл Excel содержит некорректные данные. {ex}")
    except Exception as ex:
        logger.error(f"Ошибка в содержимом файла Excel: {ex}")
        raise ValueError(f"Ошибка при чтении Excel-файла: {ex}")


#if __name__ == "__main__":
#     excel_file = "/home/andrej/Poetry_homework/Homework_2.10-1_Git/data/transactions_excel.xlsx"
#
#     try:
#         transactions = get_transactions_excel(excel_file)
#         print("Транзакции из Excel-файла:")
#         for transaction in transactions:
#             print(transaction)
#     except Exception as e:
#         print(f"Ошибка: {e}")
