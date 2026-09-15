import random

while True:
    try:
        n = int(input("Level: "))

        if n <= 0:
            continue

    except ValueError:
        pass

    else:
        break

ans = random.randint(1, n)

while True:
    try:
        guess = int(input("Guess: "))

        if guess <= 0:
            continue

        if guess < ans:
            print("Too small!")

        elif guess > ans:
            print("Too large!")

        else:
            print("Just right!")
            break

    except ValueError:
        pass
