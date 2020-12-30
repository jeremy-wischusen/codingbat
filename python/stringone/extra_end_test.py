"""

Given a string, return a new string made of 3 copies of the last 2 chars of the original string. 
The string length will be at least 2.


extra_end('Hello') == 'lololo'
extra_end('ab') == 'ababab'
extra_end('Hi') == 'HiHiHi'
"""
"""
Solution
"""


def extra_end(str):
    e = str[-2:]
    return e + e + e


"""
Tests
"""


def test_exercise():
    assert extra_end("Hello") == "lololo"
    assert extra_end("ab") == "ababab"
    assert extra_end("Hi") == "HiHiHi"


"""
Our Solution:

def extra_end(str):
  end = str[-2:]
  return end + end + end
"""