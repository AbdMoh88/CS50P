from working import convert
import pytest


def test_normal():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:00 PM to 5:00 AM") == "21:00 to 05:00"
    assert convert("9 PM to 5 AM") == "21:00 to 05:00"
    assert convert("12 AM to 5 AM") == "00:00 to 05:00"
    assert convert("12:00 AM to 5:00 AM") == "00:00 to 05:00"
    assert convert("12 PM to 9 PM") == "12:00 to 21:00"
    assert convert("12:05 PM to 9:00 PM") == "12:05 to 21:00"



def test_minutes():
    assert convert("9:25 PM to 5:30 AM") == "21:25 to 05:30"
    assert convert("9:25 AM to 5:30 PM") == "09:25 to 17:30"


def test_valerr():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9AM to 8PM")
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 17:00 PM")

