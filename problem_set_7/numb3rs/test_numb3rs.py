from numb3rs import validate


def test_correct_ip():
    assert validate("192.168.1.1") == True
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True


def test_wrong_ip():
    assert validate("275.3.6.28") == False
    assert validate("256.1.192.3") == False
    assert validate("255.256.254.250") == False
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False


def test_txt():
    assert validate("cat") == False
    assert validate("1.2.3.cat") == False
