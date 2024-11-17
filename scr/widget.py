from masks import get_mask_account, get_mask_card_number


def mask_account_card(cards_accounts_data: str) -> str:
    """ Функция, которая умеет обрабатывать информацию как о картах, так и о счетах."""
    if cards_accounts_data.startswith("Счет" or "Счёт"):
        account_number = cards_accounts_data.split(maxsplit=1)[1]
        return f"Счет {get_mask_account(account_number)}"
    else:
        card_type, card_number = cards_accounts_data.rsplit(maxsplit=1)
        return f"{card_type} {get_mask_card_number(card_number)}"



