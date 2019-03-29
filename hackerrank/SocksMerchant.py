#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    d = {}
    socks = 0
    if n <= 1:
        return 0
    for s in ar:
        if s not in d:
            d[s] = 1
        else:
            d[s] += 1
            if d[s] == 2:
                socks += 1
                d[s] = 0
    return socks
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
