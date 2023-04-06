"""
Order Check - HackerRank 3/20/23

Students in a class are asked to stand in ascending order
according to their heights for the annual class photograph. 
Determine the number of students not currently standing in their correct positions. 

Example: 
height = [1, 1, 3, 3, 4, 1]

The 3 students indicated indices 2, 4, and 5 are not in the right positions. The correct positions are [1, 1, 1, 3, 3, 4].
Return 3. 

"""

"""
PASSING CODE
"""

def countStudents(height):
    # Write your code here
    pos = sorted(height)
    count = 0
    indx = 0
    while (indx < len(height)):
        if (height[indx] != pos[indx]):
            count += 1
        indx += 1
    
    return count