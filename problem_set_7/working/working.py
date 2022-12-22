import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if format := re.search(r"^(1[0-2]|[1-9]{1}):?([0-5]\d)? (PM|AM) to (1[0-2]|[1-9]{1}):?([0-5]\d)? (PM|AM)$", s):
        hr1 = int(format.group(1))
        if format.group(3) == "PM" and hr1 != 12:
            hr1 += 12
        elif format.group(3) == "AM" and hr1 == 12:
            hr1 = 0
        if format.group(2) is None:
            time1 = f"{hr1:02}:00"
        else:
            time1 = f"{hr1:02}:{format.group(2)}"
        hr2 = int(format.group(4))
        if format.group(6) == "PM" and hr2 != 12:
            hr2 += 12
        elif format.group(6) == "AM" and hr2 == 12:
            hr2 = 0
        if format.group(5) is None:
            time2 = f"{hr2:02}:00"
        else:
            time2 = f"{hr2:02}:{format.group(5)}"
        return f"{time1} to {time2}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()
