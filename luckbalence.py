#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    max_luck=0
    important = []
    for contest in contests:
        max_luck+=contest[0]
        if contest[1]:
            important.append(contest[0])
    important.sort()
    for i in range(len(important)-k):
        max_luck-=important[i]*2
    return max_luck
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
