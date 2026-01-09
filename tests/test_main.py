from app.main import multiplication, division

def test_multiplication():
    assert multiplication(2, 2) == 4

def test_division():
    assert division(10, 5) == 2

def test_fail_division():
    assert division(2, 0) == 0 
