def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6 and s.isalpha() and s.isalnum():
        return True
    elif 2 <= len(s) <= 6 and s[0:2].isalpha() and s.isalnum():
        for char in s:
            if char.isdigit():
                x = s.index(char)
                if s[x] != "0" and s[x:6].isdigit():
                    return True
                else:
                    return False
    else:
        return False


if __name__ == "__main__":
    main()
