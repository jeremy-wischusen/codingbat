"""

The squirrels in Palo Alto spend most of the day playing. 
In particular, they play if the temperature is between 60 and 90 (inclusive). 
Unless it is summer, then the upper limit is 100 instead of 90. 
Given an int temperature and a boolean is_summer, 
return True if the squirrels play and False otherwise.


"""
"""
Solution
"""


def squirrel_play(temp, is_summer):
    if is_summer:
        u = 100
    else:
        u = 90
    return temp >= 60 and temp <= u


"""
Tests
"""


def test_exercise():
    assert squirrel_play(70, False) == True
    assert squirrel_play(95, False) == False
    assert squirrel_play(95, True) == True


"""

"""