#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    table={}
    for i in range(len(cost)):
        cur=(table.get(cost[i],[]))
        cur.append(i)
        table[cost[i]]=cur
    for i in range(len(cost)):
        if cost[i]<money:
            change = money-cost[i]
            match = table.get(change)
            if match:
                if match[0]!=i:
                    print(f"{i+1} {match[0]+1}")
                    return
                elif len(match)>1:
                    print(f"{i+1} {match[1]+1}")
                    return
                    
                    

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
