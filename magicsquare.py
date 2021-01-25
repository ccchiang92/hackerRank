#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    def isMag(arr):
        if (arr[0]+arr[4]+arr[8]) != 15:
            return False
        elif (arr[2]+arr[4]+arr[6]) != 15:
            return False
        else:
            for i in range(3):
                if sum(arr[i*3:i*3+3]) != 15:
                    return False
                elif sum([arr[i],arr[i+3],arr[i+6]]) != 15:
                    return False
            return True
    
    from itertools import permutations  
    x= []
    for i in range(3):
        for j in range(3):
            x.append(s[i][j])
    permuts = permutations(range(1,10))
    min_cost =9999
    for a_list in permuts:
        if isMag(a_list):
            min_cost = min(min_cost,sum([abs(a_list[i]-x[i])for i in range(9)]))
    return min_cost
            
    # print(x)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
