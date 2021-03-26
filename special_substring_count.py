#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    count = n
    for i in range(n-1):
        cur = s[i]
        mid = True
        for j in range(i+1,n):
            if s[j]==cur:
                if mid:
                    count += 1
                elif (mid_i-i)==(j-mid_i):
                    count += 1
                    break
            elif mid:
                mid = False
                mid_i = j
            else:
                break
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
