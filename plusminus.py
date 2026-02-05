#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos=[]
    neg=[]
    zer=[]
    n=len(arr)
    for nums in arr:
        if nums <0:
            neg.append(nums)
        elif nums >0:
            pos.append(nums)
        else:
            zer.append(nums)
    postot=len(pos)/n
    negtot=len(neg)/n
    zertot=len(zer)/n
    print(f"{postot}")
    print(negtot)
    print(zertot)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
