while True:
    try:
        fraction = input("Fraction: ")
        x = int(fraction.split("/")[0])
        y = int(fraction.split("/")[1])
        if x > y:
            x / 0
    except (ValueError, ZeroDivisionError):
        pass
    else:
        break

percentage = round((x / y) * 100)

if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")
