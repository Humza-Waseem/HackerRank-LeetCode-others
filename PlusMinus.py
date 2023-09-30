

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

def plusMinus(arr):
    length_of_array = len(arr)
    positive = len([x for x in arr if x > 0]) / length_of_array
    negative = len([x for x in arr if x < 0]) / length_of_array
    zero = len([x for x in arr if x == 0]) / length_of_array
    
    print(f"{positive}\n{negative}\n{zero}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)