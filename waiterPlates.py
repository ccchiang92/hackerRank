#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#

def gen_primes():
    # prime generator from stack overflow
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1
        
def waiter(number, q):
    prime_generator=gen_primes()
    answers=[]
    for i in range(q):
        p=next(prime_generator)
        A=[]
        B=[]
        while number:
            cur=number.pop()
            if cur%p==0:
                B.append(cur)
            else:
                A.append(cur)
        while B:
            answers.append(B.pop())
        number=A
    while number:
        answers.append(A.pop())
    return answers
                
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
