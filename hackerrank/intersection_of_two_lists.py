"""
Intersection of two lists

Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays 
and you may return the result in any order. 

Example 1: 
Input: nums1 = [1, 2, 2, 1] nums2 = [2,2]
Output: [2,2]

Example 2: 
Input: nums1 = [4, 9, 5] nums2 = [9, 4, 9, 8, 4]
Output: [4, 9]
Explanation: [9, 4] is also accepted

Constraints: 
- 1 <= nums1.length, nums2.length <= 1000
- 0 <= nums1[i], nums2[i] <= 1000
"""

# Complete the 'intersect' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums1
#  2. INTEGER_ARRAY nums2
#

def intersect(nums1, nums2):
    # Write your code here
    nums1_table = {}
    nums2_table = {}
    answer = []
    
    for num in nums1:
        if num in nums1_table: 
            nums1_table[num] += 1
        else: 
            nums1_table[num] = 1

    for num in nums2: 
        if num in nums2_table: 
            nums2_table[num] += 1
        else:
            nums2_table[num] = 1
        
        if num in nums1_table:
            if nums2_table[num] <= nums1_table[num]:
                answer.append(num)
    return answer
    