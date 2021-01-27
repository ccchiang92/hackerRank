#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    s=s.replace(' ','')
    c = math.ceil(math.sqrt(len(s)))
    r = math.floor(math.sqrt(len(s)))
    if (r * c) < len(s):
        r = c
    output={}
    for i in range(0,c):
        output[i]=''
        for j in range(0,len(s),c):  
            if (i+j)<len(s):       
                if output[i]:
                    output[i]+=s[j+i]
                else:
                    output[i]=s[j+i]
    returnString=''
    for i in output:
        if returnString=='':
            returnString=output[i]
        else:
            returnString+=' '
            returnString+=output[i]
    return returnString
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()

    
