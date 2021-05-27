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
    import bisect 
    from collections import deque
    out=[]
    for i in range(len(arr)):
        stack=copy.copy(arr)
        maxL=-1
        while len(stack)>i:
            poped=deque()
            minL=stack[-1]
            contain={}
            for j in range(i+1):
                cur=stack.pop()
                contain[cur]=contain.get(cur,0)+1
                poped.append(cur)
            minList=deque(sorted(poped))
            minL=minList[0]
            maxL=max(maxL,minL)            
            while stack:
                outgoing=poped.popleft()
                contain[outgoing]-=1
                cur=stack.pop()
                contain[cur]=contain.get(cur,0)+1
                poped.append(cur)
                bisect.insort(minList, cur)                 
                if cur <=minL:
                    minL=cur
                elif outgoing <=minL:
                    minList.popleft()
                    minNext=minList[0]
                    while contain[minNext]<=0:
                        minList.popleft()
                        if minList:
                            minNext=minList[0]
                        else:
                            break
                    minL=minNext
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
