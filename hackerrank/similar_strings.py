"""
Similar Strings

Two strings are said to be similar if they are composed of the same characters. 
For example: "abaca" and "cba" are similar isnce both of them are composed of characters a, b, and c
However "abaca" and "bcd" are not similar since they do nto share all of the same letters

Given an array of strings words of length n, find the number of pairs of strings that are similar

Note: 
- each string is composed of lowercase english characters only
- pairs are considered index-wise, i.e. two equal strings at different indices are counted as separate pairs
- a pair at indices (i, j) is the same as the pair at (j, i)

Constraints: 
- 1 <= n <= 10^5
- The sum of the lengths of all strings does not exceed 10^6
- All string sconsist of lowecase English characters only

Sample: 
['aba', 'abaca', 'baab', 'cba'] - expected output 2


"""

def countSimilarPairs(words):
    char_set = [sorted(set(item)) for item in words]
    pairs = []    
    
    for i in range(len(char_set)):
        current = char_set[i]
        for j in range(len(char_set)):
            check = char_set[j]
            if j != i: 
                if current == check:
                    pair = [i, j]
                    pair.sort()
                    if pair not in pairs:
                        pairs.append(pair)
    return len(pairs)
    