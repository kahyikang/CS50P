from um import count

def test_normal():
    assert count("um") == 1

def test_in_word_um():
    assert count("lamums") == 0

def test_case_sensitive():
    assert count("UM um Um...") == 3

def test_sentence_um():
    assert count("Hi, um... um, thanks!") == 2

