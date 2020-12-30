"""

Given 2 strings, a and b, return a string of the form short+long+short, 
with the shorter string on the outside and the longer string on the inside. 
The strings will not be the same length, but they may be empty (length 0).


combo_string('Hello', 'hi') → 'hiHellohi'
combo_string('hi', 'Hello') → 'hiHellohi'
combo_string('aaa', 'b') → 'baaab'
"""
"""
Solution
"""


def combo_string(a, b):
    len_a = len(a)
    len_b = len(b)
    if len_a > len_b:
        out = b
        mid = a
    else:
        out = a
        mid = b

    return "{0}{1}{0}".format(out, mid)


"""
Tests
"""


def test_exercise():
    assert combo_string("Hello", "hi") == "hiHellohi"
    assert combo_string("hi", "Hello") == "hiHellohi"
    assert combo_string("aaa", "b") == "baaab"


"""

"""