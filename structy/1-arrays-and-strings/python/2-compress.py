"""
Write a function, compress, that takes in a string as an argument.
The function should return a compressed version of the string where consecutive 
ccurrences of the same characters are compressed into the number of occurrences 
followed by the character. Single character occurrences should not be changed.

'aaa' compresses to '3a'
'cc' compresses to '2c'
't' should remain as 't'
You can assume that the input only contains alphabetic characters.
"""

"""
ASSUMPTIONS: 
- only contains alphabetic characters

EDGE CASES: 
- single character occurrences do not need to be changed

PATTERN: 
- Two Pointer

PSEUDOCODE:
1. Add a character to the end that is not alphabetic
2. Create left, right, answer variables
3. While the right pointer is less than the length of the string:
   3a. If left char equals right char, increment the right pointer
   3b. If not: 
       3b-1. find the count of the char by subtracting left from right pointer
       3b-2. if that count equals 1, add the character
       3b-3. if that count > 1, add the count and the character
       3b-4. Set the left pointer to the right pointer
4. return answer
"""

def compress(s):
  s += '!'
  left=right=0
  answer = ''

  while (right < len(s)):
    if (s[left] == s[right]):
      right += 1
    else:
      num = right - left
      if num != 1:
        answer = answer + str(num) + s[left]
      else: 
        answer = answer + s[left]
      left = right

  return answer