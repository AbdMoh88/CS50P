import random

while True:
    try:
        l = int(input("Level: "))
        if l > 0:
            n = random.randint(1, l)
            g = int(input("Guess: "))
            if g > n:
                print("Too large!")
            elif g < n:
                print("Too small!")
            elif g == n:
                print("Just right!")
                break
        else:
            pass
    except ValueError:
        pass
