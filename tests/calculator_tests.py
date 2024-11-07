from main import get_area, get_hypotenuse

def test_get_hypotenuse_case_1():
    res = get_hypotenuse(3, 4)
    assert res == 5
def test_get_hypotenuse_case_2():
    res = get_hypotenuse(5, 12)
    assert res == 13


def test_get_hypotenuse_case_3():
    res = get_hypotenuse(8, 15)
    assert res ==  17
def test_get_area_case_1():
    res = get_area(3, 4)
    assert res ==  6
def test_get_area_case_2():
    res = get_area(5, 12)
    assert res == 30
def test_get_area_case_3():
    res = get_area(8, 15)
    assert res == 60
