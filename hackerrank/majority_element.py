"""
Majority Element - HackerRank 3/20/23

Given an array nums of size n, return the majority element. 
The majority element is the element that appears more than [n/2] times. 
You may assume that the majority element always exists in the array. 
"""

"""
Passing Solution
"""

def majorityElement(nums):
    dct = {}
    for num in nums:
        if num in dct:
            dct[num] += 1
        else: 
            dct[num] = 1
    return max(dct, key=dct.get)