"""

We have a loud talking parrot. 
The "hour" parameter is the current hour time in the range 0..23. 
We are in trouble if the parrot is talking and the hour is before 7 or after 20. 
Return True if we are in trouble.


parrot_trouble(True, 6) → True
parrot_trouble(True, 7) → False
parrot_trouble(False, 6) → False
"""

"""
Solution
"""


def parrot_trouble(talking, hour):
    return (talking) and (hour < 7 or hour > 20)


"""
Tests
"""


def test_exercise():
    assert parrot_trouble(True, 6) == True
    assert parrot_trouble(True, 7) == False
    assert parrot_trouble(False, 6) == False


"""
Solution:
def parrot_trouble(talking, hour):
  return (talking and (hour < 7 or hour > 20))
  # Need extra parenthesis around the or clause
  # since and binds more tightly than or.
  # and is like arithmetic *, or is like arithmetic +
"""