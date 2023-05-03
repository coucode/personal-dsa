""" Longest Substring Without Repeating Characters
Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxCount = 0

        if len(s) == 0:
            return 0

        for left in range(len(s)):
            right = left + 1
            count = 0
            string = s[left]

            while right < len(s):
                if string.find(s[right]) == -1:
                    count += 1
                    string = string + s[right]
                    maxCount = max(count, maxCount)
                    right += 1
                else: 
                    break

        return maxCount + 1