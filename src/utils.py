import json
import logging
import os.path

from src.external_api import convert_to_rub

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "../logs", "utils.log"), mode="w"
)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transactions(path):
    """Принимает json и возвращает список"""
    try:
        logger.info("Получение списка данными о финансовых транзакциях")
        with open(path, "r", encoding="utf-8") as data_json:
            return json.load(data_json)
    except FileNotFoundError:
        logger.error("Ошибка файл не найден")
        return []
    except json.decoder.JSONDecodeError:
        logger.error("Ошибка обработки файла")
        return []
    except Exception as e:
        logger.error(f"Неизвестная ошибка {e}")
        return []


def transaction_amount_in_rub(transactions, transaction_id):
    """Выводит сумму транзакции"""
    logger.info("Начало работы функции")
    for transaction in transactions:
        if transaction.get("id") == transaction_id:
            operation_amount = transaction.get("operationAmount", {})
            amount = operation_amount.get("amount")
            currency = operation_amount.get("currency", {}).get("code")

            if not amount or not currency:
                logger.info(f"Некорректные данные {transaction_id}.")
                return "Ввод недействительный"

            if currency == "RUB":
                logger.info(f"Сумма транзакции {transaction_id} в рублях: {amount}.")
                return float(amount)
            else:
                try:
                    converted_amount = convert_to_rub(transaction)
                    logger.info(f"Сумма транзакции {transaction_id} в рублях после конвертации: {converted_amount}.")

                    if converted_amount == 0:
                        logger.info(f"Конвертация транзакции {transaction_id} невозможна.")
                        return "Конвертация невозможна"

                    return round(converted_amount, 2)
                except Exception as e:
                    logger.error(f"Ошибка конвертации транзакции {transaction_id}: {e}")
                    return "Конвертация невозможна"
    logger.error(f"Транзакция {transaction_id} не найдена.")
    return "Tранзакция не найдена"


# if __name__ == "__main__":
#     transactions = get_transactions("../data/operations.json")
#     print(transaction_amount_in_rub(transactions, 939719570))
