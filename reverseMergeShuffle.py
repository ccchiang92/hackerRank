#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the reverseShuffleMerge function below.
def reverseShuffleMerge(s):
    reverse = reversed(s)
    char_count ={}
    needed ={}
    used={}
    stack=[]
    for char in s:
        char_count[char]=char_count.get(char,0)+1
    for key in char_count:
        needed[key]=char_count[key]//2
        used[key]=0
    
    for char in reverse:
        if needed[char]>used[char]:
            while stack and (stack[-1]>char) and (used[stack[-1]]+char_count[stack[-1]]-1>=needed[stack[-1]]):
                last_char = stack.pop()
                used[last_char]-=1
            used[char]+=1
            stack.append(char)
        char_count[char]-=1
    return ''.join(stack)
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = reverseShuffleMerge(s)

    fptr.write(result + '\n')

    fptr.close()
