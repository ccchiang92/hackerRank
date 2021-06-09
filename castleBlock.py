#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER startX
#  3. INTEGER startY
#  4. INTEGER goalX
#  5. INTEGER goalY
#

def minimumMoves(grid, startX, startY, goalX, goalY):
    minMoves=10201
    thisLevel=[]
    nextLevel=[]
    upperX=len(grid)
    upperY=len(grid[0])
    thisLevel.append((startX+1,startY,1,0))
    thisLevel.append((startX-1,startY,1,1))
    thisLevel.append((startX,startY+1,1,2))
    thisLevel.append((startX,startY-1,1,3))
    visited={}
    
    while thisLevel:
        curNode=thisLevel.pop()
        curX=curNode[0]
        curY=curNode[1]
        curMove=curNode[2]
        curDirection=curNode[3]
        # pass out of bounds, blocked and reach goal cases
        if curX<0 or curX>upperX-1 or curY<0 or curY>upperY-1:
            if not thisLevel and nextLevel:
                thisLevel=nextLevel
                nextLevel=[]
            continue
        elif curX==goalX and curY==goalY:
            minMoves=min(minMoves,curMove)
            if not thisLevel and nextLevel:
                thisLevel=nextLevel
                nextLevel=[]
            continue
        elif grid[curX][curY]=='X':
            if not thisLevel and nextLevel:
                thisLevel=nextLevel
                nextLevel=[]
            continue
        else:
            lastVisitedMoves = visited.get((curX,curY),10201)
            if lastVisitedMoves >= curMove:
                visited[(curX,curY)]=curMove
                if curDirection==1 or curDirection==3:
                    opposite=curDirection-1
                else:
                    opposite=curDirection+1
                for i in range(4):
                    if i==opposite:
                        continue
                    elif i==curDirection:
                        nextMove=curMove
                    else:
                        nextMove=curMove+1
                    if i ==0 and visited.get((curX+1,curY),10201)>nextMove and curX+1<upperX:
                        nextLevel.append((curX+1,curY,nextMove,0))
                    elif i==1 and visited.get((curX-1,curY),10201)>nextMove and curX-1>=0:
                        nextLevel.append((curX-1,curY,nextMove,1))
                    elif i==2 and visited.get((curX,curY+1),10201)>nextMove and curY+1<upperY:
                        nextLevel.append((curX,curY+1,nextMove,2))
                    elif i==3 and visited.get((curX,curY-1),10201)>nextMove and curY-1>=0:
                        nextLevel.append((curX,curY-1,nextMove,3))
        # print(nextLevel)
        # print(thisLevel)
        if not thisLevel and nextLevel:
            thisLevel=nextLevel
            nextLevel=[]
    # print(visited)
    return minMoves
    # asdasdas
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    first_multiple_input = input().rstrip().split()

    startX = int(first_multiple_input[0])

    startY = int(first_multiple_input[1])

    goalX = int(first_multiple_input[2])

    goalY = int(first_multiple_input[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()
