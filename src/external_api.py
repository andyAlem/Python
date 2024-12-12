import os

import requests
from dotenv import load_dotenv
from requests import RequestException

load_dotenv("../.env")
API_KEY = os.getenv("API_KEY")


def convert_to_rub(transaction: dict):
    operation_amount = transaction.get("operationAmount", {})
    amount = operation_amount.get("amount")
    currency = operation_amount.get("currency", {}).get("code")

    if not amount or not currency:
        raise ValueError("Неверные данные транзакции. Отсутствуют сумма или валюта.")

    if currency not in {"USD", "EUR"}:
        raise ValueError(f"Валюта {currency} не поддерживается.")

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
    headers = {"apikey": API_KEY}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        json_result = response.json()

        if "result" in json_result:
            return json_result["result"]
        else:
            return 0
    except (RequestException, ValueError, KeyError):
        return 0


if __name__ == "__main__":
    try:
        print(convert_to_rub(8221.37, "USD"))
    except Exception as e:
        print(f"Error: {e}")
