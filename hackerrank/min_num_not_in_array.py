"""
Min Number Not in Array - HackerRank 3/27/23

Given an array A of N integers, returns the smallest positive integer
(greater than 0) that does not occur in A. 

For example: 
- Given A = [1, 3, 6, 4, 1, 2], the function should return 5
- Given A = [1, 2, 3], the function should return 4
- Given A = [-1, -3], the function should return 1

Write an efficient algorithm for the following assumptions: 
- N is an integer within the range [1..100,000]
- each element of array A is an integer within the range [-1,000,000 .. 1,000,000]
"""

"""
PASSING CODE
"""

# def smallest_not_included(A):
#     a = sorted(filter(lambda x: x >0, A))
#     if (len(a) == 0):
#         return 1
#     if (a[0] != 1):
#         return 1
#     for i in range(len(a)):
#         if i > 0:
#             diff = a[i] - a[i - 1]
#             if (diff > 1):
#                 return a[i - 1] + 1
#     return max(a) + 1

"""
Walkthrough Solution
- Create a set
- Set has a constant lookup time
- Time Complexity: O(n) because of the while loop
- Space Complexity: O(n)
"""

def smallest_not_included(A):
    seen = set(A)
    res = 1

    while res in seen: 
        res += 1
    
    return res