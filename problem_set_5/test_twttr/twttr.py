def main():
    x = input("Input: ")
    print(f"Output: {shorten(x)}")


def shorten(word):
    vl = ["a", "e", "i", "o", "u"]
    vu = ["A", "E", "I", "O", "U"]
    short = ""
    for char in word:
        if char not in vl and char not in vu:
            short += char
    return short


if __name__ == "__main__":
    main()
