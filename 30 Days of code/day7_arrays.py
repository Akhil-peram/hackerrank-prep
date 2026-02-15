#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    left = 0
    right = len(arr) -1
    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left+=1
        right-=1
    print(" ".join(str(x) for x in arr))

