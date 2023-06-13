"""
Write a function, uncompress, that takes in a string as an argument. 
The input string will be formatted into multiple groups according to the following pattern:

<number><char>

for example, '2c' or '3a'.
The function should return an uncompressed version of the string where each 'char' of a group 
is repeated 'number' times consecutively. You may assume that the input string is well-formed 
according to the previously mentioned pattern.

uncompress("2c3a1t"); // -> 'ccaaat'
uncompress("4s2b"); // -> 'ssssbb'
uncompress("2p1o5p"); // -> 'ppoppppp'
uncompress("3n12e2z"); // -> 'nnneeeeeeeeeeeezz'
uncompress("127y"); // ->'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
"""
import math
def uncompress(s):
  left = 0
  right = 0
  answer = ''
  
  while (right < len(s)):
    try:
      charCheck = int(s[right])
      right +=1
    except:
      num = int(s[left:right])
      for x in range(num):
        answer = answer + s[right]
      left = right + 1
      right = right + 1
  
  return answer