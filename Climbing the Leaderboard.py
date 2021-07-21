#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    numbers=[]
    output=[]
    r_counts=0
    for i in range(len(ranked)):
        if r_counts==0:
            r_counts+=1
            numbers.append(r_counts)
        elif ranked[i]==ranked[i-1]:
            numbers.append(r_counts)
        else:
            r_counts+=1
            numbers.append(r_counts)
    current=len(ranked)-1
    for p in player:
        count=0
        while ranked[current]<p:
            count+=1
            if current!=0:
                current-=1
            else:
                break
        if ranked[current]==p:
            output.append(numbers[current])
        elif ranked[current]<p:
            output.append(1)
        else:
            output.append(numbers[current]+1)
            
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
