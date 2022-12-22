import inflect

p = inflect.engine()

names = []

while True:
    try:
        n = input("name: ").title()
        names.append(n)
    except EOFError:
        print()
        break

print(f"Adieu, adieu, to {p.join(names)}")
