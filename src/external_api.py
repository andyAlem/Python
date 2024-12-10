import os

import requests
from dotenv import load_dotenv
from requests import RequestException

load_dotenv(".env")
API_KEY = os.getenv("API_KEY")


def convert_to_rub(amount, currency):
    """Функцию конвертации в рубли"""
    if currency not in {"EUR", "USD"}:
        raise ValueError("We could convert only EUR or USD")

    url = "https://api.apilayer.com/exchangerates_data/convert"
    params = {"to": "RUB", "from": currency, "amount": amount}
    headers = {"apikey": API_KEY}
    try:
        response = requests.get(url, headers=headers, params=params)
        result = response.json()
        return result.get("result", 0.0) #float
    except RequestException:
        return 0


#if __name__ == "__main__":
#    print(convert_to_rub(100, "EUR"))
