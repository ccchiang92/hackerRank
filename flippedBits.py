#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
    binary=''
    remainder=n
    while remainder>1:
        newBit=remainder%2
        remainder=remainder//2
        binary=str(newBit)+binary
    binary=str(remainder)+binary
    extra=32-len(binary)
    binary=('0'*extra)+binary
    output=0
    for i,digit in enumerate(binary):
        filped=(int(digit)+1)%2
        output+=pow(2,31-i)*filped
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
