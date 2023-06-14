"""
pair product
Write a function, pair_product, that takes in a list and a target product as 
arguments. The function should return a tuple containing a pair of indices 
whose elements multiply to the given target. The indices returned must be unique.

Be sure to return the indices, not the elements themselves.

There is guaranteed to be one such pair whose product is the target.

pair_product([3, 2, 5, 4, 1], 8) # -> (1, 3)
pair_product([3, 2, 5, 4, 1], 10) # -> (1, 2)
pair_product([4, 7, 9, 2, 5, 1], 5) # -> (4, 5)
pair_product([4, 7, 9, 2, 5, 1], 35) # -> (1, 4)
pair_product([3, 2, 5, 4, 1], 10) # -> (1, 2)
pair_product([4, 6, 8, 2], 16) # -> (2, 3)
"""
# TWO POINTER SOLUTION
# def pair_product(numbers, target_product):
#   left = 0
#   right = 1
#   answer = False
  
#   while answer is False:
#     if (numbers[left] * numbers[right] == target_product):
#       return (left, right)
#     else:
#       if right == len(numbers) - 1:
#         left += 1
#         right = left + 1
#       else: 
#         right += 1

# Hash Map Solution
def pair_product(numbers, target_product):
  prev = {}
  
  for i, num in enumerate(numbers):
    complement = target_product/num
    
    if (prev.get(complement)):
      return (i, prev[complement])
    else: 
      prev[num] = i