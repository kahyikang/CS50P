grocery = {}

while True:
    try:
        x = input().strip().upper()

        if x in grocery:
            grocery[x] = grocery[x] + 1
        else:
            grocery[x] = 1

    except EOFError:
        print()
        break


for g in sorted(grocery):
    print(grocery[g], g)
