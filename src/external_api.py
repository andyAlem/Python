import os

import requests
from dotenv import load_dotenv
from requests import RequestException

load_dotenv('.env')
API_KEY = os.getenv('API_KEY')

def convert_to_rub(amount, currency):
    if currency not in {"EUR", "USD"}:
        raise ValueError("We could not convert EUR or USD")

    url = "https://api.apilayer.com/exchangerates_data/convert"
    params = {
        "to": "RUB",
        "from": currency,
        "amount": amount
    }
    headers = {"apikey": API_KEY}
    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        return data.get("result", 0.0)
    except RequestException as e:
        print(f"Request Error API: {e}")
        return 0.0
    except KeyError:
        print("KeyError API.")
        return 0.0

if __name__ == "__main__":
    print(convert_to_rub(100, "EUR"))