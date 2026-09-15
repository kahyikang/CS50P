# The Locked Lab

#### Video Demo: <YOUR VIDEO URL>

#### Description:

The Locked Lab is a terminal-based escape room program written in Python.
The player wakes up inside a fictional laboratory and must solve four
different security puzzles in order to escape.

The project was designed to demonstrate several programming concepts
covered in CS50's Introduction to Programming with Python, including
functions, loops, conditionals, exception handling, string manipulation,
randomization, and automated testing using pytest.

The game contains four puzzle stages.

The first puzzle is a Caesar cipher challenge. The player is shown an
encrypted word and must decode it using a provided shift value.

The second puzzle is a numerical sequence challenge. The program randomly
selects an arithmetic sequence and the player must determine the next
number.

The third puzzle asks the player to enter a randomly generated four-digit
security code based on clues displayed by the program.

The final puzzle presents a scrambled word. The player must rearrange the
letters to identify the correct password.

The program also tracks how many attempts the player requires to solve
all four puzzles. A final score is calculated based on the number of
incorrect attempts.

## Files

### project.py

This is the main program file. It contains the main function and all
functions required to run the escape room.

`caesar_decode` decodes Caesar cipher text.

`check_answer` compares user input with the expected answer while ignoring
capitalization and unnecessary spaces.

`next_sequence` calculates the next value of an arithmetic number sequence.

`calculate_score` calculates the player's final score according to the
total number of attempts.

The remaining puzzle functions control the individual escape room stages.

### test_project.py

This file contains automated tests for the main helper functions in
project.py.

The tests confirm that Caesar cipher decoding, answer checking, sequence
calculation, and score calculation work correctly.

### requirements.txt

The program uses only Python standard library modules, so no external
packages are required.

## Design Decisions

I chose to separate the puzzle logic from the user interaction where
possible. This makes the main logic easier to test using pytest.

Randomization was added so that users may receive different puzzles each
time the program is executed. However, the core functions remain
deterministic and can therefore be tested independently.

The score begins at 100. Four attempts represent a perfect game because
there are four puzzles. Every additional attempt reduces the final score
by 10 points, with a minimum score of zero.
