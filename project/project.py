import random


def main():
    print("==========================================")
    print("           *  THE LOCKED LAB  *           ")
    print("==========================================")

    name = input("\nEnter your name: ").strip()

    print("\n..........................................")

    print(f"\nWelcome to my GAME! {name}...")
    print("You wake up inside a DARK laboratory...")
    print("The main door is LOCKED!")
    print("To escape...")
    print("You must solve FOUR security PUZZLES...")

    total_attempts = 0

    print("\n---------------------------------------")
    print("      PUZZLE 1: ENCRYPTED MESSAGE      ")
    print("---------------------------------------")
    attempts = puzzle_cipher()
    total_attempts += attempts

    print("\n---------------------------------------")
    print("        PUZZLE 2: LOGIC CIRCUIT        ")
    print("---------------------------------------")
    attempts = puzzle_sequence()
    total_attempts += attempts

    print("\n---------------------------------------")
    print("        PUZZLE 3: SECURITY CODE        ")
    print("---------------------------------------")
    attempts = puzzle_security_code()
    total_attempts += attempts

    print("\n---------------------------------------")
    print("        PUZZLE 4: POWER SWITCH         ")
    print("---------------------------------------")
    attempts = puzzle_power_switch()
    total_attempts += attempts


    score = calculate_score(total_attempts)

    print("\n==========================================")
    print("                 ESCAPED!                 ")
    print("==========================================")

    print(f"\nCongratulations!")
    print("You UNLOCKED the laboratory door.")

    print(f"\nTotal attempts: {total_attempts}")
    print(f"Final score     : {score}/100")

    if score >= 90:
        print("Rank         : Master Escape Artist 🏆")
    elif score >= 70:
        print("Rank         : Skilled Investigator 🔎")
    elif score >= 50:
        print("Rank         : Successful Survivor 🔓")
    else:
        print("Rank         : Lucky Escapee 😅")


