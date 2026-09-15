camel = input("camelCase: ").strip()
snake = ""

for c in camel:
    if c.isupper():
        snake += "_" + c.lower()
    else:
        snake += c.lower()

print(snake)
