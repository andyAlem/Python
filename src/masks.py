def get_mask_card_number(card_number: int) -> str:
    """
    Функция принимает номер карты и возвращает его маску в формате:
    XXXX XX** **** XXXX
    """
    card_number_str = str(card_number)

    masked_card = f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"
    return masked_card


def get_mask_account(account_number: int) -> str:
    """
    Функция принимает номер счета и возвращает его маску в формате:
    **XXXX
    """
    account_number_str = str(account_number)

    masked_account = f"**{account_number_str[-4:]}"
    return masked_account
