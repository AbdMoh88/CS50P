from seasons import check_date, age_calc, age_words


def test_check_date():
    assert check_date("1988-01-02") == "1988-01-02"
    assert check_date("2022-09-10") == "2022-09-10"


def test_age_calc():
    assert age_calc("2022-09-10") == 1440
    assert age_calc("1988-01-02") == 18246240


def test_age_words():
    assert age_words(1440) == "One thousand, four hundred forty minutes"
    assert age_words(1) == "One minutes"
