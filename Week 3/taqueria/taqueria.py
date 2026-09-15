menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total = 0.00

while True:
    try:
        x = input("Item: ").strip().title()
        total += menu[x]

    except KeyError:
        pass

    except EOFError:
        print()
        break

    else:
        print(f"Total: ${total:.2f}")
