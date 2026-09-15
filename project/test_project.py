import pytest
import project

from project import (
    caesar_decode,
    check_answer,
    next_sequence,
    calculate_score,
    count_correct_positions,
    toggle,
    all_powered,
    display_power,
    puzzle_cipher,
    puzzle_sequence,
    puzzle_security_code,
    puzzle_power_switch,
)


# --------------------------------------------------
# TEST CAESAR CIPHER
# --------------------------------------------------

def test_caesar_decode():
    assert caesar_decode("KHOOR", 3) == "HELLO"
    assert caesar_decode("VHFUHW", 3) == "SECRET"
    assert caesar_decode("GRRU", 3) == "DOOR"
    assert caesar_decode("ORFNHG", 3) == "LOCKED"


def test_caesar_decode_lowercase():
    assert caesar_decode("khoor", 3) == "hello"
    assert caesar_decode("def", 3) == "abc"


def test_caesar_decode_wraparound():
    assert caesar_decode("ABC", 3) == "XYZ"


def test_caesar_decode_symbols():
    assert caesar_decode("KHOOR!", 3) == "HELLO!"
    assert caesar_decode("KHOOR 123", 3) == "HELLO 123"


# --------------------------------------------------
# TEST ANSWER CHECKING
# --------------------------------------------------

def test_check_answer():
    assert check_answer("HELLO", "HELLO") is True
    assert check_answer("hello", "HELLO") is True
    assert check_answer("HeLLo", "HELLO") is True


def test_check_answer_spaces():
    assert check_answer("  HELLO  ", "HELLO") is True
    assert check_answer("hello", "  HELLO  ") is True


def test_check_answer_wrong():
    assert check_answer("WORLD", "HELLO") is False
    assert check_answer("DOOR", "LOCKED") is False


# --------------------------------------------------
# TEST NUMBER SEQUENCE
# --------------------------------------------------

def test_next_sequence():
    assert next_sequence([2, 4, 6, 8]) == 10
    assert next_sequence([5, 10, 15, 20]) == 25
    assert next_sequence([10, 20, 30, 40]) == 50


def test_next_sequence_negative_difference():
    assert next_sequence([10, 8, 6, 4]) == 2
    assert next_sequence([20, 15, 10, 5]) == 0


def test_next_sequence_same_numbers():
    assert next_sequence([5, 5, 5, 5]) == 5


def test_next_sequence_too_short():
    with pytest.raises(ValueError):
        next_sequence([5])


def test_next_sequence_not_arithmetic():
    with pytest.raises(ValueError):
        next_sequence([1, 2, 4, 8])


# --------------------------------------------------
# TEST SCORE CALCULATION
# --------------------------------------------------

def test_calculate_score_perfect():
    assert calculate_score(4) == 100


def test_calculate_score_mistakes():
    assert calculate_score(5) == 90
    assert calculate_score(6) == 80
    assert calculate_score(7) == 70
    assert calculate_score(8) == 60


def test_calculate_score_minimum():
    assert calculate_score(14) == 0
    assert calculate_score(20) == 0
    assert calculate_score(100) == 0


# --------------------------------------------------
# TEST SECURITY CODE
# --------------------------------------------------

def test_count_correct_positions():
    secret = "4578"

    assert count_correct_positions(secret, "4563") == 2
    assert count_correct_positions(secret, "8888") == 1
    assert count_correct_positions(secret, "5578") == 3
    assert count_correct_positions(secret, "4278") == 3


def test_count_correct_positions_all_correct():
    assert count_correct_positions("4578", "4578") == 4


def test_count_correct_positions_none_correct():
    assert count_correct_positions("4578", "0000") == 0


def test_count_correct_positions_some_correct():
    assert count_correct_positions("4578", "4000") == 1
    assert count_correct_positions("4578", "4500") == 2
    assert count_correct_positions("4578", "4570") == 3


# --------------------------------------------------
# TEST POWER SWITCH HELPERS
# --------------------------------------------------

def test_toggle():
    assert toggle(True) is False
    assert toggle(False) is True


