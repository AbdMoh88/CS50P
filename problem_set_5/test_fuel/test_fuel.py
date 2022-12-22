from fuel import convert, gauge
import pytest


def test_str_con():
    assert convert("1/4") == 25
    assert convert("1/5") == 20
    assert convert("2/10") == 20


def test_verror_con():
    with pytest.raises(ValueError):
        convert("cat/5")
        convert("1/dog")
        convert("5/2")


def test_zeroerror_con():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")


def test_int_gau():
    assert gauge(25) == "25%"


def test_verror_gau():
    with pytest.raises(TypeError):
        gauge("25")


def test_e_gau():
    assert gauge(1) == "E"


def test_f_gau():
    assert gauge(99) == "F"
