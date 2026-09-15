from fuel import convert, gauge
import pytest

def test_convert_str():
    with pytest.raises(ValueError):
        convert("a/a")

def test_convert_float():
    with pytest.raises(ValueError):
        convert("2.2/4.4")

def test_convert_negative():
    with pytest.raises(ValueError):
        convert("-8/10")

def test_convert_divide_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_convert_valid():
    assert convert("1/2") == 50

def test_gauge_empty():
    assert gauge(1) == "E"

def test_gauge_percent():
    assert gauge(55) == "55%"

def test_gauge_full():
    assert gauge(99) == "F"
