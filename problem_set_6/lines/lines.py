import sys

if len(sys.argv) == 2 and sys.argv[1].endswith(".py"):
    fileName = sys.argv[1]
    try:
        with open(fileName) as file:
            lines = 0
            for line in file:
                if line.lstrip().startswith("#"):
                    lines = lines
                elif line.strip():
                    lines += 1
            print(lines)
    except FileNotFoundError:
        sys.exit("File does not exist")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    sys.exit("Not a Python file")
