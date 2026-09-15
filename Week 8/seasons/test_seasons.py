from datetime import date
from seasons import parse_date, calculate_minutes, convert_to_words


def test_parse_date_valid():
    assert parse_date("2026-12-31") == date(2026, 12, 31)


def test_invalid_date_format():
    assert parse_date("January 1, 2000") is None
    assert parse_date("01-01-2000") is None
    assert parse_date("2000/01/01") is None
    assert parse_date("abc") is None


def test_invalid_date():
    assert parse_date("2000-02-30") is None
    assert parse_date("2000-13-01") is None
    assert parse_date("2000-00-01") is None
    assert parse_date("2023-02-29") is None


def test_calculate_minutes_one_day():
    birthday = date(1999, 12, 31)
    today = date(2000, 1, 1)
    assert calculate_minutes(birthday, today) == 1440


def test_calculate_minutes_one_year():
    birthday = date(1999, 1, 1)
    today = date(2000, 1, 1)
    assert calculate_minutes(birthday, today) == 525600


def test_calculate_minutes_leap_year():
    birthday = date(2000, 1, 1)
    today = date(2001, 1, 1)
    assert calculate_minutes(birthday, today) == 527040


def test_convert_to_words():
    assert convert_to_words(1440) == "One thousand, four hundred forty minutes"
    assert convert_to_words(525600) == "Five hundred twenty-five thousand, six hundred minutes"
