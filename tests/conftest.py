import pytest

@pytest.fixture
def card_number_empty():
    return ""

@pytest.fixture
def card_nonstandard_cards():
    return [
        ("-1502398039483094853496868705199"),
        ("-70734726758"),
        ("688"),
        ("89909"),
        ("599948426353"),
    ]