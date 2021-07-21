#!/usr/bin/python

def displayPathtoPrincess(n,grid):
    if grid[0][0]=='p':
        corner=1
    elif grid[0][n-1]=='p':
        corner=2
    elif grid[n-1][0]=='p':
        corner=3
    elif grid[n-1][n-1]=='p':
        corner=4
    for _ in range(n//2):
        if corner==1 or corner ==2:
            print('UP')
        else:
            print('DOWN')
    
    for _ in range(n//2):
        if corner==1 or corner ==3:
            print('LEFT')
        else:
            print('RIGHT')
    


m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)