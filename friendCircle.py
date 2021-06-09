#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxCircle function below.
def maxCircle(queries):
    maxSize=0
    connections={}
    sizeByRoot={}
    output=[]
    def getRoot(node):
        if not connections.get(node):
            return None
        else:
            origin=node
            while node!=connections[node]:
                node=connections[node]
            if connections[origin]!=node:connections[origin]=node
            return node
    for first,second in queries:
        root1=getRoot(first)
        root2=getRoot(second)
        if not root1 and not root2:
            if not connections:
                maxSize=2
            connections[first]=first
            connections[second]=first
            sizeByRoot[first]=2
        elif root1 and root2:
            if root1!=root2:
                if sizeByRoot[root2]>sizeByRoot[root1]:root1,root2 = root2, root1
                connections[root2]=root1
                sizeByRoot[root1]+=sizeByRoot[root2]
                maxSize=max(maxSize,sizeByRoot[root1])
        else:
            if root2 and not root1:
                root1,root2 = root2, root1
                first, second = second, first
            connections[second]=root1
            sizeByRoot[root1]+=1
            maxSize=max(maxSize,sizeByRoot[root1])
        output.append(maxSize)
                    
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = maxCircle(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
