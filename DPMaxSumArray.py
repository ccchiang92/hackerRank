#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    if len(arr)<=2:
        return max(arr)
    else:
        old_max=arr[0]
        cur_max=max(arr[0],arr[1])
        for i in range(2,len(arr)):
            self_max=arr[i]
            sum_max=self_max+old_max
            old_max=cur_max
            cur_max=max(self_max,sum_max,cur_max)
    return cur_max
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
