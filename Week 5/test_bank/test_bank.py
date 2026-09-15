from bank import value

def test_hello():
    assert value("hello") == 0

def test_halo():
    assert value("halo") == 20

def test_case():
    assert value("Wow, Man") == 100
    assert value("HEY") == 20
    assert value("HEllo") == 0

def test_num():
    assert value("1234") == 100
