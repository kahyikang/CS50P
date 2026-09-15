import random


def main():
    score = 0
    level = get_level()

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        corr_ans = x + y

        for i in range(3):
            try:
                ans = int(input(f"{x} + {y} = "))

                if ans != corr_ans:
                    print("EEE")
                    if i == 2:
                        print(f"{x} + {y} = {corr_ans}")
                else:
                    score += 1
                    break

            except ValueError:
                print("EEE")
                pass

    print(f"Score: {score}")

def get_level():
    while True:
        try:
            l = int(input("Level: "))
            if 1 <= l <= 3:
                return l

        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
