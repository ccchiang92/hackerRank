#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER maxSum
#  2. INTEGER_ARRAY a
#  3. INTEGER_ARRAY b
#

from collections import deque
def twoStacks(maxSum, a, b):
    rolling_sum=0
    stackA=deque(a)
    stackB=deque(b)
    b_j=0
    a_i=0
    while rolling_sum<=maxSum and stackA:
        cur=stackA.popleft()
        if rolling_sum+cur<=maxSum:
            a_i+=1
            rolling_sum+=cur
        else:
            break
    maxCount=a_i
    while stackB:
        if rolling_sum+stackB[0]<=maxSum:
            cur=stackB.popleft()
            rolling_sum+=cur
            b_j+=1
            maxCount=max(a_i+b_j,maxCount)
        elif a_i>0:
            rolling_sum-=a[a_i-1]
            a_i-=1
        else:
            stackB=[]
            break
    return max(a_i+b_j,maxCount)
   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        maxSum = int(first_multiple_input[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(maxSum, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
