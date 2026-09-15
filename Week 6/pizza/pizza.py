import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

else:
    arg = sys.argv[1]

    if not arg.endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(arg) as file:
            reader = csv.DictReader(file)

            print(tabulate(reader, headers = "keys", tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")
