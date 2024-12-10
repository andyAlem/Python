import json
import os

import requests
from dotenv import load_dotenv


def convert_to_rub(amount, currency):
    if currency not in {"EUR", "USD"}:
        raise ValueError("We could convert EUR or USD")

    import requests

    url = "https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from}&amount={amount}"
    payload = {}
    headers = {
        "apikey": "tEM2t7kwdp4hMJ3gZLmrUe69NSXRMSKi"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    result = response.text