#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countInversions function below.
def countInversions(arr):
    countInversions.count = 0
    def mergeSort(arr):
        l=len(arr)
        if l>1:
            mid = l//2
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])
            new=arr
            x = 0
            y = 0
            for z in range(l):
                if x<mid and y<l-mid:
                    if left[x]<=right[y]:
                        new[z]=left[x]
                        x += 1
                    else:
                        new[z]=right[y]
                        y += 1
                        countInversions.count += (mid - x)
                elif x<mid:
                    new[z]=left[x]
                    x += 1        
                elif y<l-mid:
                    new[z]=right[y]
                    y += 1
            return new      
        else:
            return arr
    mergeSort(arr)
    return countInversions.count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
