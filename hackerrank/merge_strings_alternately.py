"""
HackerRank 4/24/23
Merge Strings Alternately

You are given two strings word1 and word2. Merge the strins by adding 
letters in alternating order, starting with word1. If a string is longer than
the other, append the additional letters onto the end of the merged string. 

Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"

Example 2:
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"

Example 3:
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
"""
# Complete the 'merge_alt' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING word1
#  2. STRING word2
#

def merge_alt(word1, word2):
    min_len = 0
    word_rem = ''
    if len(word1) < len(word2):
        min_len = len(word1)
        word_rem = word2[min_len:]
    elif len(word2) < len(word1):
        min_len = len(word2)
        word_rem = word1[min_len:]
    else: 
        min_len = len(word1)
    answer = ''
    for i in range(min_len):
        answer = answer + word1[i] + word2[i]
    answer = answer + word_rem
    return answer