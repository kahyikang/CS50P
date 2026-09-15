from twttr import shorten
import pytest

def test_no_placement():
    assert shorten("qplm") == "qplm"

def test_lower_case():
    assert shorten("how are you?") == "hw r y?"

def test_upper_case():
    assert shorten("BYEBYE") == "BYBY"

def test_title_case():
    assert shorten("Hello") == "Hll"

def test_num():
    assert shorten("123") == "123"

def test_punc():
    assert shorten("^*(#@$&())") == "^*(#@$&())"

def test_no_word():
    with pytest.raises(TypeError):
        shorten()
