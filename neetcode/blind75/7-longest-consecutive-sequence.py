"""
Longest Consecutive Sequence
Medium
15.6K
650
Companies
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
Accepted
1.1M
Submissions
2.2M
Acceptance Rate
48.5%
"""

# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         sorted_nums = sorted(nums)
#         count = 1
#         longest = 1

#         if (len(sorted_nums) == 0):
#             return 0

#         for i in range(len(sorted_nums)):
#             if i >= 1:
#                 if (sorted_nums[i] - sorted_nums[i - 1]) == 1:
#                     count += 1
#                     if count >= longest:
#                         longest = count
#                 elif (sorted_nums[i] - sorted_nums[i - 1]) == 0:
#                     pass
#                 else: 
#                     count = 1
#         return longest

"""Solution using Set"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0        

        for num in nums_set:
            if (num - 1) not in nums_set:
                length = 1
                while (num + length) in nums_set:
                    length += 1
                if (length >= longest):
                    longest = length
        
        return longest