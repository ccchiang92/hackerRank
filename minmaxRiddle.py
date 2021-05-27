#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the riddle function below.
def riddle(arr):
    # complete this function
    import copy
    out=[]
    for i in range(len(arr)):
        stack=copy.copy(arr)
        maxL=-1
        while len(stack)>i:
            poped=[]
            minL=pow(10,10)
            for j in range(i+1):
                cur=stack.pop()
                poped.append(cur)
                minL=min(minL,cur)
            for l in range(i):
                stack.append(poped.pop())
            maxL=max(maxL,minL)
        out.append(maxL)
    return out

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = riddle(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
