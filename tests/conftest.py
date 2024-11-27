import pytest

@pytest.fixture
def card_number_empty():
    return ""

@pytest.fixture
def nonstandard_cards():
    return [
        ("3434344444444444444433"),
        ("-44444444443rr"),
        ("3398"),
    ]

@pytest.fixture
def mask_account():
    return  [
        ("64686473678894779589", "**9589"),
        ("35383033474447895560", "**5560"),
        ("73654108430135874305", "**4305"),
    ]

@pytest.fixture
def mask_account_empty():
    return ""

@pytest.fixture
def nonstandard_accounts():
    return  [
        ("888888888888888888888888888333232"),
        ("9999999"),
        ("12325"),
        ("1"),
        ("0"),
    ],