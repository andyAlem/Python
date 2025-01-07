import os

import requests
from dotenv import load_dotenv
from requests import RequestException

load_dotenv("../.env")
API_KEY = os.getenv("API_KEY")

# функция перестала работать, добавил логи, чтобы найти ошибку ...... 100 Запросов  месяц???


def convert_to_rub(transaction: dict):
    """Конвертация суммы из другой валюты в рубли."""
    operation_amount = transaction.get("operationAmount", {})
    amount = operation_amount.get("amount")
    currency = operation_amount.get("currency", {}).get("code")

    if not amount or not currency:
        raise ValueError("Неверные данные транзакции. Отсутствуют сумма или валюта.")

    if currency == "RUB":
        return float(amount)

    if currency in {"USD", "EUR"}:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        headers = {"apikey": API_KEY}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Поймает ошибки HTTP
            json_result = response.json()

            if "result" in json_result:
                return json_result["result"]
            else:
                return 0
        except RequestException as e:
            return 0
        except ValueError as e:
            logger.error(f"Ошибка при обработке данных API: {e}")
            return 0
        except KeyError as e:
            logger.error(f"Отсутствуют нужные данные в ответе API: {e}")
            return 0
    else:
        logger.warning(f"Конвертация для валюты {currency} не поддерживается.")
        return 0


# if __name__ == "__main__":
#     try:
#         transaction = {
#             "operationAmount": {"amount": "45.24", "currency": {"code": "USD"}}
#         }
#         result = convert_to_rub(transaction)
#         print(f"Сумма в рублях: {result}")
#     except Exception as e:
#         print(f"Error: {e}")
