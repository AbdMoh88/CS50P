def main():
    x = input("Greeting: ")
    print(f"${value(x)}")


def value(greeting):
    insen = greeting.strip().lower()
    if insen[0:5] == "hello":
        return 0
    elif insen[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
