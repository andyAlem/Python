import pytest

@pytest.fixture
def card_number_empty():
    return ""

@pytest.fixture
def card_nonstandard_cards():
    return [
        ("3434344444444444444433"),
        ("-44444444443rr"),
        ("3398"),
    ]