"""

Given an array of ints, return True if the array is length 1 or more, 
and the first element and the last element are equal.


same_first_last([1, 2, 3]) → False
same_first_last([1, 2, 3, 1]) → True
same_first_last([1, 2, 1]) → True
"""
"""
Solution
"""


def same_first_last(nums):
    l = len(nums)
    if l < 1:
        return False
    return nums[0] == nums[-1]


"""
Tests
"""


def test_exercise():
    assert same_first_last([1, 2, 3]) == False
    assert same_first_last([1, 2, 3, 1]) == True
    assert same_first_last([1, 2, 1]) == True


"""
Our Solution:

def same_first_last(nums):
  return (len(nums) >= 1 and nums[0] == nums[-1])
"""