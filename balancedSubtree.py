#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'mostBalancedPartition' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY parent
#  2. INTEGER_ARRAY files_size
#

def mostBalancedPartition(parent, files_size):
    # Write your code here
    total = sum(files_size)
    sub_size={}
    # faster method
    # build a dictionary of children
    # then use children dict for recursion mapping of sub_size
    # children={}
    # for i in range(1,len(parent)):
    #     prev_entry = children.get(parent[i],[])
    #     prev_entry.append(i)
    #     children[parent[i]]=prev_entry
    # def fill(ind):
    #     local_size = files_size[i]
    #     for child in children[ind]:
    #        local_size+=fill(child)
    #     sub_size[ind]=local_size

    for i in range(len(parent)):
        sub_size[i]=sub_size.get(i,0)+files_size[i]
        cur_parent = parent[i]
        while cur_parent!=-1:
            sub_size[cur_parent]=sub_size.get(cur_parent,0)+files_size[i]
            cur_parent=parent[cur_parent]
    output=total
    for size in sub_size.values():
        output=min(output,abs(total-size-size))

    return output
        

if __name__ == '__main__':