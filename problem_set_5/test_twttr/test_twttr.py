from twttr import shorten


def test_lower():
    assert shorten("twetter") == "twttr"


def test_upper():
    assert shorten("TWETTER") == "TWTTR"


def test_num():
    assert shorten("CS50") == "CS50"


def test_pun():
    assert shorten(".,-_") == ".,-_"
