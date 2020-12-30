"""
Given a string, return the count of the number of times that a substring length 2 appears in the string 
and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).


last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2
"""
"""
Solution
"""


def last2(str):
    l = len(str)

    count = 0
    start = 0
    strEnd = str[-2:]
    while start < l:
        i = str.find(strEnd, start)

        if i != -1:
            start = i + 1
            count += 1
        else:
            break
    return count - 1 if count > 0 else 0


"""
Tests
"""


def test_exercise():

    assert last2("hixxhi") == 1
    assert last2("xaxxaxaxx") == 1
    assert last2("axxxaaxx") == 2


"""
def last2(str):
  # Screen out too-short string case.
  if len(str) < 2:
    return 0
  
  # last 2 chars, can be written as str[-2:]
  last2 = str[len(str)-2:]
  count = 0
  
  # Check each substring length 2 starting at i
  for i in range(len(str)-2):
    sub = str[i:i+2]
    if sub == last2:
      count = count + 1

  return count
"""