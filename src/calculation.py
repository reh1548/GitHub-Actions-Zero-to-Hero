# app.py
# This is a test commit
# Substract function and test added by Rehanul Ahmed
def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0

def test_substract():
    assert substract(1, 2) == -1
    assert substract(3, 2) = 1
