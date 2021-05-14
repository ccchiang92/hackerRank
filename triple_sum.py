#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the triplets function below.
def triplets(a, b, c):
    #sort and remove duplicates
    US_a = sorted(list(set(a)))
    US_b = sorted(list(set(b)))
    US_c = sorted(list(set(c)))
    a_pointer=0
    c_pointer=0
    output=0
    for i in range(len(US_b)):
        while a_pointer<len(US_a) and US_a[a_pointer]<=US_b[i]:
            a_pointer+=1
        while c_pointer<len(US_c) and US_c[c_pointer]<=US_b[i]:
            c_pointer+=1
        output += c_pointer * a_pointer
    
    return output
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
