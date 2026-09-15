import re
import sys


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    if re.search(r"^<iframe (.+)></iframe>$", s):
        s = s[s.find("src=") + 5: s.find('"', s.find("src=") + 5)]

        if match := re.search(r"^https?://(?:www\.)?youtube\.com/embed/(.+)$", s):
            s = match.group(1)
            return "https://youtu.be/" + s

    return "None"


if __name__ == "__main__":
    main()
