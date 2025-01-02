from src.masks import get_mask_account, get_mask_card_number
from datetime import datetime


def mask_account_card(cards_accounts_data: str) -> str:
    """Функция, которая умеет обрабатывать информацию как о картах, так и о счетах."""
    if cards_accounts_data.startswith(("Счет", "Счёт")):
        account_number = cards_accounts_data.split(maxsplit=1)[1]
        return f"Счет {get_mask_account(account_number)}"
    else:
        card_type, card_number = cards_accounts_data.rsplit(maxsplit=1)
        return f"{card_type} {get_mask_card_number(card_number)}"



def get_date(date: str) -> str:
    """Функция для обработки формата времени"""
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
        return date_obj.strftime("%Y-%m-%d %H:%M:%S")
    except ValueError:
        try:
            date_obj = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")
            return date_obj.strftime("%Y-%m-%d %H:%M:%S")
        except ValueError:
            raise ValueError(f"Неверный ввод, проверьте количество символов. Получено: {date}")


