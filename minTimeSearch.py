#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minTime function below.
def minTime(machines, goal):
    max_days = math.ceil(goal/len(machines))*max(machines)
    min_days = math.ceil(goal/len(machines))*min(machines)
    up=max_days
    low=min_days
    tot=0
    for days in machines:
        tot+=min_days//days
    if tot >= goal:
        return min_days
    while up>low:
        mid_days= (up+low)//2
        tot=0
        for days in machines:
            tot+=mid_days//days
        if tot >=goal:
            up=mid_days
        elif tot < goal :
            low = mid_days+1
    return low
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()
