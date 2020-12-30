"""

The number 6 is a truly great number. Given two int values, a and b, 
return True if either one is 6. Or if their sum or difference is 6. 
Note: the function abs(num) computes the absolute value of a number.

"""
"""
Solution
"""


def love6(a, b):
    return a == 6 or b == 6 or sum([a, b]) == 6 or abs(a - b) == 6


"""
Tests
"""


def test_exercise():
    assert love6(6, 4) == True
    assert love6(4, 5) == False
    assert love6(1, 5) == True


"""

"""