from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("HELLO") == 0


def test_h():
    assert value("Hi") == 20
    assert value("hey") == 20


def test_other():
    assert value("what's up?") == 100
    assert value("Good Morning") == 100
