#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr,n):
    # Write your code here
    sumZero = 0
    sumNegative = 0
    sumPositive = 0
    for i in range(0,len(arr),1):
        if(arr[i] == 0):
            sumZero = sumZero + 1
        elif(arr[i] > 0):
            sumPositive = sumPositive + 1
        elif(arr[i] < 0):
            sumNegative = sumNegative + 1
    ratio1,ratio2,ratio3 = CalculateRatio(sumZero,sumNegative,sumPositive,n)
    # return ratio1,ratio2,ratio3
    print(ratio1/n,ratio2/n,ratio3/n)
    # return sumZero,sumPositive,sumNegative
def CalculateRatio(sumZero,sumNegative,sumPositive,n):
    ratioZero = sumZero / n
    ratioPositive = sumPositive / n
    ratioNegative = sumNegative / n
    return [round(ratioZero,6),round(ratioPositive,6),round(ratioNegative,6)]
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr,n)