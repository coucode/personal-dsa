#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'arrange' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def arrange(sentence):
    lengths = {}
    words = sentence[0:-1].split(' ')
    for word in words:
        if len(word) in lengths:
            lengths[len(word)].append(word)
        else:
            lengths[len(word)] = [word]
            
    # Get a list of the keys
    # Sort the keys
    # Iterate through the keys and add their values to a string
    # If it is the first value, Uppercase, middle values, lowercase, last value lowercase + add a period
    
    # keys = sorted(lengths.keys())
    arranged = ''
    count = 0
    
    for key in sorted(lengths.keys()):
        joined = ' '.join(lengths[key])
        if count == 0:
            arranged = joined.capitalize()
        else: 
            arranged = arranged + " " + joined.lower()
        count += 1
    
    return arranged + '.'