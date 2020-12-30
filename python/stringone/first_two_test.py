"""
Given a string, return the string made of its first two chars, so the String "Hello" yields "He". 
If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" 
yields the empty string "".


assert first_two('Hello')  ==  'He'
assert first_two('abcdefg')  ==  'ab'
assert first_two('ab')  ==  'ab'
"""
"""
Solution
"""


def first_two(str):
    return str[:2]


"""
Tests
"""


def test_exercise():
    assert first_two("Hello") == "He"
    assert first_two("abcdefg") == "ab"
    assert first_two("ab") == "ab"


"""
Our Solution:

def first_two(str):
  if len(str) >= 2:
    return str[:2]
  else:
    return str
"""