import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

else:
    before = sys.argv[1]
    after = sys.argv[2]

    if not before.endswith(".csv") or not after.endswith(".csv"):
        sys.exit("Not a CSV file")

    rows = []
    try:
        with open(before) as file:
            reader = csv.DictReader(file)
            for row in reader:
                rows.append(row)

    except FileNotFoundError:
        sys.exit("File does not exist")

    with open(after, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in rows:
            last, first = row["name"].split(", ")
            house = row["house"]
            writer.writerow({"first": first, "last": last, "house": house})
