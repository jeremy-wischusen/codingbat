"""
Given a string, return a new string where the first and last chars have been exchanged.


front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'
"""
"""
Solution
"""


def front_back(str):
    l = len(str)
    if l <= 1:
        return str
    return str[l - 1] + str[1:-1] + str[:1]


"""
Tests
"""


def test_exercise():
    assert front_back("code") == "eodc"
    assert front_back("a") == "a"
    assert front_back("ab") == "ba"


"""
Solution:
def front_back(str):
  if len(str) <= 1:
    return str
  
  mid = str[1:len(str)-1]  # can be written as str[1:-1]
  
  # last + mid + first
  return str[len(str)-1] + mid + str[0]
"""