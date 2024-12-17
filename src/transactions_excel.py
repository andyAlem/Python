import os
import pandas as pd


def get_transactions_excel(file_path):

    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Excel файл '{file_path}' не найден.")

    if not file_path.endswith(('.xls', '.xlsx')):
        raise ValueError("Неверный формат файла.")

    try:
        df = pd.read_excel(file_path)

        if df.empty:
            raise ValueError("Excel файл пустой.")

        return df.to_dict(orient='records')

    except ValueError as ex:
        raise ValueError(f"Файл Excel содержит некорректные данные. {ex}")
    except Exception as ex:
        raise ValueError(f"Ошибка при чтении Excel-файла: {ex}")


# if __name__ == "__main__":
#     excel_file = "/home/andrej/Poetry_homework/Homework_2.10-1_Git/data/transactions_excel.xlsx"
#
#     try:
#         transactions = get_transactions_excel(excel_file)
#         print("Транзакции из Excel-файла:")
#         for transaction in transactions:
#             print(transaction)
#     except Exception as e:
#         print(f"Ошибка: {e}")