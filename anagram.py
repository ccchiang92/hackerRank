#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    chars ={}
    for char in a:
        chars[char] = chars.get(char,0)+1
    for char in b:
        chars[char] = chars.get(char,0)-1
    count = 0
    for val in chars.values():
        count +=abs(val)
    return count
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
