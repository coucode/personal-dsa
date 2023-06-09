"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

# class Solution:
#     def containsDuplicate(self, nums):
#         counts = {}
#         for num in nums:
#             if num in counts:
#                 counts[num] += 1
#                 if counts[num] >= 2: 
#                     return True
#             else: 
#                 counts[num] = 1
#         return False

### SOLUTION USING SET

class Solution:
    def containsDuplicate(self, nums):
        num_set = set()

        for num in nums:
            if num in num_set:
                return True
            else: 
                num_set.add(num)
        return False
