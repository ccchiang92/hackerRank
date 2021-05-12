#!/bin/python3

import os
import sys

#
# Complete the swapNodes function below.
#
def swapNodes(indexes, queries):
    def inOrder(tree):
        # return the tree in a list "in order"
        output=[]
        stack = [1]
        traversed =set()
        while stack:
            curNode=stack.pop()
            if (curNode in traversed):
                output.append(curNode)
            elif curNode != -1:
                traversed.add(curNode)
                stack.append(tree[curNode-1][1])
                stack.append(curNode)
                stack.append(tree[curNode-1][0])
        return output
    
    def swap(swapping, full):
        # swapping -> list of nodes where the children are to be swaped
        # full -> full tree
        # return a swaped tree
        for index in swapping:
            cur =full[index-1]
            full[index-1]=cur[::-1]
        return full
    
    output=[]
    for q in queries:
        curLevel =[1]
        nextLevel =[]
        depth = 1
        count = 1
        swapLevel = 1
        if q == 1:
            indexes=swap(curLevel,indexes)
            swapLevel += 1
        while count < len(indexes):
            for i in curLevel:
                curNode = indexes[i-1]
                for index in curNode:
                    if index!=-1:
                        nextLevel.append(index)
                        count += 1
            curLevel = nextLevel
            nextLevel =[]           
            depth += 1
            if swapLevel*q == depth:
                indexes=swap(curLevel,indexes)
                swapLevel += 1
        output.append(inOrder(indexes))
        
           
    return output
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
