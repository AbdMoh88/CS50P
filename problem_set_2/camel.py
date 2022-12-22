x = input("camelCase: ")
print("snake_case: ", end="")
for alpha in x:
    if alpha.isupper():
        print(f"_{alpha.lower()}", end="")
    else:
        print(alpha, end="")
print()

