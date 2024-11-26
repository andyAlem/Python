from masks import get_mask_account, get_mask_card_number


def mask_account_card(cards_accounts_data: str) -> str:
    """Функция, которая умеет обрабатывать информацию как о картах, так и о счетах."""
    if cards_accounts_data.startswith("Счет" or "Счёт"):
        account_number = cards_accounts_data.split(maxsplit=1)[1]
        return f"Счет {get_mask_account(account_number)}"
    else:
        card_type, card_number = cards_accounts_data.rsplit(maxsplit=1)
        return f"{card_type} {get_mask_card_number(card_number)}"


def get_date(date: str) -> str:
    """Функция, которая изменяет дату в нужном формате"""

    return f"{(date[8:10])}.{(date[5:7])}.{(date[0:4])}"


if __name__ == "__main__":
    print(mask_account_card("Счет Platinum 73654108430135874305"))
    print(get_date("2024-03-11T02:26:18.671407"))
