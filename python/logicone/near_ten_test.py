"""

Given a non-negative number "num", return True if num is within 2 of a multiple of 10. 
Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. 
"""
"""
Solution
"""


def near_ten(num):
    m = num % 10
    return m <= 2 or m >= 8


"""
Tests
"""


def test_exercise():

    assert near_ten(7) == False
    assert near_ten(8) == True
    assert near_ten(12) == True
    assert near_ten(13) == False
    assert near_ten(17) == False
    assert near_ten(19) == True
    assert near_ten(22) == True
    assert near_ten(23) == False
    assert near_ten(27) == False
    assert near_ten(29) == True


"""

"""