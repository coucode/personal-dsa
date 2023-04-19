"""
Given a list of s of strings, return true if all strings in s are anagrams of
each other, and false otherwise. 
An Anagram is a word or phrase formed by rearranning the letters of a different
word or phrase, typically using all the original letters exactly once. 

Example 1: 
Input: s = ["anagram", "nagaram"]
Output: True

Example 2: 
Input: s = ["rat", "car"]
Output: False

Example 3: 
Input: s = ["cat"]
Output: True

Constraints: 
1 <= s.length <=5 * 10^4
strings in s consist of lowercase english letters
"""
# Complete the 'is_anagrams' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING_ARRAY s as parameter.
#

def is_anagrams(s):
    # Write your code here
    s_sort = sorted(s[0])
    for word in s:
        word_sort = sorted(word)
        if s_sort != word_sort:
            return False
    return True