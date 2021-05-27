#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the riddle function below.
def riddle(arr):
    # complete this function
    out=[]
    minList=[0]*(len(arr)-1)
    for i in range(len(arr)):
        maxL=-1
        if i==0:
            for j in range(len(arr)):
                if j<len(arr)-1:
                    minList[j]=arr[j]
                maxL=max(arr[j],maxL)
        else:
            for k in range(len(minList)):
                minList[k]=min(arr[i+k],minList[k])
                maxL=max(maxL,minList[k])
            minList.pop()
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
