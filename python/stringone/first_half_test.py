"""

Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".


assert first_half('WooHoo')  ==  'Woo'
assert first_half('HelloThere')  ==  'Hello'
assert first_half('abcdef')  ==  'abc'
"""
"""
Solution
"""


def first_half(str):
    l = len(str)
    if l > 1:
        mid = l / 2
        return str[0:mid]
    return str


"""
Tests
"""


def test_exercise():
    assert first_half("WooHoo") == "Woo"
    assert first_half("HelloThere") == "Hello"
    assert first_half("abcdef") == "abc"


"""
"""