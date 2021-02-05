#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0 for i in range(n)]
    for q in queries:
        arr[q[0]-1]+=q[2]
        if (q[1]) != n:
            arr[q[1]]-=q[2]
    starting_val = 0    
    max_val = 0
    for val in arr:
        starting_val+=val
        max_val = max(max_val,starting_val)
    return max_val
            
        
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
