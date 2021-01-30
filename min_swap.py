#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    count=0
    i=0
    new=arr
    while i<len(arr):
        if arr[i]!=i+1:
            swap_ind = arr[i]
            swap_val = arr[swap_ind-1]
            arr[swap_ind-1]=swap_ind
            arr[i]=swap_val
            count+=1
        else:
            i+=1
            
    return count
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
