#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    i = 0
    while i < len(c):
        if i == len(c) - 1:
            # last item
            break
        if i < len(c) - 2:
            if c[i+2] == 0:
                i += 2
            else:
                i += 1
        else:
            i += 1
        jumps += 1

    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
