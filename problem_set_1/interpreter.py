x, y, z = input("Expression: ").strip().split(" ")

if y == ("+"):
    print(round(float(x) + float(z), 1))
if y == ("-"):
    print(round(float(x) - float(z), 1))
if y == ("*"):
    print(round(float(x) * float(z), 1))
if y == ("/"):
    print(round(float(x) / float(z), 1))
