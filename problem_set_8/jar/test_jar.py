from jar import Jar


def test_init():
    jar = Jar(5)
    assert jar.capacity == 5
    assert jar.size == 0
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0


def test_str():
    jar = Jar(10)
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(1)
    assert str(jar) == "🍪🍪"
    jar.deposit(4)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(10)
    jar.deposit(2)
    assert jar.size == 2
    jar.deposit(5)
    assert jar.size == 7


def test_withdraw():
    jar = Jar(10)
    jar.deposit(10)
    jar.withdraw(2)
    assert jar.size == 8
    jar.withdraw(3)
    assert jar.size == 5
