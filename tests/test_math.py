import pytest


def add_two_numbers(a,b):
    return a + b
@pytest.mark.math
def test_small_Numbers():
    assert add_two_numbers(3,4) == 7 , "the sum of the two value should be 7"
@pytest.mark.math
def test_large_numbers():

    assert add_two_numbers(100,400) == 500 , "the sum sholl be 500"






