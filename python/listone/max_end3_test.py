"""

Given an array of ints length 3, figure out which is larger, 
the first or last element in the array, and set all the other 
elements to be that value. Return the changed array.


max_end3([1, 2, 3]) → [3, 3, 3]
max_end3([11, 5, 9]) → [11, 11, 11]
max_end3([2, 11, 3]) → [3, 3, 3]
"""
"""
Solution
"""


def max_end3(nums):
    f = nums[0]
    l = nums[-1]
    if f > l:
        v = f
    else:
        v = l
    return [v, v, v]


"""
Tests
"""


def test_exercise():
    assert max_end3([1, 2, 3]) == [3, 3, 3]
    assert max_end3([11, 5, 9]) == [11, 11, 11]
    assert max_end3([2, 11, 3]) == [3, 3, 3]


"""
Our Solution:

def max_end3(nums):
  big = max(nums[0], nums[2])
  nums[0] = big
  nums[1] = big
  nums[2] = big
  return nums

"""