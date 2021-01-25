#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    zeros = 0
    pos = 0
    neg = 0
    tot = len(arr)
    for i in range(tot):
        if arr[i]==0:
            zeros += 1
        elif arr[i]>0:
            pos += 1
        else:
            neg += 1
    print(round(pos/tot,6))    
    print(round(neg/tot,6))    
    print(round(zeros/tot,6))    

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
