import pandas as pd
import os


def get_transactions_csv(file_path):

    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"CSV файл '{file_path}' не найден.")

    if not file_path.endswith(".csv"):
        raise ValueError("Неверный формат файла. Ожидается CSV.")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            df = pd.read_csv(file)

        if df.empty:
            raise ValueError("CSV файл пустой.")
        return df.to_dict(orient="records")

    except Exception as e:
        raise ValueError(f"Ошибка при чтении CSV-файла: {e}")
