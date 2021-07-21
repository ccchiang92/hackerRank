#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#
def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    searchStack=[]
    nextStack=[]
    visited={}
    nodes={}
    # init of searchable structure
    for i in range(graph_nodes):
        nodes[i+1]=[]
    for i, origin in enumerate(graph_from):
        endPoint=graph_to[i]
        listofEndPoints=nodes.get(origin)
        listofEndPoints.append(endPoint)
        nodes[origin]=listofEndPoints
    for i, origin in enumerate(graph_to):
        endPoint=graph_from[i]
        listofEndPoints=nodes.get(origin)
        listofEndPoints.append(endPoint)
        nodes[origin]=listofEndPoints
    # add all color==val nodes to initial stack
    for i in range(len(ids)):
        if ids[i] == val:
            searchStack.append((i+1,i+1,0))
    # bfs
    while searchStack:
        curSearch=searchStack.pop()
        origin=curSearch[1]
        curNode=curSearch[0]
        edgeLength=curSearch[2]
        if not visited.get(curNode):
            visited[curNode]=(origin,edgeLength)
            connected=nodes[curNode]
            for endPoint in connected:
                nextStack.append((endPoint,origin,edgeLength+1))
        elif visited.get(curNode)[0]!=origin:
            return edgeLength+visited.get(curNode)[1]
        if not searchStack:
            searchStack, nextStack = nextStack, searchStack
            
    return -1
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    fptr.write(str(ans) + '\n')

    fptr.close()
