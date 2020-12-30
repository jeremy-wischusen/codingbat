"""

Given two strings, a and b, return the result of putting them together in the order abba, 
e.g. "Hi" and "Bye" returns "HiByeByeHi".


make_abba('Hi', 'Bye') → 'HiByeByeHi'
make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
make_abba('What', 'Up') → 'WhatUpUpWhat'
"""
"""
Solution
"""


def make_abba(a, b):
    return "{}{}{}{}".format(a, b, b, a)


"""
Tests
"""


def test_exercise():
    assert make_abba("Hi", "Bye") == "HiByeByeHi"
    assert make_abba("Yo", "Alice") == "YoAliceAliceYo"
    assert make_abba("What", "Up") == "WhatUpUpWhat"


"""
Our Solution:

def make_abba(a, b):
  return a + b + b + a
"""