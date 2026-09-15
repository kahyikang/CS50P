while True:
    try:
        frac = input("Fraction: ")
        x, y = frac.split("/")
        x = int(x)
        y = int(y)

        if x > y or x < 0:
            continue

        fuel = round((x/y)*100)

    except (ValueError, ZeroDivisionError):
        pass

    else:
        if fuel <= 1:
            print("E")
        elif fuel >= 99:
            print("F")
        else:
            print(f"{fuel}%")

        break


