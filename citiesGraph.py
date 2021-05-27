#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#

def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_road>=c_lib:
        return c_lib*n
    else:
        connections={}
        for road in cities:
            a=road[0]-1
            b=road[1]-1
            connections[a]=connections.get(a,[])+[b]
            connections[b]=connections.get(b,[])+[a]
        for i in range(n):
            if not connections.get(i,False):
                connections[i]=[]
        visited=set()
        searched=set()
        tot=0
        nextStack=[x for x in range(n)]
        while nextStack:
            i = nextStack.pop()
            if i not in visited:
                visited.add(i)
                searched.add(i)
                tot+=c_lib
                for city in connections[i]:
                    if city not in visited:
                        visited.add(city)
                        tot+=c_road
                        nextStack.append(city)
            elif i not in searched:
                searched.add(i)
                for city in connections[i]:
                    if city not in visited:
                        visited.add(city)
                        tot+=c_road
                        nextStack.append(city)
        return tot

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
