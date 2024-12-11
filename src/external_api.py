import os

import requests
from dotenv import load_dotenv
from requests import RequestException

load_dotenv("../.env")
API_KEY = os.getenv("API_KEY")


def convert_to_rub(amount: float, currency: str):
    if currency not in {"USD", "EUR"}:
        raise ValueError("Валюта не поддерживается.")

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
        return "Конвертация невозможна"


if __name__ == "__main__":
    try:
        print(convert_to_rub(8221.37, "USD"))
    except Exception as e:
        print(f"Error: {e}")
