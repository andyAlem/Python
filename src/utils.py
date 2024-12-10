import json
from json import JSONDecodeError
from src.external_api import convert_to_rub

def get_transactions(path):
    """Функция принимает на вход путь до JSON-файла
     и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        with open(path, encoding='utf-8') as f:
            try:
                data_json = json.load(f)
            except JSONDecodeError:
                print('Error decoding')
                return []
        return data_json
    except FileNotFoundError:
        print('File not found')
        return []


def transactions_amount_in_rub(transactions, transaction_id):

    for transaction in transactions:
        try:
            if transaction.get("id") == transaction_id:
                currency_code = transaction["operationAmount"]["currency"]["code"]
                amount = float(transaction["operationAmount"]["amount"])

                if currency_code == "RUB":
                    return amount
                else:
                    rub_amount = round(convert_to_rub(amount, currency_code), 2)
                    if rub_amount != 0:
                        return rub_amount
                    else:
                        return "Convert is not possible"
        except KeyError as e:
            return f"Key is missing {e}"
        except ValueError as e:
            return f"Error: Value is not correct {e}"

    return "Transaction not found"

if __name__ == "__main__":
    transactions = get_transactions("../data/operations.json")
    print(transactions_amount_in_rub(transactions, 811920303))