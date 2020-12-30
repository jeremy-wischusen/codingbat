"""

Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".


hello_name('Bob') → 'Hello Bob!'
hello_name('Alice') → 'Hello Alice!'
hello_name('X') → 'Hello X!'

"""
"""
Solution
"""


def hello_name(name):
    return "Hello {}!".format(name)


"""
Tests
"""


def test_exercise():
    assert hello_name("Bob") == "Hello Bob!"
    assert hello_name("Alice") == "Hello Alice!"
    assert hello_name("X") == "Hello X!"


"""
Our Solution:

def hello_name(name):
  return "Hello " + name + "!"

"""