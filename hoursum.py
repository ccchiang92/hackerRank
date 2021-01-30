#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    sums=[]
    for i in range(4):
        for j in range(4):
            ind_sum=0        
            ind_sum += sum(arr[i][j:j+3])
            ind_sum += sum(arr[i+2][j:j+3])
            ind_sum += arr[i+1][j+1]
            sums.append(ind_sum)
    return max(sums)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
