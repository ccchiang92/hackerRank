#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'contacts' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY queries as parameter.
#
def contacts(queries):
    output=[]
    starts={}
    for q in queries:
        if q[0]=='add':
            word=q[1]
            for i in range(len(q[1])):
                starts[word[:i+1]]=starts.get(word[:i+1],0)+1
        elif q[0]=='find':
            output.append(starts.get(q[1],0))
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries_rows = int(input().strip())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
