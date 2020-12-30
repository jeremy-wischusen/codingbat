"""

Given an int array length 2, return True if it contains a 2 or a 3.

has23([2, 5]) → True
has23([4, 3]) → True
has23([4, 5]) → False

"""
"""
Solution
"""


def has23(nums):
    look_for = [2, 3]
    return nums[0] in look_for or nums[1] in look_for


"""
Tests
"""


def test_exercise():
    assert has23([2, 5]) == True
    assert has23([4, 3]) == True
    assert has23([4, 5]) == False


"""

"""