def caesar_decode(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")

            decoded = chr(
                (ord(char) - base - shift) % 26 + base
            )

            result += decoded

        else:
            result += char

    return result


def check_answer(user_answer, correct_answer):
    return user_answer.strip().lower() == correct_answer.strip().lower()


def calculate_score(attempts):
    score = 100 - ((attempts - 4) * 10)

    if score < 0:
        return 0

    return score


def count_correct_positions(secret, guess):
    correct = 0

    for i in range(4):
        if secret[i] == guess[i]:
            correct += 1

    return correct


def toggle(value):
    return not value


def all_powered(state):
    return all(state.values())


def display_power(state):
    print("\nSYSTEM STATUS")

    for system in ["A", "B", "C", "D"]:
        status = "ON" if state[system] else "OFF"
        print(f"{system}: {status}")


def puzzle_cipher():
    messages = [
        ("KHOOR", 3, "HELLO"),
        ("VHFUHW", 3, "SECRET"),
        ("GRRU", 3, "DOOR"),
        ("ORFNHG", 3, "LOCKED")
    ]

    encrypted, shift, answer = random.choice(messages)

    print("\nA computer screen displays:")
    print(f"\n    {encrypted}")
    print(f"\nHint: Caesar cipher, shift = {shift}")

    attempts = 0

    while True:
        user = input("\nDecoded message: ")
        attempts += 1

        if check_answer(user, answer):
            print("\nCorrect! 🔓")
            print("Security Level 1 disabled.")
            return attempts

        print("Incorrect. Try again.")


def puzzle_sequence():
    puzzles = [
        {
            "grid": [
                "       2     3        8",
                "       4     5       24",
                "       6     7        ?"
            ],
            "answer": 48,
            "hint": "Try multiplying the first two numbers, then use the first number again."
        },

        {
            "grid": [
                "       2     3       13",
                "       4     5       41",
                "       6     7        ?"
            ],
            "answer": 85,
            "hint": "Think about the square of both numbers."
        },

        {
            "grid": [
                "       5     2       13",
                "       7     3       25",
                "       9     4        ?"
            ],
            "answer": 41,
            "hint": "Multiply the two numbers, then look at their difference."
        },

        {
            "grid": [
                "       3     4       14",
                "       5     6       22",
                "       7     8        ?"
            ],
            "answer": 30,
            "hint": "Add the first two numbers, then multiply the result."
        }
    ]

    puzzle = random.choice(puzzles)

    print("\nThe laboratory power system is OFFLINE.")
    print("To restore power, solve the missing value.")
    print("\nEach row follows the SAME hidden rule.\n")

    print("       A     B     OUTPUT")
    print("    ---------------------")

    for row in puzzle["grid"]:
        print(row)

    attempts = 0

    while True:
        user = input("\nMissing output: ").strip()
        attempts += 1

        try:
            user = int(user)

            if user == puzzle["answer"]:
                print("\nPOWER RESTORED! ⚡")
                print("Correct! 🔓")
                print("Security Level 2 disabled.")
                return attempts

        except ValueError:
            print("Please enter a number.")
            continue

        print("\nIncorrect.")

        if attempts == 2:
            print(f"💡 Hint: {puzzle['hint']}")
        else:
            print("Study the relationship between the rows.")


def puzzle_security_code():
    secret = "4578"

    clues = [
        ("4563", 2),
        ("8888", 1),
        ("5578", 3),
        ("4278", 3)
    ]

    print("\nThe security terminal requires a 4-digit access code.")
    print("You found several previous login attempts.")
    print()
    print("Each clue tells you how many digits are correct")
    print("AND in the correct position.")
    print()

    for guess, correct in clues:
        print(f"    {guess}  -->  {correct} correct")

    attempts = 0

    while True:
        user = input("\nEnter the 4-digit security code: ").strip()

        if not user.isdigit() or len(user) != 4:
            print("Please enter exactly 4 digits.")
            continue

        attempts += 1

        if user == secret:
            print("\nACCESS GRANTED! 🔓")
            print("Security Level 3 disabled.")
            return attempts

        correct = count_correct_positions(secret, user)

        print("\nACCESS DENIED.")
        print(f"Your attempt has {correct} correct digit(s) in the correct position.")


def puzzle_power_switch():
    state = {
        "A": False,
        "B": False,
        "C": False,
        "D": False
    }

    switch_effects = {
        "A": ["A", "B", "D"],
        "B": ["A", "C", "D"],
        "C": ["A", "B", "C"],
        "D": ["A", "D"]
    }

    print("\n⚠ LABORATORY POWER FAILURE ⚠")
    print("\nThe emergency generator is locked.")
    print("Four switches control four power circuits.")
    print("Each switch toggles several circuits.")

    print("\nOFF becomes ON.")
    print("ON becomes OFF.")

    print("\nYour goal: Turn ALL FOUR circuits ON.")

    print("\nSWITCH CONNECTIONS")
    print("------------------")
    print("Switch A --> A, B, D")
    print("Switch B --> A, C, D")
    print("Switch C --> A, B, C")
    print("Switch D --> A, D")

    # One complete round = one attempt
    attempts = 1

    moves_since_reset = 0
    max_moves = 5

    while True:
        display_power(state)

        print(f"\nMoves remaining: {max_moves - moves_since_reset}")

        choice = input(
            "Press switch A, B, C or D: "
        ).strip().upper()

        if choice not in switch_effects:
            print("\nInvalid switch. Choose A, B, C or D.")
            continue

        # Do NOT increase attempts here
        moves_since_reset += 1

        for system in switch_effects[choice]:
            state[system] = toggle(state[system])

        print(f"\nSwitch {choice} activated.")

        if all_powered(state):
            display_power(state)

            print("\nPOWER RESTORED! ⚡")
            print("Security Level 4 disabled.")

            return attempts

        if moves_since_reset == max_moves:
            print("\n🚨 SYSTEM OVERLOAD!")
            print("Too many switch operations.")
            print("The power system has reset.")

            # A new round means one more attempt
            attempts += 1

            state = {
                "A": False,
                "B": False,
                "C": False,
                "D": False
            }

            moves_since_reset = 0


if __name__ == "__main__":
    main()
