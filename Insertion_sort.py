#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    for index in range(1, n):
        key = arr[index]
        index2 = index - 1
        while index2 >= 0:
            if arr[index2] < key:
                break
            if arr[index2] > key:
                arr[index2+1] = arr[index2]
                for index in arr:
                    print(index, end=' ')
                print()
            index2 = index2 - 1
        arr[index2+1] = key
        
    for i in arr:
        print(i, end=' ')

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
