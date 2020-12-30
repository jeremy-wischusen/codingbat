"""
Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating 
if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should ring. 
Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". 
Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".
"""
"""
Solution
"""


def alarm_clock(day, vacation):
    if vacation:
        wd = "10:00"
        we = "off"
    else:
        wd = "7:00"
        we = "10:00"
    if day == 0 or day == 6:
        return we
    return wd


"""
Tests
"""


def test_exercise():
    assert alarm_clock(1, False) == "7:00"
    assert alarm_clock(5, False) == "7:00"
    assert alarm_clock(0, False) == "10:00"


"""

"""