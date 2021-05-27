#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    left=[]
    legend=['(',')','[',']','{','}']
    for char in s:
        if char==legend[0] or char==legend[2] or char==legend[4]:
            left.append(char)
        elif char==legend[1] or char==legend[3] or char==legend[5]:
            if not left:
                return 'NO'
            else:
                match=left.pop()
                if char==legend[1]and match!=legend[0]:
                    return 'NO'
                elif char==legend[3]and match!=legend[2]:
                    return 'NO'
                elif char==legend[5]and match!=legend[4]:
                    return 'NO'
    return 'YES' if not left else 'NO'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
