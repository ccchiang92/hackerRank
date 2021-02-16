#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    if len(arr)<3:
        return 0
    singles={}
    pair={}
    count = 0
    for i in arr[::-1]:
        second = i * r
        third = i * r* r
        count += pair.get((second,third),0)        
        pair[(i,second)]=pair.get((i,second),0)+singles.get(second,0)
        singles[i]=singles.get(i,0)+1
        
    
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
