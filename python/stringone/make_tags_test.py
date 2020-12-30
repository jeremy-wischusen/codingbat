"""

The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. 
In this example, the "i" tag makes <i> and </i> which surround the word "Yay". 
Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".


make_tags('i', 'Yay') → '<i>Yay</i>'
make_tags('i', 'Hello') → '<i>Hello</i>'
make_tags('cite', 'Yay') → '<cite>Yay</cite>'
"""
"""
Solution
"""


def make_tags(tag, word):
    return "<{0}>{1}</{0}>".format(tag, word)


"""
Tests
"""


def test_exercise():
    assert make_tags("i", "Yay") == "<i>Yay</i>"
    assert make_tags("i", "Hello") == "<i>Hello</i>"
    assert make_tags("cite", "Yay") == "<cite>Yay</cite>"


"""

"""