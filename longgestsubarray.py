#!/bin/python3

import math
import os
import random
import re
import sys

def longestSubarray(arr):
    # more optimize ver using a pointer method
    max_length =1
    i=1
    consec = 1
    length=1
    a=arr[0]
    b_yet =True
    while i<len(arr):
        if arr[i]==arr[i-1]:
            consec+=1
        else:
            consec=1
        if arr[i]==a:
            length +=1
        elif b_yet:
            if abs(arr[i]-a)==1:
                b=arr[i]
                b_yet =False
                length +=1
            else:
                length=1
                a=arr[i]
        elif arr[i]==b:
            length +=1
        elif abs(arr[i]-arr[i-1])==1:
            a=arr[i-1]
            b=arr[i]
            length=consec+1
        else:
            length=1
            b_yet=True
            a=arr[i]
        i+=1
        max_length =max(length,max_length)
    return max_length
            
