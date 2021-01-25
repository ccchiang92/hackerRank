#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    max = arr[0]
    min = arr[0]
    sum = arr[0]
    for i in range(1,len(arr)):
        if arr[i]> max:
            max = arr[i]
        elif arr[i]<min:
            min = arr[i]
        sum+=arr[i]
    s_sum = sum - max
    l_sum = sum - min
    print(str(s_sum) +' '+ str(l_sum))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
