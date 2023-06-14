"""
pair sum
Write a function, pair_sum, that takes in a list and a target sum as arguments. 
The function should return a tuple containing a pair of indices whose elements sum to the given target. 
The indices returned must be unique.

Be sure to return the indices, not the elements themselves.

There is guaranteed to be one such pair that sums to the target.

pair_sum([3, 2, 5, 4, 1], 8) # -> (0, 2)
pair_sum([4, 7, 9, 2, 5, 1], 5) # -> (0, 5)
pair_sum([4, 7, 9, 2, 5, 1], 3) # -> (3, 5)
pair_sum([1, 6, 7, 2], 13) # -> (1, 2)
pair_sum([9, 9], 18) # -> (0, 1)
pair_sum([6, 4, 2, 8 ], 12) # -> (1, 3)

"""

"""
ASSUMPTIONS/EDGE CASES:
- INPUT: List of integers, integer of target sum
- OUTPUT: Tuple with pair of indices

PATTERN: 
Two Pointer

PSEUDOCODE:
1. Set variables for left and right pointers, and answer
   1a. Left Pointer starts at 0
   1b. Right Pointer starts to the right of the left pointer
2. While answer variable is null do the following steps:
3. Increment the right pointer and check if the values equal the target sum
   3a. If yes, return a tuple with the value of the left and right pointer
   3b. If no, increment the right pointer
4. If there is no answer and right pointer has reached the end, increment the left pointer
   and set the right pointer to the left pointer + 1
5. Return the answer
"""

def pair_sum(numbers, target_sum):
  left = 0
  right = 1
  answer = False
  
  while answer is False:
    if (numbers[left] + numbers[right] == target_sum):
      answer = (left, right)
      return answer
    else:
      if (right == len(numbers) - 1):
        left += 1
        right = left + 1
      else: 
        right += 1