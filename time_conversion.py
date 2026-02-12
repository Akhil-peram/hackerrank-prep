#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    period = s[-2:]       # AM or PM
    hh = int(s[:2])       # hours
    mm = s[3:5]           # minutes
    ss = s[6:8]           # seconds

    # Conversion logic
    if period == "AM":
        if hh == 12:
            hh = 0
    else:  # PM case
        if hh != 12:
            hh += 12

    # Format back to string with leading zeros
    return f"{hh:02}:{mm}:{ss}"


        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