def test_all_powered_true():
    state = {
        "A": True,
        "B": True,
        "C": True,
        "D": True
    }

    assert all_powered(state) is True


def test_all_powered_false():
    state = {
        "A": True,
        "B": False,
        "C": True,
        "D": True
    }

    assert all_powered(state) is False


def test_all_powered_all_off():
    state = {
        "A": False,
        "B": False,
        "C": False,
        "D": False
    }

    assert all_powered(state) is False


# --------------------------------------------------
# TEST DISPLAY POWER
# --------------------------------------------------

def test_display_power(capsys):
    state = {
        "A": True,
        "B": False,
        "C": True,
        "D": False
    }

    display_power(state)

    captured = capsys.readouterr()

    assert "A: ON" in captured.out
    assert "B: OFF" in captured.out
    assert "C: ON" in captured.out
    assert "D: OFF" in captured.out


# --------------------------------------------------
# TEST PUZZLE 1
# --------------------------------------------------

def test_puzzle_cipher_correct_first_try(monkeypatch):
    # Always select:
    # KHOOR -> HELLO
    monkeypatch.setattr(
        project.random,
        "choice",
        lambda choices: choices[0]
    )

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "HELLO"
    )

    assert puzzle_cipher() == 1


def test_puzzle_cipher_second_try(monkeypatch):
    monkeypatch.setattr(
        project.random,
        "choice",
        lambda choices: choices[0]
    )

    answers = iter([
        "WRONG",
        "HELLO"
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(answers)
    )

    assert puzzle_cipher() == 2


# --------------------------------------------------
# TEST PUZZLE 2
# --------------------------------------------------

def test_puzzle_sequence_correct_first_try(monkeypatch):
    # Always choose first puzzle:
    #
    # 2  3  8
    # 4  5  24
    # 6  7  ?
    #
    # answer = 48

    monkeypatch.setattr(
        project.random,
        "choice",
        lambda choices: choices[0]
    )

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "48"
    )

    assert puzzle_sequence() == 1


def test_puzzle_sequence_second_try(monkeypatch):
    monkeypatch.setattr(
        project.random,
        "choice",
        lambda choices: choices[0]
    )

    answers = iter([
        "40",
        "48"
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(answers)
    )

    assert puzzle_sequence() == 2


# --------------------------------------------------
# TEST PUZZLE 3
# --------------------------------------------------

def test_puzzle_security_code_correct(monkeypatch):
    monkeypatch.setattr(
        "builtins.input",
        lambda _: "4578"
    )

    assert puzzle_security_code() == 1


def test_puzzle_security_code_second_try(monkeypatch):
    answers = iter([
        "1234",
        "4578"
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(answers)
    )

    assert puzzle_security_code() == 2


def test_puzzle_security_code_invalid_input(monkeypatch):
    answers = iter([
        "12",
        "abcd",
        "4578"
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(answers)
    )

    # Invalid formats should not count as attempts
    assert puzzle_security_code() == 1


# --------------------------------------------------
# TEST PUZZLE 4
# --------------------------------------------------

def test_puzzle_power_switch_perfect(monkeypatch):
    # Correct solution:
    # B -> D -> A

    switches = iter([
        "B",
        "D",
        "A"
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(switches)
    )

    # Solved without reset = 1 attempt
    assert puzzle_power_switch() == 1


def test_puzzle_power_switch_invalid_input(monkeypatch):
    switches = iter([
        "X",   # invalid, should not count
        "B",
        "D",
        "A"
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(switches)
    )

    assert puzzle_power_switch() == 1


def test_puzzle_power_switch_after_reset(monkeypatch):
    # Press C five times.
    # This causes the system to reach the maximum
    # moves without solving, so it resets.
    #
    # Then solve using B -> D -> A.

    switches = iter([
        "C",
        "C",
        "C",
        "C",
        "C",
        "B",
        "D",
        "A"
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(switches)
    )

    # First round failed
    # Second round solved
    assert puzzle_power_switch() == 2
