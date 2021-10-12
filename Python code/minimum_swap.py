import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    sorts=0
    i=0
    while i <len(arr):
        index=arr[i]-1
        if arr[i]!=arr[index]:
            arr[i],arr[index]=arr[index],arr[i]
            sorts+=1
        else:
            i+=1
    return sorts
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
