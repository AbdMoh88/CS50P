import sys
import csv


if len(sys.argv) == 3 and sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
    before = sys.argv[1]
    after = sys.argv[2]
    try:
        with open(after, "w") as first_last:
            with open(before) as name:
                writer = csv.DictWriter(
                    first_last, fieldnames=["first", "last", "house"]
                )
                writer.writeheader()
                for row in csv.DictReader(name):
                    last, first = row["name"].split(", ")
                    house = row["house"]
                    writer.writerow({"first": first, "last": last, "house": house})
    except FileNotFoundError:
        sys.exit("File does not exist")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    sys.exit("Not a CSV file")
