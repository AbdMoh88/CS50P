import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        q = int(input(f"{x} + {y} = "))
        ans = x + y
        if q == ans:
            score += 1
        else:
            print("EEE")
            i = 1
            while i <= 2:
                try:
                    q = int(input(f"{x} + {y} = "))
                    ans = x + y
                    if q == ans:
                        score += 1
                        break
                    elif q != ans and i == 2:
                        print("EEE")
                        print(f"{x} + {y} = {ans}")
                        i += 1
                        pass
                    else:
                        print("EEE")
                        i += 1
                        pass
                except ValueError:
                    print("EEE")
                    if i == 2:
                        print(f"{x} + {y} = {ans}")
                    i += 1
                    pass
            score += 0
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            l = int(input("Level: "))
            if 1 <= l <= 3:
                return l
                break
            else:
                pass
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        a = random.randint(0, 9)
    elif level == 2:
        a = random.randint(10, 99)
    else:
        a = random.randint(100, 999)
    return a


if __name__ == "__main__":
    main()
