"""

Given a number n, return True if n is in the range 1..10, inclusive. 
Unless outside_mode is True, in which case return True if the number 
is less or equal to 1, or greater or equal to 10.
"""
"""
Solution
"""


def in1to10(n, outside_mode):
    if outside_mode:
        return n <= 1 or n >= 10
    return n >= 1 and n <= 10


"""
Tests
"""


def test_exercise():
    assert in1to10(5, False) == True
    assert in1to10(11, False) == False
    assert in1to10(11, True) == True


"""

"""