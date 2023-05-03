/* Longest Substring Without Repeating Characters
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
*/
let lengthOfLongestSubstring = function(s) {
   let table = {}
   let maxCount = 0;
   if (s.length === 0) return 0

   for (let i = 0; i < s.length; i++){
       let count = 0;
       let str = s[i]
       for (let j = i + 1; j < s.length; j++){
           if (str.indexOf(s[j]) === -1){
               str = str + s[j]
               count++
               table[count] = str
               maxCount = Math.max(count, maxCount)
           } else {
               break
           }
       }
   }
   return maxCount + 1
};