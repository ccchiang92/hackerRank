#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'primality' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#

def primality(n):
    if n==2 or n==3:
        return 'Prime'
    elif n%2==0 or n%3==0 or n==1:
        return 'Not prime'
    else:
        i=5
        while i**2<=n:
            if n%i==0 or n%(i+2)==0:
                return 'Not prime'
            else:
                i+=6
    return 'Prime'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    p = int(input().strip())

    for p_itr in range(p):
        n = int(input().strip())

        result = primality(n)

        fptr.write(result + '\n')

    fptr.close()
