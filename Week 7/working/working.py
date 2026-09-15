import re
import sys


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    pattern = r"(0?[1-9]|1[0-2])(?::[0-5][0-9])? (AM|PM)"
    if not re.search(rf"^{pattern} to {pattern}$", s):
        raise ValueError("time format no match")

    start, end = [x.upper() for x in s.split(" to ")]
    return f"{convertion(start)} to {convertion(end)}"


def convertion(s):
    time, apM = s.split()
    if ":" in time:
        hrs, min = [int(x) for x in time.split(":")]

    else:
        hrs = int(time)
        min = 0

    hrs = convert_hrs(hrs,apM)
    return f"{hrs:02}:{min:02}"


def convert_hrs(hrs,apM):
    if apM == "AM" and hrs == 12:
        return 0
    elif apM == "PM" and hrs != 12:
        return hrs+12
    else:
        return hrs


if __name__ == "__main__":
    main()
