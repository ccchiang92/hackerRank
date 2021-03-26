#!/bin/python3

import math
import os
import random
import re
import sys
# 332
# 323
# 233

# Complete the isValid function below.
def isValid(s):
    extra = False
    checks={}
    for char in s:
        checks[char]=checks.get(char,0)+1
    vals=list(checks.values())
    if len(checks)>=3:
        first=vals[0]
        second=vals[1]
        third=vals[2]
        if (first==second) | (first == third):
            check_val=first
        elif second==third:
            check_val = second
        else:
            return 'NO'
    else:
        check_val=vals[0]
    for val in checks.values():
        if check_val != val:
            if abs(val-check_val) == 1:
                if extra:
                    return 'NO'
                else:
                    extra = True
            elif val==1:
                extra = True
            else:
                return 'NO'
    return 'YES'
                    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
