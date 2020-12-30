"""

Given a string and a non-negative int n, return a larger string that is n copies of the original string.


string_times('Hi', 2) → 'HiHi'
string_times('Hi', 3) → 'HiHiHi'
string_times('Hi', 1) → 'Hi'
"""
"""
Solution
"""


def string_times(str, n):
    s = ""
    while n > 0:
        s += str
        n -= 1
    return s


"""
Tests
"""


def test_exercise():
    assert string_times("Hi", 2) == "HiHi"
    assert string_times("Hi", 3) == "HiHiHi"
    assert string_times("Hi", 1) == "Hi"
    assert string_times("Hi", 0) == ""


"""
Solution:
def string_times(str, n):
  result = ""
  for i in range(n):  # range(n) is [0, 1, 2, .... n-1]
    result = result + str  # could use += here
  return result
"""