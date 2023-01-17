import pytest

def f():
    return 3

@pytest.mark.great
def test_f(input_val):
    assert f() == 2 * input_val

@pytest.mark.great
def test_r(input_val):
    assert f() == 3 * input_val

@pytest.mark.others
def test_h():
    assert f()*2 == 9

@pytest.mark.parametrize('a,b', [(0,0), (1,2)])
def test_personal(a,b):
    assert a==b