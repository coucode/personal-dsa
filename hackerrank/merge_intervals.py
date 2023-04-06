"""
Merge Intervals - HackerRank 3/27/23

Given an array of intervals where intervals[i] = [start, end]
merge all overlapping intervals, and return an array of the 
non-overlapping intervals that coverall all the intervals in the input

Example 1: 
Input: 
- intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

Output: 
- [[1, 6], [8, 10], [15, 18]]

Explanation: Since intervals [1, 3] and [2, 6] overlap, merge them into [1, 6]
"""

"""
My (Incomplete) Solution as of 3/28/23
"""

# def merge_intervals(intervals):
    
#     length = len(intervals) + 1

#     while(len(intervals) != length):
#         length = len(intervals)

#         for i in range(len(intervals)):
#             if (i > 0):
#                 if (intervals[i][0] <= intervals[i - 1][1]):
#                     copy = intervals[0:i - 1]
#                     copy.append([intervals[i - 1][0], intervals[i][1]])
#                     if (i < len(intervals) - 1):
#                       copy.append(intervals[i + 1:])
#                     intervals = copy

#     print(intervals)
#     return intervals

"""
Walkthrough Solution
1. Sort the input so the intervals are in the correct order
2. 
Time Complexity: n log n
Space Complexity: 
- 
"""

def merge_intervals(intervals):
    intervals.sort(reverse=True)
    answer = []

    while len(intervals) > 1:
        if intervals[-1][1] >= intervals[-2][0]:
            intervals[-2][0] = min(intervals[-1][0], intervals[-2][0])
            intervals[-2][1] = max(intervals[-1][1], intervals[-2][1])
            intervals.pop()
        else:
            answer.append(intervals.pop())
    return answer + intervals

# merge_intervals([[1,4], [4, 6]])
merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]])