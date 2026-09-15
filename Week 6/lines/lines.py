import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

else:
    arg = sys.argv[1]

    if not arg.endswith(".py"):
        sys.exit("Not a Python file")

    count = 0
    try:
        with open(arg, "r") as file:
            for line in file:
                clean_line = line.lstrip()

                if not clean_line or clean_line.startswith("#"):
                    continue

                count += 1

    except FileNotFoundError:
        sys.exit("File does not exist")

    print(f"{count}")
