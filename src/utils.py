import json

from src.external_api import convert_to_rub


def get_transactions(path):
    try:
        with open(path, "r", encoding="utf-8") as data_json:
            return json.load(data_json)
    except FileNotFoundError:
        return []
    except json.decoder.JSONDecodeError:
        return []
    except Exception as e:
        print(f"Неизвестная ошибка {e}")
        return []


def transaction_amount_in_rub(
    transactions, transaction_id
):  # https://sky.pro/media/ispolzovanie-dict-getkey-vmesto-dictkey-v-python/

    for transaction in transactions:
        if transaction.get("id") == transaction_id:
            operation_amount = transaction.get("operationAmount", {})
            amount = operation_amount.get("amount")
            currency = operation_amount.get("currency", {}).get("code")

            if not amount or not currency:
                return "Ввод недействительный"

            if currency == "RUB":
                return float(amount)
            else:
                try:
                    converted_amount = convert_to_rub(float(amount), currency)
                    print(f"Converted amount: {converted_amount}")

                    if converted_amount == 0:
                        return "Конвертация невозможна"
                except Exception as e:
                    print(f"Ошибка конвертации: {e}")
                    return round(converted_amount, 2)
    return "Tранзакция не найдена"


if __name__ == "__main__":
    transactions = get_transactions("../data/operations.json")
    print(transaction_amount_in_rub(transactions, 441945886))
