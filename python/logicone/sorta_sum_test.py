"""
Given 2 ints, a and b, return their sum. 
However, sums in the range 10..19 inclusive, are forbidden, 
so in that case just return 20.
"""
"""
Solution
"""


def sorta_sum(a, b):
    s = a + b
    if s >= 10 and s <= 19:
        return 20
    return s


"""
Tests
"""


def test_exercise():
    assert sorta_sum(3, 4) == 7
    assert sorta_sum(9, 4) == 20
    assert sorta_sum(10, 11) == 21


"""
Our Solution:

def sorta_sum(a, b):
  sum = a + b
  if sum >= 10 and sum <= 19:
    return 20
  return sum

"""