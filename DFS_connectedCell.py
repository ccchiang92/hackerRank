#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxRegion' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#

def maxRegion(grid):
    row=len(grid)
    col=len(grid[0])
    visited={}
    groupID=0
    maxlength=0
    for i in range(row):
        for j in range(col):
            if grid[i][j]==1 and visited.get((i,j)) is None:
                visited[(i,j)]=groupID
                currentLen=1
                maxlength=max(maxlength,1)
                stack=[(i,j)]
                while stack:
                    cur=stack.pop()
                    for x in range(cur[0]-1,cur[0]+2):
                        for y in range(cur[1]-1,cur[1]+2):
                            if x>=0 and x<row and y>=0 and y<col:
                                if grid[x][y]==1 and visited.get((x,y)) is None:
                                    visited[(x,y)]=groupID
                                    currentLen+=1
                                    maxlength=max(maxlength,currentLen)
                                    stack.append((x,y))
                groupID+=1
    return maxlength
                                    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    m = int(input().strip())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)

    fptr.write(str(res) + '\n')

    fptr.close()
