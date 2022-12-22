x = input("What's the answer to the Great Question of Life? ").strip().lower()

if x == "42":
    print("Yes")
elif x == "forty two":
    print("Yes")
elif x == "forty-two":
    print("Yes")
else:
    print("No")
