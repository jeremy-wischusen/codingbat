"""

Given a non-empty string like "Code" return a string like "CCoCodCode".


string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
"""
"""
Solution
"""


def string_splosion(str):
    l = len(str)
    e = l + 1
    s = ""
    if l > 0:
        for i in range(e):
            s += str[:i]
    return s


"""
Tests
"""


def test_exercise():
    assert string_splosion("Code") == "CCoCodCode"
    assert string_splosion("abc") == "aababc"
    assert string_splosion("ab") == "aab"


"""
Solution:
def string_splosion(str):
  result = ""
  # On each iteration, add the substring of the chars 0..i
  for i in range(len(str)):
    result = result + str[:i+1]
  return result
"""