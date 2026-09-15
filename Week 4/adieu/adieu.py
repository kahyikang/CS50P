import inflect
p = inflect.engine()

name_list = []

while True:
    try:
        name_list.append(input("Name: "))

    except EOFError:
        print()
        break

print("Adieu, adieu, to " + p.join(name_list))

