import math
import os
import random
import re
import sys
def staircase(n):
    # Write your code here
    for i in range(n):
        print(' '*(n-i-1) + '#'*(i+1))

    # for i in range(n):
    #     print(' '*n-1-i)
    #     for j in range(n):
    #         print('#' * i+1 ,end=" ")

      

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
