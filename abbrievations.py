#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'abbreviation' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def abbreviation(a, b):
    # initialize dp matrix
    dp =[[False for i in range(len(b)+1)] for j in range(len(a)+1)]
    # both empty case
    dp[0][0]=True
    # empty b case
    for i in range(1,len(a)+1):
        if a[i-1].islower():
            print(i)
            dp[i][0]=True
        else:
            # empty b vs Capital a
            # can just break loop since default is false
            break
    for di in range(1,len(a)+1):
        ai=di-1
        for dj in range(1,len(b)+1):
            bj=dj-1
            if a[ai]==b[bj]:
                dp[di][dj]=dp[di-1][dj-1]
            elif a[ai].upper()==b[bj]:
                dp[di][dj]=dp[di-1][dj-1] or dp[di-1][dj]
            elif a[ai].islower():
                dp[di][dj]= dp[di-1][dj]
    return 'YES' if dp[-1][-1] else 'NO'
                
    
            
  
    
  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
