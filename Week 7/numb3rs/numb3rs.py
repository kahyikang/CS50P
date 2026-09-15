import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    range = r"([1-9]?[0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])"
    if re.search(rf"^{range}\.{range}\.{range}\.{range}$", ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
