from plates import is_valid


def test_len():
    assert is_valid("Hello") == True
    assert is_valid("H") == False
    assert is_valid("HelloCS") == False


def test_first_two():
    assert is_valid("CS50") == True
    assert is_valid("50CS") == False
    assert is_valid("C2022") == False


def test_num():
    assert is_valid("CS50") == True
    assert is_valid("CS50P") == False
    assert is_valid("CS05") == False


def test_spec_char():
    assert is_valid("CS,50") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS.50") == False
