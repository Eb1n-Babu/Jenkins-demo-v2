from app import add

def test_add_integers():
    assert add(2, 3) == 5

def test_add_floats():
    assert add(2.5, 3.1) == 5.6

def test_add_negative():
    assert add(-1, -2) == -3