total = 0

while True:
    print("Amount Due:", 50 - total)
    insert = int(input("Insert Coin: "))
    if insert == 25 or insert == 10 or insert == 5:
        total += insert

    if total >= 50:
        print("Change Owed:", total - 50)
        break
