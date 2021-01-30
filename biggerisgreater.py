#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    end = len(w)-1
    change_point=end+1
    output=''
    for i in range(end):
        if w[end-i] > w[end-1-i]:
            change_point=end-i-1
            break
    if change_point == end+1:
        return 'no answer'
    else:
        if change_point+1 == end:
            min_char=w[end]
            output += w[0:change_point]
            output += w[end]
            output += w[change_point]
            return output
        else:
            if change_point!=0:
                    output += w[0:change_point]
            min_char=w[change_point+1]
            min_index = change_point+1
            for i in range(change_point+1,end+1):
                if (w[i]>w[change_point])& (w[i]<min_char):
                    min_char= w[i]
                    min_index = i           
            output += min_char
            temp = w[change_point:min_index] + w[min_index+1:end+1]
            temp = sorted(temp)
            for char in temp:
                output += char
            return output
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
