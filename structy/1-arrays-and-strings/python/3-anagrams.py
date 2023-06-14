"""
anagrams
Write a function, anagrams, that takes in two strings as arguments. The function should return a boolean indicating whether or not the strings are anagrams. Anagrams are strings that contain the same characters, but in any order.

anagrams('restful', 'fluster') # -> True
anagrams('cats', 'tocs') # -> False
anagrams('monkeyswrite', 'newyorktimes') # -> True
anagrams('paper', 'reapa') # -> False
anagrams('elbow', 'below') # -> True
anagrams('tax', 'taxi') # -> False
anagrams('taxi', 'tax') # -> False
anagrams('night', 'thing') # -> True
anagrams('abbc', 'aabc') # -> False
anagrams('po', 'popp') # -> false
anagrams('pp', 'oo') # -> false

"""

def anagrams(s1, s2):
  count = dict()
  
  for char in s1:
    if count.get(char) is None:
      count[char] = 1
    else: 
      count[char] += 1
  
  for char2 in s2:
    if count.get(char2) is None:
      return False
    else:
      count[char2] -= 1
  
  for char3 in count:
    if count[char3] != 0:
      return False
  return True
