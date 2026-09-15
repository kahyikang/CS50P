from datetime import date
import sys
import re
import inflect


def main():
    birth_date = input("Date of Birth: ").strip()

    birthday = parse_date(birth_date)

    if birthday is None:
        sys.exit("Invalid date")

    minutes = calculate_minutes(birthday, date.today())

    print(convert_to_words(minutes))


def parse_date(date_string):
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date_string):
        return None

    try:
        return date.fromisoformat(date_string)
    except ValueError:
        return None


def calculate_minutes(birthday, today):
    difference = today - birthday

    return difference.days * 24 * 60


def convert_to_words(minutes):
    engine = inflect.engine()

    words = engine.number_to_words(minutes, andword="")

    return words.capitalize() + " minutes"


if __name__ == "__main__":
    main()
