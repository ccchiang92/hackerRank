#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    arr.sort()
    smallest = arr[len(arr)-1]-arr[0]
    for i in range(0,len(arr)-k+1):
        if arr[i+k-1]-arr[i]<smallest:
            smallest = arr[i+k-1]-arr[i]
    return smallest
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
