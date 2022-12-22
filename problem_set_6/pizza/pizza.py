import sys
from tabulate import tabulate
import csv


if len(sys.argv) == 2 and sys.argv[1].endswith(".csv"):
    fileName = sys.argv[1]
    try:
        with open(fileName) as file:
            table = csv.DictReader(file)
            print(tabulate(table, headers="keys", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    sys.exit("Not a CSV file")
