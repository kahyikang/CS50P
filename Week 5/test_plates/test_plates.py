from plates import is_valid

def test_correct():
    assert is_valid("AA123") == True

def test_num_in_middle():
    assert is_valid("AA12A") == False

def test_more_than_six_char():
    assert is_valid("AAA78945") == False

def test_less_than_two_char():
    assert is_valid("A") == False

def test_no_start_two_letter():
    assert is_valid("A945") == False

def test_first_num_zero():
    assert is_valid("AA012") == False

def test_punc_space():
    assert is_valid("AA,123") == False
    assert is_valid("AA 789") == False
