from project import check_city, check_month, check_day


def test_check_city():
    assert check_city("Chicago") == "Chicago"
    assert check_city("New York") == "New York"
    assert check_city("New") == False
    assert check_city("Texas") == False


def test_check_month():
    assert check_month("January") == "January"
    assert check_month("Jan") == "January"
    assert check_month("Jam") == False
    assert check_month("All") == "All"


def test_check_day():
    assert check_day("Monday") == "Monday"
    assert check_day("Wed") == "Wednesday"
    assert check_day("All") == "All"
    assert check_day("Son") == False

