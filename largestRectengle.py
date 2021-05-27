#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(h):
    stack=[]
    mArea=0
    for i in range(len(h)):
        if not stack:
            stack.append(i)
        elif h[stack[-1]]<=h[i]:
            stack.append(i)
        else:
            while h[stack[-1]]>h[i]:
                topi=stack.pop()
                top=h[topi]
                if stack:
                    mArea=max(mArea,top*(i-stack[-1]-1))
                else:
                    mArea=max(mArea,top*i)
                    break
            stack.append(i)
    while stack:
        topi=stack.pop()
        if stack:
            mArea=max(mArea,h[topi]*(len(h)-stack[-1]-1))
        else:
            mArea=max(mArea,len(h)*h[topi])
    return mArea
                
       
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
