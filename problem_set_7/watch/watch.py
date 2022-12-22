import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if s := re.search(
        r"src=\"https?://(?:www\.)?youtube\.com/embed/(\w+?)\"",
        s,
    ):
        return f"https://youtu.be/{s.group(1)}"
    else:
        return "None"


if __name__ == "__main__":
    main()
