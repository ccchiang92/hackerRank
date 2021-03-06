#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    import bisect
    notif=0
    if len(expenditure)>d:
        if d%2==0:
            isEven=True
        else:
            isEven=False
        trail=expenditure[0:d]
        trail.sort()
        for i in range(d, len(expenditure)):
            if i!=d:
                del trail[bisect.bisect_left(trail,expenditure[i-d-1])]
                bisect.insort(trail,expenditure[i-1])
            if isEven:
                med=(trail[d//2]+trail[(d//2)-1])/2
            else:
                med = trail[d//2]
            if expenditure[i]>=2*med:
                notif += 1
    return notif
                
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
