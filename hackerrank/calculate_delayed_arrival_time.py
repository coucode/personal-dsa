#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findDelayedArrivalTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER arrivalTime
#  2. INTEGER delayedTime
#

"""
You are given a positive integer arrivalTime denoting the arrival time of a train in hours, and another 
positive integer delayedTime denoting the amount of delay in hours. Return the time wehn the train will
arrive at the station. Note that the time in this problem is in 24-hours format
"""

def findDelayedArrivalTime(arrivalTime, delayedTime):
    # Write your code here
    answer = arrivalTime + delayedTime
    
    if answer == 24:
        return 0

    elif answer > 24:
        return answer - 24
    else: 
        return answer
if __name__ == '__main__':