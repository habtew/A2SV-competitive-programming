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
    # Write your code here
    main_diag = 0
    axis_diag = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i + j == len(arr) - 1:
                axis_diag += arr[i][j]
            if i == j:
                main_diag += arr[i][j]
    return abs(main_diag - axis_diag)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

