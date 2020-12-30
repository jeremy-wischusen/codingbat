"""

Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.


front3('Java') → 'JavJavJav'
front3('Chocolate') → 'ChoChoCho'
front3('abc') → 'abcabcabc'
"""
"""
Solution
"""


def front3(str):
    f = str[:3]
    return f + f + f


"""
Tests
"""


def test_exercise():
    assert front3("Java") == "JavJavJav"
    assert front3("Chocolate") == "ChoChoCho"
    assert front3("abc") == "abcabcabc"


"""

"""