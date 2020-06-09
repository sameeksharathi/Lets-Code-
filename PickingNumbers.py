'''
Given an array of integers, find and print the maximum number of integers you can select from the array such that the absolute difference
between any two of the chosen integers is less than or equal to 1. For example, if your array is a=[1,1,2,2,4,4,5,5,5], you can create two
subarrays meeting the criterion: [1,1,2,2] and [4,4,5,5,5]. The maximum length subarray has 5 elements.

Function Description:
Complete the pickingNumbers function in the editor below. It should return an integer that represents the length of the longest array
that can be created.

pickingNumbers has the following parameter(s):
a: an array of integers

Input Format:
The first line contains a single integer n, the size of the array a.
The second line contains n space-separated integers a[i].

Output Format:
A single integer denoting the maximum number of integers you can choose from the array such that the absolute difference between
any two of the chosen integers is <=1.
'''



import math
import os
import random
import re
import sys

def pickingNumbers(a):
    arr = sorted(a)
    cnt = []
    for i in range(len(arr)):
        c = 0
        for j in range(i,len(arr)):
            if(abs(arr[i]-arr[j])<=1):
                c+=1
        cnt.append(c)
    return max(cnt)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = pickingNumbers(a)
    fptr.write(str(result) + '\n')
    fptr.close()
    
