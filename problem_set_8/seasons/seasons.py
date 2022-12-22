from datetime import date
import sys
import re
import inflect


p = inflect.engine()


def main():
    date = input("Date of Birth: ")
    birthday = check_date(date)
    age = age_calc(birthday)
    print(age_words(age))


def check_date(d):
    if re.search(r"^\d{4}-[0-1]{1}\d{1}-[0-3]{1}\d{1}$", d):
        return d
    else:
        sys.exit("Invalid date")


def age_calc(birth):
    year, month, day = birth.split("-")
    age_days = date.today() - date(int(year), int(month), int(day))
    age_min = int(age_days.total_seconds() / 60)
    return age_min


def age_words(age):
    age_words = f"{p.number_to_words(age, andword='')} minutes"
    return age_words.capitalize()


if __name__ == "__main__":
    main()
