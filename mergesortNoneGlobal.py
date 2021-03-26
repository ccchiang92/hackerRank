#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countInversions function below.
def countInversions(arr):
    def mergeSort(arr,count):
        l=len(arr)
        local = 0
        if l>1:
            mid = l//2
            left, localL= mergeSort(arr[:mid],count)
            right, localR = mergeSort(arr[mid:],count)
            local += localL + localR
            new=[]
            x = 0
            y = 0
            for z in range(l):
                if x<mid and y<l-mid:
                    if left[x]<=right[y]:
                        new.append(left[x])
                        x += 1
                    else:
                        new.append(right[y])
                        y += 1
                        local += (mid - x)
                elif x<mid:
                    new.append(left[x])                    
                    x += 1        
                elif y<l-mid:
                    new.append(right[y])
                    y += 1
            return new, count + local     
        else:
            return arr, count
    temp, final = mergeSort(arr,0)
    return final


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
