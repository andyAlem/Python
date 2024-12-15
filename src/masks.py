import logging
import os.path

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "../logs", "masks.log"), mode="w"
)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: int) -> str:
    """
    Функция принимает номер карты и возвращает его маску в формате:
    XXXX XX** **** XXXX
    """
    try:
        card_number_str = str(card_number)
        masked_card = f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"
        logger.info(f"Номер карты после маскирования: {masked_card}")
        return masked_card
    except Exception as ex:
        logger.error(f"Ошибка при маскировании номера карты {card_number}: {ex}")
        return


def get_mask_account(account_number: int) -> str:
    """
    Функция принимает номер счета и возвращает его маску в формате:
    **XXXX
    """
    try:
        account_number_str = str(account_number)
        masked_account = f"**{account_number_str[-4:]}"
        logger.info(f"Маскированный номер счёта: {masked_account}")
        return masked_account
    except Exception as ex:
        logger.error(f"Ошибка при маскировании номера счёта {account_number}: {ex}")
        return ""


# if __name__ == "__main__":
#     print(get_mask_card_number(899898988456))
#     print(get_mask_account(6669932141487952))
