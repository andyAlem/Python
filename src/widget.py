from datetime import datetime

# from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(cards_accounts_data) -> str:
    """Функция для маскировки номера карты или счета"""
    if not cards_accounts_data:
        return "Данные отсутствуют"

    if not isinstance(cards_accounts_data, str):
        return "Данные в файле отсутствуют"

    try:
        cards_accounts_data = cards_accounts_data.replace("Счёт", "Счет")  # для теста и функционала
        card_type, card_number = cards_accounts_data.rsplit(maxsplit=1)

        if "Счет" in card_type or "Счёт" in card_type:
            masked_number = f"**{card_number[-4:]}"

        elif len(card_number) >= 8:
            masked_number = f"{card_number[:4]} ** **** {card_number[-4:]}"

        else:
            masked_number = card_number

        return f"{card_type} {masked_number}"
    except ValueError:
        return "Некорректные данные"


def get_date(date: str) -> str:
    """Функция для обработки формата времени"""
    try:
        if date.endswith("Z"):  # проверяем новый формат, иначе выдаст ошибку в main
            date_obj = datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
            return date_obj.strftime("%d.%m.%Y %H:%M:%S")

        date_obj = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
        return date_obj.strftime("%d.%m.%Y %H:%M:%S")

    except ValueError:
        try:
            date_obj = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")
            return date_obj.strftime("%d.%m.%Y %H:%M:%S")
        except ValueError:
            raise ValueError(f"Неверный формат даты. Проверьте ввод: {date}")
