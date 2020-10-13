#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    s1=s2=k=0
    p=len(arr[0])-1
    for i in range(len(arr)):
        for j in range(len(arr)):
            if(i==j):
                s1+=arr[i][j]
                
    while(p>-1):
        s2+=arr[k][p]
        p-=1
        k+=1
    if(s1>s2):
        return s1-s2
    elif(s1<s2):
        return s2-s1
    else:
        return 0    
        
        
    return None
    # Write your code here

if __name__ == '__main__':


    #n = int(input("Enter no. of rows:").strip())

    arr = [[1,2,3],[4,5,6],[7,8,9]]

    
    result = diagonalDifference(arr)
    
