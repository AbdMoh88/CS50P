import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if ip := re.search(
        r"^((2[0-4]\d|25[0-5]|[0-1]?\d{1,2})\.){3}(2[0-4]\d|25[0-5]|[0-1]?\d{1,2}){1}$",
        ip,
    ):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
