grocery = {}

while True:
    try:
        key = input().upper()
        if key in grocery:
            grocery[key] += 1
        else:
            grocery[key] = 1
    except EOFError:
        print()
        break


for key in sorted(grocery):
    print(grocery[key], key)
