x = input("Input: ")

print("Output: ", end="")

for vowel in x:
    lower = ("aeiou")
    upper = ("AEIOU")
    if vowel in (lower):
        print("", end="")
    elif vowel in (upper):
        print("", end="")
    else:
        print(vowel, end="")

print()
