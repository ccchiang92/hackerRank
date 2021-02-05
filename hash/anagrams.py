#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    from itertools import combinations
    from collections import Counter
    ana_count=0
    # generate all possible substring indicies with combinations then splice to create a list of substrings
    # also sort all substring and rejoins them
    all_subStrings = [''.join(sorted(s[i:j])) for i , j in combinations(range(len(s)+1),2)]
    counts = Counter(all_subStrings)
    for v in counts.values():
        if v==2:
            ana_count +=1            
        elif v>2:
            ana_count += sum(range(v))            
    
    return ana_count
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
