from um import count
import pytest


def test_c1():
    assert count("um") == 1
    assert count("hello, UM, world!") == 1
    assert count("Um.") == 1
    assert count("uM?") == 1


def test_zero():
    assert count("yummy") == 0
    assert count("umum") == 0


def test_more():
    assert count("Um, thanks for the um album") == 2
    assert count("UM, Thanks, um..um...") == 3

