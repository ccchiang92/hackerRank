#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    move_count=0
    first = 1
    second = 2
    third = 3
    for i,val in enumerate(q):
        diff = val-(i+1)
        if (diff)>2:
            print('Too chaotic')
            return
        elif val == first:
            first = second
            second = third
            third +=1
        elif val == second:
            move_count += 1
            second = third            
            third +=1
        elif val == third:
            third +=1
            move_count += 2         
            
    print(move_count)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
