def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if not s[0].isalpha() or not s[1].isalpha():
        return False

    first_number = True
    for chr in s:
        if not chr.isalnum():
            return False

        if chr.isdigit():
            if chr == "0" and first_number:
                return False
            first_number = False

        elif chr.isalpha and not first_number:
            return False

    return True



main()
