def main():
    while True:
        try:
            fraction = input("Fraction: ")
            per = convert(fraction)
            print(gauge(per))
            break
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    x = int(fraction.split("/")[0])
    y = int(fraction.split("/")[1])
    if x > y and y != 0:
        raise ValueError
    percentage = round((x / y)* 100)
    return percentage


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
