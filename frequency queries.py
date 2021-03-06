#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    stored={}
    counts={}
    output=[]
    for i in queries:
        oper = i[0]
        data = i[1]
        if oper==1:
            adding = stored.get(data,0)+1
            stored[data]=adding
            counts[adding]=counts.get(adding,0)+1
            counts[adding-1]=counts.get(adding-1,1)-1
        elif oper ==2:
            # stored[data]=stored.get(data,1)-1
            if stored.get(data,0)!=0:
                subbing = stored.get(data)-1
                stored[data]=subbing
                counts[subbing]=counts.get(subbing,0)+1
                counts[subbing+1]=counts.get(subbing+1,1)-1
        else:
            if counts.get(data,0)>0:
                output.append(1)
            else:
                output.append(0)
    return output
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
