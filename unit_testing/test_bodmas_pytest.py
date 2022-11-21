import bodmas


def test_addtion():
    assert bodmas.addtion(3,1) == 4
    assert bodmas.addtion(3, 2) == 5
    assert bodmas.addtion(3, 3) == 6

def test_subtraction():
    assert bodmas.subtraction(3, 1) == 2

def test_multiplication():
    assert bodmas.multiplication (3, 1) == 3



