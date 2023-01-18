#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    swaps = 0
    for index in range(len(a)):
        for index2 in range(len(a)-1):
            if a[index2] > a[index2+1]:
                temp = a[index2]
                a[index2] = a[index2+1]
                a[index2+1] = temp
                swaps = swaps + 1
    print("Array is sorted in", swaps, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[len(a)-1])

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
