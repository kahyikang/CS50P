import re

name = input("What's your name? ").strip()

# := operator assigns a value from right to left and ask a boolean question at the same time
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")
