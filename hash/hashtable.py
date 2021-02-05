#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    mag_dic = {}
    for word in magazine:
        if mag_dic.get(word):
            mag_dic[word]+=1
        else:
            mag_dic[word]=1
    for word in note:
        if mag_dic.get(word)!=None:
            if mag_dic[word]>0:
                mag_dic[word]-=1
            else:
                print('No')
                return
        else:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
