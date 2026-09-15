from numb3rs import validate
import pytest

def test_valid():
    assert validate("127.0.0.0") == True

def test_invalid():
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("192.168.001.1") == False

def test_alpha():
    assert validate("cat") == False
